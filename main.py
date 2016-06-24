
# -*- coding: utf-8 -*-
import os, time, re
import urlparse, random, getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def check_job_page(job_id, page_html):

    if 'foram encontradas vagas com os' in page_html.text:
        print 'Erro 410: %s' % job_id
    else:
        html = page_html.prettify("utf-8")
        file_name = "apinfo-%s.html" % job_id
        file_path = 'job_offers/apinfo/%s' % file_name
        if not os.path.isfile(file_path):
            with open(file_path, "wb") as htmlfile:
                htmlfile.write(html)
                print'Created file: %s' % file_name
        else:
            print'File already exists: %s' % file_name


def get_job_opportunity(browser, job_id):
    job_url = 'http://www.apinfo.com/apinfo/inc/list44.cfm?codvaga=%s' % job_id
    browser.get(job_url)
    time.sleep(random.uniform(0.3, 0.5))
    page_html = BeautifulSoup(browser.page_source)
    check_job_page(job_id, page_html)


def main():

    browser = webdriver.PhantomJS(executable_path='./phantomjs/bin/phantomjs')
    browser.get('http://www.apinfo.com')
    print("[+] The bot is starting!")

    """
    home_page = BeautifulSoup(browser.page_source)
    #latest_job_id = get_latest_job_id(home_page)
    latest_job_id = '475001'


    latest_id_int = int(latest_job_id) + 1
    for job_id in reversed(range(latest_id_int)):
        get_job_opportunity(browser, job_id)
    """
    start_id = int("48850")
    for job_id in range(start_id, 94649, 1):
        get_job_opportunity(browser, job_id)

if __name__ == '__main__':
    main()
