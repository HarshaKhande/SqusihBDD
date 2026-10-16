# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names

@Given("the browser is launched")
def open_login_page(context):
    open_page("/")
    context.userData["login_page"] = LoginPage()
    context.userData["home_page"] = HomePage()

@When("I enter invalid credentials")
def login_with_credentials(context, username, password):
    context.userData["login_page"].userlogin(username, password)

@When("I click login button")
def clickLoginButton(context):
    test.warning("TODO implement error message should be displayed")

@Then("error message should be displayed")
def step(context):
    test.warning("TODO implement error message should be displayed")





@Given("QA Environment is up and running")
def open_browser(context):
    open_page("/")
    context.userData["login_page"] = LoginPage()
    context.userData["home_page"] = HomePage()


@When(r'user enters "([^"]+)" and "([^"]+)"', regexp=True)
def enterCredentails(context, username, password):
    context.userData["login_page"].userlogin(username, password)

@When("user clicks on login button")
def clickLoginButton(context):
    context.userData["login_page"].click_login()   

@Then("user is navigated to home page")
def validatehomepage(context):
    test.log("User is navigated to home page")
    




