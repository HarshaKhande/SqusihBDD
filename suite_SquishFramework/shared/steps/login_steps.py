# -*- coding: UTF-8 -*-
source(findFile("scripts", "common.py"))
source(findFile("scripts", "pages/login_page.py"))
source(findFile("scripts", "pages/home_page.py"))

@Given("the login page is open")
def open_login_page(context):
    open_page("/")
    context.userData["login_page"] = LoginPage()
    context.userData["home_page"] = HomePage()

@When("I login with username |word| and password |word|")
def login_with_credentials(context, username, password):
    context.userData["login_page"].login(username, password)

@Then("the login result should be |word|")
def verify_login_result(context, expected):
    actual = context.userData["home_page"].login_result()
    test.compare(actual, expected, "Verify login result")

@Then("the welcome message should contain |word|")
def verify_welcome(context, expected_word):
    actual = context.userData["home_page"].welcome_text()
    test.verify(expected_word in actual, "Welcome message should contain '%s'" % expected_word)
