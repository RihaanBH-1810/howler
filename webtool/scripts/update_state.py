import requests

def send_update(task):
    requests.post("url", data={"status": f"{task}_completed"})