from EnvSetup.BrowserSetup import Browser
import time


class VarsAll:
    try:
        brow = Browser()
        driver = brow.LaunchBrowser('firefox','https://traveltriangle.com/')
        time.sleep(2)
    except Exception as Exp:
        print(Exp)
