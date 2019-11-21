#coding=utf-8
import unittest,time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import requests
# from ddt import ddt,data,unpack,file_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class T(unittest.TestCase):
    def setUp(self):
        desired={}
        desired['platformName'] = 'Android'
        desired['platformVersion'] = '7.1.1'
        desired['deviceName'] = 'emulator-5554'
        desired['appPackage'] = 'com.deayea.loganwatch'  # 'com.nicksong.toastutil'#
        desired['appActivity'] = 'com.deayea.loganwatch.activity.MainActivity'  # '.MainActivity'
        desired["noReset"]="true"
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired)
    def tearDown(self):
        self.driver.quit()


    def test1(self):

        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.ID,"android:id/content")))
        warnKunag = self.driver.find_element_by_id("android:id/content")
        if warnKunag.is_displayed():
            # self.driver.switch_to.alert("com.deayea.loganwatch:id/action_bar_root")
            # self.driver.switch_to.alert.accept()
            # alertTitle = self.driver.find_element_by_id("com.deayea.loganwatch:id/alertTitle").text
            # self.assertEqual("错误提示", alertTitle)
            #
            # self.driver.implicitly_wait(5)
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.ID,"android:id/button2")))
            # cancelBtn = self.driver.find_element_by_id("android:id/button2")
            cancelBtn = self.driver.find_element_by_class_name("android.widget.Button")
            cancelBtn.click()
            # TouchAction(self.driver).tap(cancelBtn).perform()
            print("取消按钮点击")
            time.sleep(3)


    def test_serect(self):
        print("test_serect 执行")
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "android:id/content")))
        warnKunag = self.driver.find_element_by_id("android:id/content")
        if warnKunag.is_displayed():
            print("弹框在显示")
        else:
            print("弹框不显示")


        # WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.ID,"com.deayea.loganwatch:id/secret")))
        # serect = self.driver.find_element_by_id("com.deayea.loganwatch:id/secret")
        #
        # # WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[1]")))
        # # serectPath = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
        # for i in range(11):
        #     serect.click()
        # TouchAction(self.driver).long_press(serect).perform()
        #
        # time.sleep(3)
        # pingText = self.driver.find_element_by_id("com.deayea.loganwatch:id/ping").text
        # if self.assertEqual(pingText,"PING"):
        #     print("通过")


        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located((By.ID, "com.deayea.loganwatch:id/version")))
            version = self.driver.find_element_by_id("com.deayea.loganwatch:id/version")
            if version.is_displayed():
                if self.assertEqual(version, "6.3.7"):
                    print("版本号一致")
            else:
                print("版本号没显示")
        except :
            pass


if __name__=="__main__":
    a=unittest.TestSuite()
    a.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(T))
    unittest.TextTestRunner(verbosity=2).run(a)
