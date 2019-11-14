from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
chromedriver = '/Users/joone/PycharmProjects/web/chromedriver 3'
driver = webdriver.Chrome(chromedriver)

#driver.find_element_by_tag_name('h4').click()

#단락을 입력받았을때 제목을 긁어오는 함수
def url_change(max_pages):
    page = 1
    title_dict = {}
    title_list=[]
    title_list2=[]
    while page <= max_pages:
        chromedriver = '/Users/joone/PycharmProjects/web/chromedriver 3'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # time.sleep(1)
        driver = webdriver.Chrome(chromedriver,options=options)
        url = 'https://opengov.seoul.go.kr/civilappeal?page=' + str(page)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        s1 = soup.find('div', {'id': 'accordion'})
        s2 = s1.find_all('h4')
        for i in s2:
            title_list.append(i.text)
            title_dict = {i: contents for i, contents in enumerate(title_list)}
        page += 1
    title_dict_df = pd.DataFrame.from_dict(title_dict, orient='index')
    title_dict_df.to_excel("ChatbotData.xlsx",'a')

# resultBatdict_df = pd.DataFrame.from_dict(resultBatdict, orient='index')
# resultBatdict_df.to_excel("test.xlsx", 'a')
#title_list += [i.text for i in s2] #List comprehension !!!!나중에 공부해두기

#각 단락별 상세정보보기를 긁어오는함수
def detail(de_pages):
    de_page = 1
    while de_page <= de_pages:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # time.sleep(1)
        url = 'https://opengov.seoul.go.kr/civilappeal?page='+str(de_page)
        driver.get(url)
        posts = driver.find_elements_by_tag_name('h4')
        postnames = []
        detail_list = []
        detail_dict = {}
        for post in posts:
            postnames.append(post.text)
        for i, postname in enumerate(postnames):
            driver.find_element_by_link_text(postname).click()
            time.sleep(2)
            driver.find_elements_by_class_name('link-orange')[i].click()
            details = driver.find_elements_by_class_name('line-all')
            for i in details:
                detail_list.append(i.text.strip())
                detail_dict = {i: contents for i, contents in enumerate(detail_list)}
            time.sleep(2)
            driver.back()
            time.sleep(2)
        detail_dict_df = pd.DataFrame.from_dict(detail_dict, orient='index')
        detail_dict_df.to_excel("testdetail.xlsx", 'a')
        de_page += 1

# if __name__ == "__main__":
#     detail(2)




# title_dict = {i: contents for i, contents in enumerate(list)}
# df.to_excel('text.xlsx') 데이터프레임 엑셀로만들
  # link = driver.find_element_by_css_selector('#civilappeal-16609591 > div > a')
            # url_new = link.get_attribute('href') 공부해야할거 get.attribute