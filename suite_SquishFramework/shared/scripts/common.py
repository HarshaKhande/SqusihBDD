# -*- coding: UTF-8 -*-
source(findFile("scripts", "config.py"))

def open_page(path="/"):
    url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")
    if isBrowserOpen():
        activeBrowserTab().setUrl(url, DEFAULT_TIMEOUT)
    else:
        startBrowser(url, DEFAULT_TIMEOUT)
    test.log("Opened page", url)

def wait_for_text(object_name, expected, timeout=DEFAULT_TIMEOUT):
    obj = waitForObjectExists(object_name, timeout)
    ok = waitFor(lambda: str(obj.innerText).strip() == expected, timeout)
    test.verify(ok, "Wait for text '%s'" % expected)
    return obj

def capture_failure(message, error=None):
    test.fail(message)
    if error is not None:
        test.log("Exception", str(error))
    try:
        test.attachDesktopScreenshot("Failure state")
    except Exception as screenshot_error:
        test.warning("Unable to attach desktop screenshot", str(screenshot_error))
