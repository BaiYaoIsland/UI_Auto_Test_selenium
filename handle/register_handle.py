'''
第三层 操作层
逻辑处理
被business调用
'''
from Imooc_selenium.page.register_page import RegisterPage

class RegisterHandle():
    def __init__(self):
        self.register_p = RegisterPage()
    # 输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_key(email)

    # 输入用户名
    def send_user_name(self):
        pass

    # 输入密码
    def send_user_password(self):
        pass

    # 输入验证码
    def send_user_code(self):
        pass

    # 获取文字信息
    def get_user_text(self,user_info):
        pass