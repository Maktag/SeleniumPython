from EnvSetup.BrowserSetup import Browser
import time


class VarsAll:
    try:
        brow = Browser()
        driver = brow.LaunchBrowser('firefox','https://in.yahoo.com/?p=us')
        time.sleep(2)
    except Exception as Exp:
        print(Exp)