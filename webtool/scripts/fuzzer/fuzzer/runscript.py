import subprocess

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
