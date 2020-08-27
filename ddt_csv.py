# coding=utf-8
# !/usr/bin/python
import csv
import codecs
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
import unittest

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)  # 关掉浏览器左上角的通知提示，如上图
options.add_argument('disable-infobars')  # 关闭'chrome正受到自动测试软件的控制'提示


class Test_Demo(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.get("https://ent.yunwoke.com/app/message")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.find_element_by_xpath("//input[@placeholder='手机号／邮箱']").send_keys("16800000013")
        cls.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
        cls.driver.find_element_by_xpath('//button[@class="next-btn"][1]').click()
        # 等待
        cls.driver.implicitly_wait(18)
        cls.driver.find_element_by_xpath("//p[text()='跳过']").click()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        pass


    def test_addhaoyou(self):
        driver = self.driver

        driver.find_element_by_xpath('//*[@id="companyHeader"]/div/div/div[3]/div[3]/img').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/ul/a[4]/li').click()

        wins = driver.window_handles
        driver.switch_to.window(wins[1])
        driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/div[2]/ul/li[2]/div[1]/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="/admin/org$Menu"]/li[1]/a').click()
        driver.implicitly_wait(8)
        # 读取本地 CSV 文件
        datas = csv.reader(codecs.open('phone.csv', 'r', 'utf_8_sig'))

        for user in datas:
            # 添加成员
            driver.find_element_by_css_selector('#root > section > section > main > div > main > div > div.main > div > div.list-hd > div.action > button:nth-child(1)').click()
            # driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/main/div/div[2]/div/div[1]/div[2]/button[1]/span').click()
            # 输入手机号
            driver.find_element_by_xpath('//*[@id="memberPhone"]').send_keys(user[1])
            # 输入姓名
            driver.find_element_by_xpath('//*[@id="memberName"]').send_keys(user[0])
            # 员工类型
            driver.find_element_by_xpath('//*[@id="memberType"]/div/div').click()
            driver.find_element_by_xpath("//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[1]").click()
            driver.get_screenshot_as_file('E:\\zidonghua\\haoma.png')
            try:
                # 保存
                driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[3]').click()
                driver.implicitly_wait(5)

            finally:
                # c = driver.find_element_by_xpath('/html/body/div[5]/div/span/div/div/div/span').text
                # print(c)
                driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]').click()
                driver.implicitly_wait(5)





if __name__ == '__main__':
    unittest.main()
