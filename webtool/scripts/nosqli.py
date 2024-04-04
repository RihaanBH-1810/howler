import subprocess


def run_nosqli(url):
    process = subprocess.run([
        "./nosql",
        "scan",
        "-t",
        url,], 
        capture_output=True, 
    )
    output=  process.stdout.decode()
    if "NoSQL" in output:
        print(f"NoSQL Injection Detected in {url}")


if __name__ == "__main__":
    run_nosqli("http://localhost:4000/user/lookup?username=test")