from selenium import webdriver
import time
import random
from PIL import Image
from base.find_element import FindElement
from util.ShowapiRequest import ShowapiRequest

class RegisterFunction():

    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    # 获取driver并且打开url
    def get_driver(self,url):
        if i == 1:
            driver = webdriver.Safari()
        elif i == 2:
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        print('This is user element :',user_element)
        return user_element

    # 获取生成的随机信息
    def get_range_user(self):
        user_info = ''.join(random.sample('123456789adgdakA', 8))
        return user_info

    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    # 解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "100046", "ea216e4d0d65459abced82ac546f65d2")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        print(res.text)
        text = res.json()['showapi_res_body']['Result']
        return text

    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@sina.com"
        file_name = "./screenshot/test.png"
        code_text = self.code_online(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('password', '1111111')
        self.send_user_info('code_text', code_text)
        self.get_user_element('register_button').click()
        # 此处可重新分出一个方法
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print("注册成功")
        else:
            self.driver.save_screenshot('./screenshot/codeerror.png')
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    for i in range(3):
        url = 'http://www.5itest.cn/register'
        register_function = RegisterFunction(url, i)
        register_function.main()