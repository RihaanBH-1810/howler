# Add missing import statement
from main import main as run_crawler
from runscript import run_fuzzer
from multiprocessing import Process, Queue
import json
from nosqli import run_nosqli
import json


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
        run_fuzzer(url, "./wordlist.txt")
        run_tests()

def run_tests():
    with open("./out/nosql_targets.json", 'r') as f:
        data = f.read()
    data = json.loads(data)
    processes = []
    for target in data:
        p = Process(target=run_nosqli, args=(f"{target['url']}?{target['input_name']}=test",))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print("All tests completed.")
    

def generate_report():

    pass

if __name__ == "__main__":
    controller("http://localhost:4000/", config={})