# coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep

desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platforVersion']='7.0'
desired_caps['deviceName']='JLF4T18601002720'
desired_caps['appPackage']='com.mymoney'
desired_caps['appActivity']='com.mymoney.biz.splash.SplashScreenActivity'
apkPath = '/Users/danish/PycharmProjects/AppTestDemo/apkPackage/mymoney.apk'
desired_caps['app']=apkPath
desired_caps['autoAcceptAlerts'] = True
desired_caps['reuse'] = 3
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

def get_size():
    x = driver.get_window_size('width')
    y = driver.get_window_size('height')
    return x,y

def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

def swipeUp():
    l = get_size()
    print(l)
    print(len(l))
    x1 =0
    y1=0
    y2 = 0

    if len(l)>1:
        x1 = int(l[0]['width'] * 0.5)
        y1 = int(l[1]['height'] * 0.8)
        y2 = int(l[1]['width'] * 0.1)
    else:
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.8)
        y2 = int(l[1]*0.1)
    driver.swipe(x1,y1,x1,y2,1000)

try:
    nextBtn = driver.find_element_by_id('com.mymoney:id/next_btn')



except NoSuchElementException:
    print('没有下一步按钮')
    pass
else:
    print('有下一步按钮')
    WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id('com.mymoney:id/next_btn'))

    for i in range(2):
        swipeLeft()
        sleep(0.5)
    driver.find_element_by_id('com.mymoney:id/begin_btn').click()



try:
    closeBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closeBtn.click()


#更多按钮点击
# WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id('com.mymoney:id/nav_setting_btn'))
driver.implicitly_wait(8)
moreBtn = driver.find_element_by_id('com.mymoney:id/nav_setting_btn')
# moreBtn = driver.find_elements_by_android_uiautomator('new UiSelector().text("更多")')
moreBtn.click()

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/content_container_ly'))
swipeUp()

#点击高级按钮
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()

#点击密码与手势密码
driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()

#手势密码保护
driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()
sleep(1)

#不知何原因 第二次设置手势密码时报错
for i in range(2):
    TouchAction(driver).press(x=250,y=284).wait(2000)\
    .move_to(x=400,y=434).wait(1000)\
    .move_to(x=545,y=583).wait(1000)\
    .move_to(x=545,y=434).wait(1000)\
    .release().perform()








