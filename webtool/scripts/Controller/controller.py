from ..crawler.main import main as run_crawler
from ..fuzzer.runscript import run_fuzzer
from multiprocessing import Process, Queue

Process = []

def controller(url, config = {}):
    print(url)
    if config != {}:
        limit = config["limit"]
        run_crawler(url,limit=int(limit))
        #run_fuzzer(url,config["wordlist"],recursion=config["recursion"],depth=config["depth"])
        

    else:
        run_crawler(url)

def run_seq_tests(file):
    with open(file, 'r') as f:
        urls = f.readlines()
    # for url in urls:
    #     Process.append(Process(target=, args=(url,)))
    

def generate_report():
    pass
