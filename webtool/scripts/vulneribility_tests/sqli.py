import subprocess

def run_sqlmap(target_url):
    # Define the command to run sqlmap with all tests
    # This command includes options for verbosity, database type, and more
    # Adjust the command as needed based on your requirements and the target
    command = [
        'sqlmap', '-u', target_url,
        '--dbs', # Enumerate DBs
        '--tables', # Enumerate tables
        '--dump', # Dump data
        '--batch', # Run in batch mode
        '--threads=5', # Use 5 threads
        '--level=2', # Set level to 5 (aggressive)
        '--risk=3', # Set risk to 3 (high)
    ]

    # Run the command and capture the output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print("sqlmap Output:")
        print(output)
        
        # Store the output to a file
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
