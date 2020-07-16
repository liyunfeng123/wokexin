from ddt import ddt,data,unpack
from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
# def get_data(file_name):
#      # 读取本地 CSV 文件
#      rows=[]
#      data_file =open(file_name,'r')
#      reader=csv.reader(data_file)
#      for user in reader:
#          rows.append(user)
#      return rows
def get_data():
   # 写方法传入数据
   return [
          ["16800000015","123456"],
          ["16800000018","123456"]
          ]
@ddt
class YunXunCase(unittest.TestCase):
        def setUp(self):
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                self.driver.get("https://test.yunwoke.com/")
        @data(*get_data())

        # @data(*get_data('haoma.csv'))
        # @data(*get_data('zhanghao.txt'))
        # @data(('16800000015','123456'),('16800000018','123456'))
        @unpack
        def test_case1(self, phone,pwd):

                driver = self.driver
                driver.find_element_by_xpath('//*[@id="homePage"]/nav/section/div[1]/div/div/ul[3]/li[1]/a').click()
                driver.find_element_by_xpath("//input[@placeholder='手机号／邮箱']").send_keys(phone)
                driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys(pwd)
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="app"]/section/article[2]/div/div[2]/div/div[1]/section/button[1]').click()
                time.sleep(5)
                s =driver.find_element_by_xpath('//*[@id="published"]/nav/section/div[2]/ul/li[1]/a').text
                print(s)
                self.assertEqual(s,'首页','失败')
                print("测试成功，结果与预期匹配")


        def tearDown(self):
                self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(YunXunCase("test_case1"))
    #
    # rst_path = "E:\\All_Test\\Test_Result\\test_case1.html"
    # fp = open(rst_path, 'wb')
    #
    # runner = HTMLTestRunner(title='test', description='云讯自动化用例', stream=fp, verbosity=2, retry=0, save_last_try=True)
    # runner.run(testsuite)
