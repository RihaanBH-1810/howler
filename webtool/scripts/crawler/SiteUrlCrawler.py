from enum import Enum
import requests
import threading
import json
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup


class SiteUrlCrawler:
    class Mode(Enum):
        ALL = 0
        INTERNAL = 1
        EXTERNAL = 2

    def __init__(self, site_base_url, limit, max_threads=10, logging_enabled=False):
        """
        Constructor for SiteCrawler.
        :param site_base_url:
        :param max_threads:
        :param logging_enabled:
        """
        self.site_base_url = site_base_url
        self.site_hostname = urlparse(site_base_url).hostname
        self.logging_enabled = logging_enabled
        self.mode = self.Mode.ALL.value
        self.limit = limit
        self.num = 0
        self.max_threads = max_threads
        self.thread_pool = []
        self.urls_to_search_lock = threading.Lock()
        self.found_url_lock = threading.Lock()
        self.nosql_targets = []
        self.urls_to_search = []
        self.found_urls = []
        self.callback = None

    def crawl(self, mode=None, callback=None):
        """
        Begins the crawling process.
        :return:
        """
        self.mode = self.Mode.ALL if mode is None else mode
        self.callback = callback

        # Build initial starting point URLs to crawl
        found_urls, nosql_targets = SiteUrlCrawler.CrawlerThread(self, self.mode).find_all_urls_on_page(self.site_base_url, False)
        for url in found_urls:
            self.found_url(url, nosql_targets)

        while len(self.thread_pool) < self.max_threads:
            thread = SiteUrlCrawler.CrawlerThread(self, self.mode)
            self.thread_pool.append(thread)
            print("Creating new thread, " + thread.getName())

        for thread in self.thread_pool:
            thread.start()

        # Using list comprehension, wait on all threads completing
        [t.join() for t in self.thread_pool]

        print("All threads completed.")

        self.thread_pool.clear()

        return self.found_urls

    def get_work_item(self):
        """
        Returns a work url for a worker thread.
        :return:
        """
        if self.num > self.limit:
            return self.urls_to_search.clear()

        if len(self.urls_to_search) > 0:
            return self.urls_to_search.pop()

        return None

    def update_nosql_targets(self, targets):
        with open("./scripts/out/nosql_targets.json", 'a') as f:
            f.write(json.dumps(targets, indent=4))

    def found_url(self, url, nosql_targets=None):
        """
        Report a new found url.
        :param url:
        :param nosql_targets: Nosql targets to update
        :return:
        """
        self.found_url_lock.acquire()

        if url not in self.found_urls:
            self.found_urls.append(url)
            self.urls_to_search.append(url)

            print("Found URL \"" + url + "\".")

            if self.callback is not None:
                self.callback(url)

        self.found_url_lock.release()

        if nosql_targets:
            self.update_nosql_targets(nosql_targets)

    class CrawlerThread(threading.Thread):
        def __init__(self, site_crawler, mode):
            super().__init__()
            self.site_crawler = site_crawler
            self.mode = mode

        def run(self) -> None:
            """
            Perform the actual work of popping a url from the shared url queue and then checking the url for any other urls
            that we can additionally check.
            :return:
            """
            while True:
                url = self.site_crawler.get_work_item()

                if url is None:
                    break

                if self.is_internal_url(url) is False:
                    print("Skipping URL \"" + url + "\" cause its external and we dont want to index the internet.")
                    break

                print("Checking URL \"" + url + "\".")
                found_urls, updated_nosql_targets = self.find_all_urls_on_page(url, True)
                self.site_crawler.found_url(url, nosql_targets=updated_nosql_targets)

            print("Completed.")

        def find_all_urls_on_page(self, url, use_callback=True):
            """
            Finds all links referenced by a particular URL and scrapes the name of the input element if it has an input field.
            :param url: The URL to search for links.
            :param use_callback: Whether to use callback function to report found URLs.
            :return: A tuple containing found URLs and updated nosql_targets.
            """
            found_urls = []

            try:
                # Fetch the HTML content of the page
                response = requests.get(url)
                if response.status_code != 200:
                    # If the request fails, return an empty list
                    return found_urls, []

                soup = BeautifulSoup(response.content, "html.parser")

                nosql_targets = []

                # Find all <a> tags for links
                for a in soup.findAll("a"):
                    a_href = a.attrs.get("href")

                    # Skip empty URLs
                    if not a_href:
                        continue

                    # If the URL is relative, make it absolute
                    if a_href.startswith('/'):
                        a_href = urljoin(url, a_href)

                    # Process only HTTP/HTTPS links
                    if not a_href.startswith(("http://", "https://")):
                        continue

                    # Check if it's an internal or external URL based on the crawler mode
                    if self.mode == SiteUrlCrawler.Mode.INTERNAL:
                        if not self.is_internal_url(a_href):
                            continue
                    elif self.mode == SiteUrlCrawler.Mode.EXTERNAL:
                        if self.is_internal_url(a_href):
                            continue

                    # Clean the URL
                    url_parts = urlparse(a_href)
                    clean_url = f"{url_parts.scheme}://{url_parts.netloc}{url_parts.path}"
                    if url_parts.query:
                        clean_url += f"?{url_parts.query}"

                    # Report the found URL
                    if use_callback:
                        self.site_crawler.found_url(clean_url)
                    else:
                        found_urls.append(clean_url)  # Append URL to found_urls list

                # Find all input elements and scrape their names
                for input_element in soup.find_all("input", {"name": True}):
                    input_name = input_element["name"]
                    print(f"Found input element with name '{input_name}'. in {url}")
                    nosql_targets.append({"url": url, "input_name": input_name})

                return found_urls, nosql_targets

            except Exception as e:
                print(f"Error processing URL {url}: {e}")

            return found_urls, []

        def is_internal_url(self, url):
            """
            Checks if a URL is internal or external pointing.
            :param url:
            :return:
            """
            return self.site_crawler.site_hostname in url

        def log(self, message):
            """
            Logging.
            :param message:
            :return:
            """
            if self.site_crawler.logging_enabled:
                print(self.getName() + " (CrawlerThread): " + message)


def main(url, limit=1000):
    queue_set = []
    external_set = []

    crawler = SiteUrlCrawler(url, limit)

    # Get ALL urls and print them
    for url in crawler.crawl(SiteUrlCrawler.Mode.INTERNAL):
        print(url)
        print("**********************")
        if url not in queue_set:
            queue_set.append(url)

    for url in crawler.crawl(SiteUrlCrawler.Mode.EXTERNAL):
        if url not in external_set and url not in queue_set:
            print("external: ", url)
            external_set.append(url)

    if len(queue_set) >= limit:
        print("Exiting crawler since limit reached...")
    else:
        print("Completed Crawling...")

    print("\n\t\tQUEUED")
    for i in queue_set:
        print(i)
    print("\n\t\tEXTERNAL")
    for i in external_set:
        print(i)

