import subprocess


def run_nosqli(url):
    subprocess.run([
        "./nosqli",
        "-u",
        url,
        "-o",
        "./scripts/out/nosql_targets_re.json",
        "-of",
        "json"
    ])
    pass
process = subprocess.run(['python3', '/home/monarch/NoSQLInsanity/NoSQLInsanity.py', '--url', url, '--platform', 'mongodb'], input="1\n1\nd\n1\n2\n", capture_output=True, text=True)