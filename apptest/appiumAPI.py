# coding=utf-8
from appium import webdriver
import unittest
import time,os
from apptest import HTMLTestReportCNPy3
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
class appiumDemo(unittest.TestCase):
    #初始化操作
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] ='com.deayea.loganwatch' #'com.nicksong.toastutil'#
        desired_caps['appActivity'] = 'com.deayea.loganwatch.activity.MainActivity' #'.MainActivity'
        desired_caps['unicodeKeyboard']='true'
        desired_caps['resetKeyboard']='true'
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
    def tearDown(self):
        self.driver.quit()

    def test01(self):
        print("哈哈哈")
        time.sleep(5)

#1.测试用例必须以testXXX开头
#2.执行顺序： setUpClass --> setUp--》test1 --》tearDown   setUp --》test2 --》tearDown -->tearDownClass

#3.功能测试用例里边标记我们的自动化可以实现的用例，比如第4个可以自动化实现，那么就test4
# 在脚本里定义test4 (excel中标记的自动化和脚本中的自动化case一一对应)。

'''
        #查找控件的方式
        #1.通过id查找
        #self.driver.find_element_by_id("com.guokr.mentor:id/text_view_tag_name")
        #self.driver.find_elements_by_id("")[0]    列表  集合
        #2.通过name查找   appium 1.7以上已经废掉了
        #self.driver.find_element_by_name("职场发展")
        #3.通过class_name查找
        #self.driver.find_elements_by_class_name("android.widget.TextView")[6]
        #4.通过xpath查找
        #self.driver.find_element_by_xpath("//FrameLayout[0]/LinearLayout[0]/FrameLayout[0]")
        #5.通过uiautomator的方式查找
        # self.driver.find_element_by_android_uiautomator()
        #6.通过uiautomation的方式查找
        #self.driver.find_element_by_ios_uiautomation()

        #对控件操作  以下以element代表控件
        #获取手机屏幕分辨率
        #height=driver.get_window_size()['height'] 获取高
        #width=driver.get_window_size()['width'] 获取宽
        #1.点击
        #element.click()
        #2.点击坐标  手机左上角 (0,0)
        #mobile: 和tap之间需要有一个空格！1.5版本以下
        #self.driver.execute_script("mobile: tap",{"x":0.5*width,"y":0.5*height})
        #1.5版本以上
                            startX     startY     endX         endY
        #3.tap点击
        #TouchAction(self.driver).tap(element).perform()
        #点击坐标
        #TouchAction(self.driver).tap(x=0.5*width,y=0.5*height).perform()
        #滑动
        #self.driver.swipe(0.5*width,0.9*height,0.5*width,0.2*height,2)
                            #起始x点   起始y点    结束x点      结束y点
        #4.滑动flick
        #向上滑动为负数，向下滑动为正数  按住中心点进行滑动
        #向左是负数，向右是正数
        #TouchActions(self.driver).flick(-10,-30).perform()
        #5.对元素进行滑动  向左是负数，向右是整数  最后一个参数是多长时间
        #TouchActions(self.driver).flick_element(element,-100,-100,5).perform()
        #6.swipe滑动  直接滑动
        #startX，startY是滑动的起始坐标；endX和endY是滑动的结束坐标；touchCount (默认 为1): 触摸数量，即手指的个数；
        # duration是滑动的持续时间，单位s。 1.5版本以下
        #self.driver.execute_script("mobile: swipe",{'startX':100,'startY':100,'endX':100,'endY':200,'tapCount':1,'duration':2})


        #7.长按long_press
        #TouchAction(self.driver).long_press(element).perform()
        #8.按着某个点拖到另一个点  按住点
        #TouchAction(self.driver).press(x=0.5*width,y=0.5*height).move_to(x=-0.2*width,y=0).release().perform()

        #9.获取值属性 text
        #e1=element.text
        #10.输入框输入文字
        #desired_caps['unicodeKeyboard']='true'
        #desired_caps['resetKeyboard']='true'
        #首先点击控件 获取到焦点再输入
        #element.click()
        #element.send_keys(u'宝马')
        #11.使用os命令  os命令相当于调用cmd命令
        #os.system("adb shell input text 宝马")

        #断言方式 使用unittest 自带有assert的断言方式
        #1.校验值是否一致  assertEqual  预期值   实际值

        #self.assertEqual(element.text,"搜你想搜")
        #2.校验值不一致
        #self.assertNotEqual("1","2")
        #3.包含关系
        #self.assertIn("你好","你好呀")
        #4.不包含
        #self.assertNotIn("你","他们")
        '''
if __name__ == '__main__':
    suite=unittest.TestSuite()
    unittest.TestLoader().loadTestsFromTestCase(appiumDemo) #加载测试用例类
    # unittest.TestLoader().loadTestsFromModule(apptest)  #测试用例模块  脚本文件的名字
    unittest.TestLoader().loadTestsFromName("appiumAPI.appiumDemo.test1") #通过测试名字加载用例   模块名.类名.测试方法名
    # unittest.TestLoader().loadTestsFromNames(["appiumAPI.appiumDemo.test1","test1"])



    '''
    #1.使用unittest的方式执行用例
    suite = unittest.TestLoader().loadTestsFromTestCase(appiumDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
    '''
    #2.使用HTMLTestRunner方式运行生成报告
    #定义一个单元测试容器  单元测试集  添加多个test


    testsuite=unittest.TestSuite()
    #将测试用例加到测试容器中
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(appiumDemo))

    filename='result.html'
    fp=open(filename,'wb')
    runner=HTMLTestReportCNPy3.HTMLTestRunner(stream=fp,title='XXX测试报告',
                    description='以下是XXX项目XXXX版本UI自动化测试报告：')
    #运行测试用例
    runner.run(testsuite)
    fp.close()

# 1.启动两个 appium server(appium desktop)  指定两组不同的端口 A(port，bootstrap port），B（port,bootstrap port）
# 2.创建两个脚本： 在desired_caps中添加udid参数  (你的设备adb devices取到的值)  Remote后边 端口指定为 A的port,B的port
# 3.分别去执行两个脚本



