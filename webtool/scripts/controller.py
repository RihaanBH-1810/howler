# Add missing import statement
from .main import main as run_crawler
from .runscript import run_fuzzer
from multiprocessing import Process, Queue
import json
import subprocess
no_sqli_queue = Queue()

def save_results(results):
    with open("./scripts/out/nosql_results.json", 'w') as f:
        f.write(json.dumps(results, indent=4))
    f.close()

def run_nosqli(url):
    process = subprocess.run([
        "./scripts/nosql",
        "scan",
        "-t",
        url,], 
        capture_output=True, 
    )
    output = process.stdout.decode()
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
        run_fuzzer(url, "./scripts/wordlist.txt")
        run_tests()

def run_tests():
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
    save_results(results)

def generate_report():

    pass

if __name__ == "__main__":
    controller("http://localhost:4000/", config={})