# -*0 coding: cp949 -*-
from web_crawler import WebCrawler


if __name__ == "__main__":

    web_crawler = WebCrawler('http://postgame.tistory.com', 'titleWrap', 'web_crawler.html')
    if web_crawler.proc_chkupdate() is True:
        print 'No update!'
    else:
        print 'New update!'
