# -*0 coding: cp949 -*-
import sys
from web_crawler import WebCrawler


if __name__ == "__main__":
    web_crawler = WebCrawler('http://postgame.tistory.com', 'titleWrap', 'c:/web_crawler.html')
    if web_crawler.proc_chkupdate() is True:
        print 'No update'
        sys.exit('ok!')
    else:
        print 'New update'
        sys.exit('error!')
