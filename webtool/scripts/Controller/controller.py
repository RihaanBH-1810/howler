from ..crawler.crawler import run_crawler

def unpack_config(config):
    pass

def  controller(url, config):
    print(url   )
    unpack_config(config)
    run_crawler(url)

