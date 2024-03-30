import subprocess

def run_sqlmap(target_url):

    command = [
        'sqlmap', '-u', target_url,
        '--dbs', 
        '--tables',
        '--dump',
        '--batch', 
        '--threads=5', 
        '--level=2', 
        '--risk=3', 
    ]

    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print("sqlmap Output:")
        print(output)
        

        with open('sqlmap_output.txt', 'w') as file:
            file.write(output)
        print("Output stored in sqlmap_output.txt")
    except subprocess.CalledProcessError as e:
        print("sqlmap execution failed:", e.output)

def main():
    target_url = input("Enter the URL to scan with sqlmap: ")
    run_sqlmap(target_url)

if __name__ == "__main__":
    main()
