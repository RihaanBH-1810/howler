from .main import main as run_crawler
from .runscript import run_fuzzer
from multiprocessing import Process, Queue, Pool
import json
from multiprocessing import JoinableQueue
import subprocess

from bane.scanners.vulnerabilities import SSRF_Scanner
from bane.scanners.vulnerabilities import XSS_Scanner
from bane.scanners.vulnerabilities import CSRF_Scanner
import requests


no_sqli_queue = Queue()
csrf_queue = Queue()
ssrf_queue = Queue()
xss_queue = Queue()



def save_results(results, filename):
    with open(f"./scripts/out/{filename}.json", 'w') as f:
        print("erro4 here")
        f.write(json.dumps(results, indent=4))

def run_nosqli(url):
    process = subprocess.run([
        "./scripts/nosql",
        "scan",
        "-t",
        url,], 
        capture_output=True, 
    )
    output = process.stdout.decode('utf-8')
    if "NoSQL" in output:
        print(f"NoSQL Injection Detected in {url}")
        no_sqli_queue.put({"url": url, "vulnerable": True, "data": output})
    else:    
        print(f"NoSQL Injection Not Detected in {url}")
        no_sqli_queue.put({"url": url, "vulnerable": False, "data": output})

def controller(url, config = {}):
    print(url)
    if config != {}:
        limit = config["limit"]
        recursion_depth = config["recursion_depth"]
        recursion = config["recursion"]
        run_crawler(url,limit=int(limit))
        if recursion:
             run_fuzzer(url,config["wordlist"],recursion=recursion ,depth=recursion_depth)
        run_fuzzer(url,config["wordlist"],recursion=config["recursion"],depth=config["depth"])
        

    else:
        run_crawler(url)
        print("\n" + "done crawling" + "\n")
        run_fuzzer(url, "./scripts/wordlist.txt")
        print("\n" + "done fuzzing" + "\n")
        # run_nosql_tests()
        print("\n" + "done nosql" + "\n")
        # run_basic_scan_tests(url)
        print("\n" + "done basic scan" + "\n")
        # run_csrf_tests(base_url=url)
        # run_ssrf_tests(base_url=url)
        run_xss_tests(base_url=url)

def run_nosql_tests():
    global no_sqli_queue

    with open("./scripts/out/nosql_targets.json", 'r') as f:
        data = f.read()
    data = json.loads(data)
    processes = []
    results = []
    for target in data:
        p = Process(target=run_nosqli, args=(f"{target['url']}?{target['input_name']}=test",))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
        
    while not no_sqli_queue.empty():
        results.append(no_sqli_queue.get())
    save_results(results, "nosql_results")

def run_ssrf_tests(base_url):
    global ssrf_queue
    ssrf_results = []
    with open('./scripts/out/links.json', 'r') as f:
        data = f.read()
    data = json.loads(data)
    response = requests.get(base_url)
    cookies = response.cookies
    for cookie in cookies:
        name = cookie.name,
        value = cookie.value
    cookie_string = f"{name}={value}"
    

    pool = Pool()
    pool.starmap(bane_ssrf, [(target["url"], cookie_string) for target in data])
    pool.close()
    pool.join()
    
        
    while not ssrf_queue.empty():
        ssrf_results.append(ssrf_queue.get())
    save_results(ssrf_results, "ssrf_results")


def bane_ssrf(url,cookie):

    scan_result = SSRF_Scanner.ssrf_check(
        u=url,
        cookie=cookie,
        timeout=120,
    )
    if type(scan_result) == tuple:
        data = {"url" : url, "vulnerable" : scan_result[0], "data" : scan_result}
        ssrf_queue.put(data)
    else:
        data = {"url" : url, "vulnerable" : "error checking", "data" : "not available"}
        ssrf_queue.put(data)

def run_csrf_tests(base_url):
    csrf_results = []
    with open('./scripts/out/links.json', 'r') as f:
        data = f.read()
    response = requests.get(base_url)
    cookies = response.cookies
    for cookie in cookies:
        name = cookie.name,
        value = cookie.value
    cookie_string = f"{name}={value}"
    data = json.loads(data)
    pool = Pool()
    pool.starmap(bane_csrf, [(target["url"], cookie_string) for target in data])
    pool.close()
    pool.join()
    

    while not csrf_queue.empty():
        csrf_results.append(csrf_queue.get())   
    print("done")
    print(csrf_results)
    save_results(csrf_results, "csrf_results")
    

def run_xss_tests(base_url):
    xss_results = []
    with open('./scripts/out/links.json', 'r') as f:
        data = f.read()
    response = requests.get(base_url)
    cookies = response.cookies
    for cookie in cookies:
        name = cookie.name,
        value = cookie.value
    cookie_string = f"{name}={value}"
    print(response.cookies)
    data = json.loads(data)
    pool = Pool()
    pool.starmap(bane_xss, [(target["url"], cookie_string) for target in data])
    pool.close()
    pool.join()
    

    while not xss_queue.empty():
        xss_results.append(xss_queue.get())   
    print("done")
    print(xss_results)
    save_results(xss_results, "xss_results")

def run_basic_scan_tests(url):
    try:
        subprocess.run(['wapiti', '-u', url, '-m', 'xss,',"-o","./scripts/out/basic_scan_results.json", "-f", "json"], check=True)        
        print("Wapiti scan completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error running Wapiti:", e)


def bane_csrf(url, cookie):
    scan_result = CSRF_Scanner.csrf_forms(
        url,
        cookie=cookie,
    )

    if scan_result != [] and type(scan_result) == list:
        data = {"url" : url, "vulnerable" : True,"data" :scan_result[0]["status"]}
        csrf_queue.put(data)
    elif type(scan_result) == bool:
        data = {"url" : url, "vulnerable" : scan_result, "data" : "notavaialble"}
        

def bane_xss(url,cookie):
    print("running xss")
    scan_result = XSS_Scanner.scan(
        u=url,
        max_pages=1,
        cookie=cookie,
    )
    print("i am here")
    if scan_result["result"] != []:
        print("i am here")     
        data = {"url" : url, "vulnerable" : True,"method":scan_result['result'][0]['result'][0]['method'], "data" : "not available"}
        xss_queue.put(data) 
    elif scan_result["result"] == []:
        data = {"url" : url, "vulnerable" : False, "data" : "not availabsle"}
        xss_queue.put(data)




    

def generate_report():
    pass

if __name__ == "__main__":
    controller("http://localhost:4000/", config={})