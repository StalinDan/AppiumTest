# coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '192.168.3.141:5555 '
desired_caps["appPackage"]="com.tal.kaoyan"
desired_caps["appActivity"]="com.tal.kaoyan.ui.activity.SplashActivity"
desired_caps['app'] = r'/Users/danish/PycharmProjects/AppTestDemo/apkPackage/kaoyan3.1.0.apk'
desired_caps['noRest'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


#用于检测不知是否有此按钮
def checkCancelBtn():
    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def checkSkipBtn():
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

checkCancelBtn()
checkSkipBtn()
