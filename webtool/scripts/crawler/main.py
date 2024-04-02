from .SiteUrlCrawler import SiteUrlCrawler

def write_to_file(data,filename):
    with open(filename, 'w') as f:
        for item in data:
            f.write("%s\n" % item)


def main(url, limit):
    queue_set = []
    external_set =[]
    # url=input("Enter the base url: ")
    # limit = int(input("Enter the limit for crawling: "))
    # Create a site crawler with 5 threads and allowing logging
    crawler = SiteUrlCrawler(url,limit)

    # Get ALL urls and print them
    for url in crawler.crawl(SiteUrlCrawler.Mode.INTERNAL):
        if url not in queue_set :
            queue_set.append(url)
    
    for url in crawler.crawl(SiteUrlCrawler.Mode.EXTERNAL):
            if url not in external_set and url not in queue_set:
                print("external: ", url)
                external_set.append(url)
    
    # print("\ncrawled:\n")
    # for i in crawled_set:print(i)
    # print("\nque:\n")
    # for i in queue_set:print(i)

    
    # while len(queue_set)!=0 and len(crawled_set)<limit:
    #     crawler = SiteUrlCrawler(queue_set[0],limit-len(queue_set))
    #     # print("\ncrawling:",queue_set[0],"\n")
    #     for url in crawler.crawl(SiteUrlCrawler.Mode.INTERNAL):
    #         if url not in queue_set and url not in crawled_set:
    #             queue_set.append(url)
    #     for url in crawler.crawl(SiteUrlCrawler.Mode.EXTERNAL):
    #         if url not in external_set and url not in crawled_set and url not in queue_set:
    #             print("external: ", url)
    #             external_set.append(url)
    #     temp = queue_set.pop(0)
    #     if temp not in crawled_set:
    #         print("crawled: ", temp)
    #         crawled_set.append(temp)
        
        # print("\ncrawled:\n")
        # for i in crawled_set:print(i)
        # print("\nque:\n")
        # for i in queue_set:print(i)
            
    if len(queue_set)>=limit:
        print("Exiting crawler since limit reached...")
    else:
        print("Completed Crawling...")

    write_to_file(queue_set,"queue.txt")
    write_to_file(external_set,"external.txt")
    
    print("\n\t\tQUEUED")
    for i in queue_set:
        print(i)
    print("\n\t\tEXTERNAL")
    for i in external_set:
        print(i)

