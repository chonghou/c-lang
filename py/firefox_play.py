import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup as bs
import csv

class Search:
    def __init__(self,isshow):
        self.setUpFirefox(isshow)

    def setUpFirefox(self,is_show):
        # 设置Firefox下载exe格式的文件，不弹出下载窗，直接下载到指定路径
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', '.')
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        # 参数 application/octet-stream 表示下载exe文件无需弹窗确认，直接下载
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')
        options = webdriver.FirefoxOptions()
        if is_show:
            options.add_argument('-head')#“有头”模式，即可以看到浏览器界面，若要隐藏浏览器，可设置为 "headless"
        else:
            #Firefox headless模式运行
            options = webdriver.FirefoxOptions()
            options.add_argument('-headless')

        #实例化对象时，将设置的Firefox参数传入
        self.driver = webdriver.Firefox(firefox_profile=profile,options=options)
        self.driver.implicitly_wait(10)
  

    def __del__(self):
        self.driver.close()

    def get(self,url):
        time.sleep(2)
        self.driver.get(url)
        return bs(self.driver.page_source).prettify()
    
    # def new_tab(self):
    #     self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    #     windows = self.driver.window_handles
    #     self.driver.switch_to.window(windows[-1])
    #     # ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
    
    # def close_tab(self):
    #     ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

    def scrollDown(self):
    #执行js实现滚轮向下滑动
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        time.sleep(2)
 
    def searchBaidu(self,keywords):
        
        self.driver.get("https://www.baidu.com")
        searchline = self.driver.find_element_by_css_selector('.s_ipt')
        searchline.clear()
        searchline.send_keys(keywords)
        searchbt = self.driver.find_element_by_css_selector('.s_btn')
        searchbt.click()
        
        try:
            # element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,'百科')))
            from selenium.webdriver.support.wait import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
 
            self.driver.find_element_by_partial_link_text('百科').click() 
            
            # locator = (By.LINK_TEXT, keywords)
            # WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            time.sleep(10)
            print(self.driver.page_source)
            # self.driver.find_element_by_partial_link_text(keywords).click()
            # soup = bs(self.driver.page_source, 'lxml')#page_source得到当前网页的源代码
            # # dr.quit()#关闭浏览器
            # # return soup.select_one('.rating_sum').text
            # print(soup.get_text())
            # print(self.driver.page_source)
        except Exception as e:
            print(e)
       
    
    def searchMoveinDouban(self,movie_name):
        self.driver.get('https://movie.douban.com/')#打开豆瓣电影
        self.driver.find_element_by_id('inp-query').send_keys(movie_name)#找到输入框并填写电影名
        self.driver.find_element_by_class_name('inp-btn').click()#找到搜索按钮并点击
        try:
            self.driver.find_element_by_partial_link_text(movie_name).click()#找到包含电影名的最近链接并点击，打开电影具体信息页面
            soup = bs(self.driver.page_source, 'lxml')#page_source得到当前网页的源代码
            dr.quit()#关闭浏览器
            return soup.select_one('.rating_sum').text
        except:
            return 'null'
 
 

if __name__ == '__main__':
    names = ['战狼2', '行动']#电影名列表
    s=Search(True)
    s.searchBaidu(names[1])
    # for n in names:
    #     s.searchBaidu(n)
        
     

 
# main()
