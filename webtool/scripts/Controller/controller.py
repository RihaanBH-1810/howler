from ..crawler.main import main as run_crawler

def unpack_config(config):
    pass

def  controller(url, config = {}):
    print(url   )
    unpack_config(config)
    run_crawler(url, limit=50)

def generate_report():
    pass