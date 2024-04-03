import subprocess
import pprint
import json


def clear_file():
    with open("./out/log.json", "w") as f:
        f.write("")
    f.close()

def run_fuzzer(url, wordlist, recursion=False, depth=0):
    if recursion:
        subprocess.run([
        "./ffuf",
        "-u",
        url,
        "-w",
        wordlist,
        "-o",
        "./out/log.json",
        "-of",
        "json",
        "-recursion-depth",
        depth,
        "-recursion",
        "-fc",
        200
    ])
    else:
        subprocess.run([
        "./ffuf",
        "-u",
        url,
        "-w",
        wordlist,
        "-o",
        "./out/log.json",
        "-of",
        "json"
    ])
        
def clean_data():
    cleaned_data = []
    with open("./out/log.json", "r") as f:
        data = f.read()
    f.close()
    data = json.loads(data)
    results_list = data["results"]
    for result in results_list:
        if result["status"] == 200:
            cleaned_data.append({"url": result["url"]})

    with open("./out/log.json", "w") as f:
        f.write(json.dumps(cleaned_data))
    f.close()
    
    pprint.pprint(data)

def compare_data():
    with open("./out/log.json", "r") as f:
        data = f.read()
    f.close()
    data = json.loads(data)
    return data

if __name__ == "__main__":
    clear_file()
    run_fuzzer("https://github.com/FUZZ", "wl.txt")
    clean_data()
    # send_update("fuzzer")
