import names # -*- coding: UTF-8 -*-
source(findFile("scripts", "common.py"))
source(findFile("scripts", "pages/login_page.py"))
source(findFile("scripts", "pages/home_page.py"))

def main():
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnError = True

    records = testData.dataset("login_data.csv")

    for record in records:
        username = testData.field(record, "Username")
        password = testData.field(record, "Password")
        expected = testData.field(record, "Expected")

        test.startSection("Login data: %s" % username)
        open_page("/")
        lp = LoginPage()
        hp = HomePage()
        lp.login(username, password)
        actual = hp.login_result()
        test.compare(actual, expected, "Expected login result for %s" % username)
        
