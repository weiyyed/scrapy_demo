# -*- coding: utf-8 -*-
import re

import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Yun3Spider(scrapy.Spider):
    name = 'yun3'
    allowed_domains = ['http://sy.51gxc.com',
                       'http://p.51gxc.com',
                       'http://passport.51gxc.com',
                       ]
    # start_urls = ['http://http://portal.51gxc.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    def start_requests(self):
        url = 'http://p.51gxc.com/'
        cookies,csrf=self.login_yun(url)
        self.headers.update({"csrf":csrf})
        return  [scrapy.Request(url,headers=self.headers,cookies=cookies,callback=self.parse_portal)]
    def parse(self, response):
        pass
    def parse_portal(self, response):
        # links=response.css("a::text").getall()
        print("测试输出：",response.body)
    def login_yun(self,url):
        option=Options()
        option.add_argument("--headless")
        option.add_argument("--disable-gpu")
        driver=webdriver.Chrome(chrome_options=option)
        driver.get(url)
        driver.find_element_by_id("name").send_keys("1031")
        driver.find_element_by_id("pwd1").send_keys("1")
        driver.find_element_by_xpath(r'//a[@onclick="login()"]').click()
        time.sleep(1)
        # 设置等待
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/script")))
        time.sleep(1)
        cookies = driver.get_cookies()
        html_source = driver.page_source
        csrf = re.search("window.csrf = '(.*?)'", html_source).group(1)
        driver.close()
        return cookies,csrf
        # 设置requests的session
