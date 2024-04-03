import subprocess

def run_nosqlinsanity(url):
    try:
        subprocess.run(['python3','/home/monarch/NoSQLInsanity/NoSQLInsanity.py', '--url',url,'--platform','mongodb'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        #stdout, stderr=process.communicate(input="1\n1\nd\n"+a+"\n"+b+"\n")
        
        #print(stdout)
    except subprocess.CalledProcessError as e:
        print("Error running NoSQLInsanity:", e)

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    #a=input("1. Send data as Get request (press 1)\n2. Send data as Post request (press 2)")
    #b=input("1. Use Linear Search (press 1)\n2. Use Binary search (press 2)")
    run_nosqlinsanity(url)