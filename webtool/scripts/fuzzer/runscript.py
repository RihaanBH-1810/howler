import subprocess
import pprint, json, requests
from bs4 import BeautifulSoup


def save_to_file(link, input_name):
    with open("../out/nosql_targets.json", "w") as f:
        data = f.read()
    f.close()
    data = json.loads(data)
    data.append({"url": link["url"], "input_name": input_name})
    with open("../out/nosql_targets.json", "w") as f:
        f.write(json.dumps(data, indent=4))
    f.close()


def clear_file():
    with open("../out/fuzzer.json", "w") as f:
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
        "../out/fuzzer.json",
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
        "../out/fuzzer.json",
        "-of",
        "json"
    ])
        
def clean_and_handle_data():
    cleaned_data = []
    with open("../out/fuzzer.json", "r") as f:
        data = f.read()
    f.close()
    data = json.loads(data)
    results_list = data["results"]
    for result in results_list:
        if result["status"] == 200:
            cleaned_data.append({"url": result["url"]})

    with open("../out/links.json", "r") as f:
        links =  f.read()
    f.close()
    links = json.loads(links)
    for link in cleaned_data:
        for l in links:
            if link["url"] == l["url"]:
                cleaned_data.remove(link)
            else:
                pass
    res = cleaned_data + links
    res = [dict(t) for t in {tuple(d.items()) for d in res}]
    print(res)
    with open("../out/links.json", "w") as f:
         f.write(json.dumps(res, indent=4))
    f.close
    check_for_input_fields(cleaned_data)        
    
    
def check_for_input_fields(links):
    for link in links:
        response = requests.get(link["url"])
        soup = BeautifulSoup(response.text, "html.parser")
        for input_element in soup.find_all("input", {"name": True}):
            input_name = input_element["name"]
            print(f"Found input element with name '{input_name}'. in {link}")
            save_to_file(link, input_name)

        
        else:
            print("No input fields found in this link")



if __name__ == "__main__":
    clear_file()
    run_fuzzer("https://github.com/FUZZ", "wl.txt")
    clean_and_handle_data()
    
    # send_update("fuzzer")
