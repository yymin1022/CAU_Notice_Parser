from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100&CONTENTS_NO=1&P_TAB_NO=1#;"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

chrome_driver = "/media/yong/Local Disk/AppProjects/CAU_Notice_Parse/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
ul_notice = soup.find("ul", id="tbody")
for li in ul_notice.find_all("li"):
    print(li.find("div", class_="txtL").find("a").text)