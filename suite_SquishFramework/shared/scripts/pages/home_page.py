# -*- coding: UTF-8 -*-
source(findFile("scripts", "config.py"))

class HomePage:
    def __init__(self):
        self.result = names.loginResult
        self.welcome = names.welcomeMessage
        self.logout_button = names.logoutButton

    def login_result(self):
        obj = waitForObjectExists(self.result, DEFAULT_TIMEOUT)
        return str(obj.innerText).strip()

    def welcome_text(self):
        obj = waitForObjectExists(self.welcome, DEFAULT_TIMEOUT)
        return str(obj.innerText).strip()

    def is_logout_visible(self):
        return object.exists(self.logout_button)

    def logout(self):
        clickButton(waitForObject(self.logout_button, DEFAULT_TIMEOUT))
