# coding=utf-8
import time
import os
import unittest
from appium import webdriver
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired={}
        desired["appPackage"]="com.guokr.mentor"
        desired["appActivity"]=".activity.MainActivity"
        desired["platformVersion"]='7.1.1'
        desired["platformName"]="Android"
        desired["deviceName"]="Android"
        desired["noReset"]="true"
        # desired['unicodeKeyboard']='true'
        # desired['resetKeyboard']='true'
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired)
    def tearDown(self):
        self.driver.quit()
    def test1(self):
        time.sleep(4)
        #https://blog.csdn.net/Sily_Z/article/details/82981279
        #1.使用text文本定位语法
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("职场发展")').click()
        #2.如果文本比较长，使用textContains模糊匹配
        # self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("互")').click()
        #3.用textStartsWith以某个文本开头来匹配
        # self.driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("互联")').click()
        #4.使用正则表达式匹配
        #https://blog.csdn.net/maocaowu_csdn/article/details/50749474  只要包含"联"字的text值  都会被匹配
        # self.driver.find_element_by_android_uiautomator('new UiSelector().textMatches(".*联.*")').click()
        #5.使用resource-id定位
        # self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.guokr.mentor:id/text_view_tag_name")')[2].click()
        #6.通过className进行定位
        # self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')[3].click()
        #7.通过description 也就是content-desc
        # self.driver.find_element_by_android_uiautomator('new UiSelector().description("content-desc属性")').click()
        #组合定位方式
        #8.id与text属性组合
        # self.driver.find_element_by_android_uiautomator('resourceId("com.guokr.mentor:id/text_view_tag_name").text("互联网")').click()
        #9.class与text属性组合
        # self.driver.find_element_by_android_uiautomator('className("android.widget.TextView").text("互联网")').click()
        #关系定位
        #10.父子定位childSelector   通过先定位父元素再定位子元素
        # self.driver.find_element_by_android_uiautomator('resourceId("com.guokr.mentor:id/recycler_view_tag_list").childSelector(className("android.view.ViewGroup").instance(2))').click()
        #11.兄弟定位fromParent   通过同一个父元素然后定位一个子元素     顶部搜索框  PS:使用该方式定位时，是定位到这个控件的"上一个兄弟控件",如果没有上一个兄弟控件，则就定位它自己
        # self.driver.find_element_by_android_uiautomator('resourceId("com.guokr.mentor:id/constraint_layout_title_bar").fromParent(resourceId("com.guokr.mentor:id/text_view_location"))').click()
        #12.通过instance定位
        #instance方法会将界面上所有相同类型的控件按顺序取出来，放到一个集合里，然后按照控件在集合的角标把想要的控件取出来；
        # 而index则是通过该控件所在层级的节点角标将对应的控件取出来。
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.guokr.mentor:id/text_view_tag_name").instance(2)').click()
        #13.通过index定位
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.guokr.mentor:id/recycler_view_tag_list").childSelector(className("android.view.ViewGroup").instance(2)).childSelector(className("android.widget.TextView").index(1))').click()
        time.sleep(3)

if __name__ == '__main__':  #运行入口
    suite=unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # testsuite=unittest.TestSuite()
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
    # fp=open("result.html","wb")
    # runner=HTMLTestReportCN.HTMLTestRunner(stream=fp,description="test")
    # runner.run(testsuite)
    # fp.close()



