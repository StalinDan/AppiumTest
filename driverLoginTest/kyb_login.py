from driverLoginTest.capability import driver,NoSuchElementException

def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('自学网2018')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()


try:
    myTabBtn = driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
except NoSuchElementException:
    print('没有我的Tab')
    login()
else:
    print('有我的Tab')
    myTabBtn.click()
    userName = driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').text
    if userName == '未登录':
        print('未登录')
        # 点击未登录
        driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
        login()
    else:
        print('已经登录')
        # 点击退出
        setBtn = driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        exitBtn = driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
        alert = driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()
        login()
