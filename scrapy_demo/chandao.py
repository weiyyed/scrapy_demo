# 禅道脚本生成
# http://192.168.6.182/zentao
# id="account"
# name="password"
# id="submit"
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


url= "http://192.168.6.182/zentao"
option = Options()
option.add_argument("--headless")
option.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=option)
driver.get(url)
driver.find_element_by_id("account").send_keys("weiyongyou")
driver.find_element_by_name("password").send_keys("a123456")
driver.find_element_by_id('submit').click()
time.sleep(1)
cookies = driver.get_cookies()

sess = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
}
sess.headers.update(headers)
for cookie in cookies:
    sess.cookies.set(cookie["name"], cookie["value"])
driver.close()
chandao_url="http://192.168.6.182/zentao/bug-browse-41-0-unresolved.html"
while chandao_url=="":
    chandao_url = input("input chandao url:")
text=sess.get(chandao_url).text

bf=BeautifulSoup(text,"lxml")
ids=bf.select('tr td.c-id.cell-id a')
# ids=bf.select("tr td.c-id.cell-id")
for id in ids:
    id.get_text()
    print(id.get_text())

    pager - label    li.pager - item - left.pager - item