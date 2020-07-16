# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack
from BeautifulReport import BeautifulReport
import os
from lxml import etree




class YunXunCase(unittest.TestCase):

    driver = None
    img_path = 'img'

    @staticmethod
    def parse(html, xpath):
        """
            解析页面中的元素并返回一个对象
        :param xpath: 需要获取页面中的元素对应的xpath
        :param html: 页面的html元素
        :return:
        """
        return etree.HTML(html).xpath(xpath)

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass




    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def tearDown(self):
        self.driver.quit()

    @BeautifulReport.add_test_img('搜索结果','输入python')
    def test_case1(self):
        """
        验证百度搜索结果
        """

        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
        self.save_img('输入python')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(1)
        self.save_img('搜索结果')







if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(YunXunCase('test_case1'))
    result = BeautifulReport(test_suite)
    rst_path = "E:\\Test_yunwoke\\Test_Result"
    result.report(filename='百度自动化测试报告', description='百度自动化用例', log_path=rst_path)