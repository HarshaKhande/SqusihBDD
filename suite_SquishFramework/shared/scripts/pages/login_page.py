# -*- coding: UTF-8 -*-
import names
source(findFile("scripts", "config.py"))

class LoginPage:

    # locators + page actions or the functions
    def __init__(self):

        self.username = names.usernameInput
        self.password = names.passwordInput
        self.login_button = names.loginButton
        self.result = names.loginResult

    def enter_username(self, username):
        setText(waitForObject(self.username, DEFAULT_TIMEOUT), username)
        test.log("Entered username", username)

    def enter_password(self, password):
        setText(waitForObject(self.password, DEFAULT_TIMEOUT), password)
        test.log("Entered password", "***")

    def click_login(self):
        clickButton(waitForObject(self.login_button, DEFAULT_TIMEOUT))
        test.log("Clicked Login button")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
    def userlogin(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
     

    def get_result(self):
        result = waitForObjectExists(self.result, DEFAULT_TIMEOUT)
        waitFor(lambda: str(result.innerText).strip() != "", DEFAULT_TIMEOUT)
        return str(result.innerText).strip()

    def clear(self):
        setText(waitForObject(self.username, DEFAULT_TIMEOUT), "")
        setText(waitForObject(self.password, DEFAULT_TIMEOUT), "")
