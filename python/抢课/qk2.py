# from DrissionPage.easy_set import set_paths
import sys
sys.path.append(r"C:\Users\ONEFOX\AppData\Local\Programs\Python\Python310\lib\site-packages\DrissionPage")
from DrissionPage import ChromiumPage

# jls_extract_var = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
# set_paths(browser_path=jls_extract_var)


page = ChromiumPage()
page.get('https://www.baidu.com')