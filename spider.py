from urllib.request import urlopen
from link_finder import linkfinder
from general import * 

class Spider:

    #class variables
    project_name = ''
    domain_name = ''
    base_url = ''
    queue_file =''
    crawled_file = ''
    queue = set()
    crawled = set() 

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = crawled_file+'/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    def boot(self):
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled= file_to_set(Spider.crawled_file)
        

