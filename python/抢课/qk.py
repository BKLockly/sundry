import requests
import http.cookiejar as cookielib
import re
import time
import os.path
from PIL import Image
import hashlib

headers = {
    "Host": "172.18.2.43",
    "Referer": "http://172.18.2.43/jwweb/_data/login_new.aspx",
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate',
    'Content_Type':'application/x-www-form-urlencoded',
    'Cookie': 'security_session_verify=d124ee60bc6eb86645324a45f7fcfbd2; ASP.NET_SessionId=suojaqj40jvuypezb0ic1s45',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
}


session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True) # 如果已经有 cookie信息的话 直接用于登录
except:
    print("[-] Cookie 未能加载")
    

#userid = input("userid:\n")
#password = input("password:\n")
userid = '2141302107'
password = '2003jackojbk520'

def qg_fgfg(validateCode):              # Encryption authentication code 
    code = validateCode.upper()
    m2 = hashlib.md5()
    m2.update(code.encode(encoding='gb2312'))
    s4 = m2.hexdigest()
    s5 = s4[0:30].upper() + '10481'
    m3 = hashlib.md5()
    m3.update(s5.encode(encoding='gb2312'))
    s6 = m3.hexdigest()
    s7 = s6[0:30].upper()
    return s7


def qg_dsds(userid,password):   # Encrypt the user name and password 
    m = hashlib.md5()
    m.update(password.encode(encoding='gb2312'))
    psw = m.hexdigest()
    s1 = userid + psw[0:30].upper() + '10481'
    m1 = hashlib.md5()
    m1.update(s1.encode(encoding='gb2312'))
    s2 = m1.hexdigest()
    s3 = s2[0:30].upper()
    return s3

def get_captcha():
    captcha_url = 'http://172.18.2.43/jwweb/sys/ValidateCode.aspx'
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    im = Image.open('captcha.jpg')
    print("[+] 请关闭图片")
    im.show()
    im.close()
    
    captcha = input("[*] 输入验证码：\n>")
    return captcha

captcha = get_captcha()
postdata = {
            '_VIEWSTATE': 'dDwtNjMyNzQ3NTkxO3Q8O2w8aTwwPjtpPDE+O2k8Mj47PjtsPHQ8cDxsPFRleHQ7PjtsPOmCtemYs+WtpumZojs+Pjs7Pjt0PHA8bDxUZXh0Oz47bDxcPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiXD4KZnVuY3Rpb24gQ2hrVmFsdWUoKXsKIHZhciB2VT0kKCdVSUQnKS5pbm5lckhUTUxcOwogdlU9dlUuc3Vic3RyaW5nKDAsMSkrdlUuc3Vic3RyaW5nKDIsMylcOwogdmFyIHZjRmxhZyA9ICJZRVMiXDsgaWYgKCQoJ3R4dF9hc21jZGVmc2Rkc2QnKS52YWx1ZT09JycpewogYWxlcnQoJ+mhu+W9leWFpScrdlUrJ++8gScpXDskKCd0eHRfYXNtY2RlZnNkZHNkJykuZm9jdXMoKVw7cmV0dXJuIGZhbHNlXDsKfQogZWxzZSBpZiAoJCgndHh0X3Bld2Vyd2Vkc2Rmc2RmZicpLnZhbHVlPT0nJyl7CiBhbGVydCgn6aG75b2V5YWl5a+G56CB77yBJylcOyQoJ3R4dF9wZXdlcndlZHNkZnNkZmYnKS5mb2N1cygpXDtyZXR1cm4gZmFsc2VcOwp9CiBlbHNlIGlmICgkKCd0eHRfc2RlcnRmZ3NhZHNjeGNhZHNhZHMnKS52YWx1ZT09JycgJiYgdmNGbGFnID09ICJZRVMiKXsKIGFsZXJ0KCfpobvlvZXlhaXpqozor4HnoIHvvIEnKVw7JCgndHh0X3NkZXJ0ZmdzYWRzY3hjYWRzYWRzJykuZm9jdXMoKVw7cmV0dXJuIGZhbHNlXDsKfQogZWxzZSB7ICQoJ2RpdkxvZ05vdGUnKS5pbm5lckhUTUw9J1w8Zm9udCBjb2xvcj0icmVkIlw+5q2j5Zyo6YCa6L+H6Lqr5Lu96aqM6K+BLi4u6K+356iN5YCZIVw8L2ZvbnRcPidcOwogICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidHh0X3Bld2Vyd2Vkc2Rmc2RmZiIpLnZhbHVlID0gJydcOwogZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInR4dF9zZGVydGZnc2Fkc2N4Y2Fkc2FkcyIpLnZhbHVlID0gJydcOyAKIHJldHVybiB0cnVlXDt9CiB9CmZ1bmN0aW9uIFNlbFR5cGUob2JqKXsKIHZhciBzPW9iai5vcHRpb25zW29iai5zZWxlY3RlZEluZGV4XS5nZXRBdHRyaWJ1dGUoJ3VzcklEJylcOwogJCgnVUlEJykuaW5uZXJIVE1MPXNcOwogc2VsVHllTmFtZSgpXDsKIGlmKG9iai52YWx1ZT09IlNUVSIpIHsKICAgZG9jdW1lbnQuYWxsLmJ0bkdldFN0dVB3ZC5zdHlsZS5kaXNwbGF5PScnXDsKICAgZG9jdW1lbnQuYWxsLmJ0blJlc2V0LnN0eWxlLmRpc3BsYXk9J25vbmUnXDsKICB9CiBlbHNlIHsKICAgIGRvY3VtZW50LmFsbC5idG5SZXNldC5zdHlsZS5kaXNwbGF5PScnXDsKICAgIGRvY3VtZW50LmFsbC5idG5HZXRTdHVQd2Quc3R5bGUuZGlzcGxheT0nbm9uZSdcOwogIH19CmZ1bmN0aW9uIG9wZW5XaW5Mb2codGhlVVJMLHcsaCl7CnZhciBUZm9ybSxyZXRTdHJcOwpldmFsKCJUZm9ybT0nd2lkdGg9Iit3KyIsaGVpZ2h0PSIraCsiLHNjcm9sbGJhcnM9bm8scmVzaXphYmxlPW5vJyIpXDsKcG9wPXdpbmRvdy5vcGVuKHRoZVVSTCwnd2luS1BUJyxUZm9ybSlcOyAvL3BvcC5tb3ZlVG8oMCw3NSlcOwpldmFsKCJUZm9ybT0nZGlhbG9nV2lkdGg6Iit3KyJweFw7ZGlhbG9nSGVpZ2h0OiIraCsicHhcO3N0YXR1czpub1w7c2Nyb2xsYmFycz1ub1w7aGVscDpubyciKVw7CnBvcC5tb3ZlVG8oKHNjcmVlbi53aWR0aC13KS8yLChzY3JlZW4uaGVpZ2h0LWgpLzIpXDtpZih0eXBlb2YocmV0U3RyKSE9J3VuZGVmaW5lZCcpIGFsZXJ0KHJldFN0cilcOwp9CmZ1bmN0aW9uIHNob3dMYXkoZGl2SWQpewp2YXIgb2JqRGl2ID0gZXZhbChkaXZJZClcOwppZiAob2JqRGl2LnN0eWxlLmRpc3BsYXk9PSJub25lIikKe29iakRpdi5zdHlsZS5kaXNwbGF5PSIiXDt9CmVsc2V7b2JqRGl2LnN0eWxlLmRpc3BsYXk9Im5vbmUiXDt9Cn0KZnVuY3Rpb24gc2VsVHllTmFtZSgpewogICQoJ3R5cGVOYW1lJykudmFsdWU9JE4oJ1NlbF9UeXBlJylbMF0ub3B0aW9uc1skTignU2VsX1R5cGUnKVswXS5zZWxlY3RlZEluZGV4XS50ZXh0XDsKfQp3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7Cgl2YXIgc1BDPU1TSUU/d2luZG93Lm5hdmlnYXRvci51c2VyQWdlbnQrd2luZG93Lm5hdmlnYXRvci5jcHVDbGFzcyt3aW5kb3cubmF2aWdhdG9yLmFwcE1pbm9yVmVyc2lvbisnIFNOOk5VTEwnOndpbmRvdy5uYXZpZ2F0b3IudXNlckFnZW50K3dpbmRvdy5uYXZpZ2F0b3Iub3NjcHUrd2luZG93Lm5hdmlnYXRvci5hcHBWZXJzaW9uKycgU046TlVMTCdcOwp0cnl7JCgncGNJbmZvJykudmFsdWU9c1BDXDt9Y2F0Y2goZXJyKXt9CnRyeXskKCd0eHRfYXNtY2RlZnNkZHNkJykuZm9jdXMoKVw7fWNhdGNoKGVycil7fQp0cnl7JCgndHlwZU5hbWUnKS52YWx1ZT0kTignU2VsX1R5cGUnKVswXS5vcHRpb25zWyROKCdTZWxfVHlwZScpWzBdLnNlbGVjdGVkSW5kZXhdLnRleHRcO31jYXRjaChlcnIpe30KfQpmdW5jdGlvbiBvcGVuV2luRGlhbG9nKHVybCxzY3IsdyxoKQp7CnZhciBUZm9ybVw7CmV2YWwoIlRmb3JtPSdkaWFsb2dXaWR0aDoiK3crInB4XDtkaWFsb2dIZWlnaHQ6IitoKyJweFw7c3RhdHVzOiIrc2NyKyJcO3Njcm9sbGJhcnM9bm9cO2hlbHA6bm8nIilcOwp3aW5kb3cuc2hvd01vZGFsRGlhbG9nKHVybCwxLFRmb3JtKVw7Cn0KZnVuY3Rpb24gb3Blbldpbih0aGVVUkwpewp2YXIgVGZvcm0sdyxoXDsKdHJ5ewoJdz13aW5kb3cuc2NyZWVuLndpZHRoLTEwXDsKfWNhdGNoKGUpe30KdHJ5ewpoPXdpbmRvdy5zY3JlZW4uaGVpZ2h0LTMwXDsKfWNhdGNoKGUpe30KdHJ5e2V2YWwoIlRmb3JtPSd3aWR0aD0iK3crIixoZWlnaHQ9IitoKyIsc2Nyb2xsYmFycz1ubyxzdGF0dXM9bm8scmVzaXphYmxlPXllcyciKVw7CnBvcD1wYXJlbnQud2luZG93Lm9wZW4odGhlVVJMLCcnLFRmb3JtKVw7CnBvcC5tb3ZlVG8oMCwwKVw7CnBhcmVudC5vcGVuZXI9bnVsbFw7CnBhcmVudC5jbG9zZSgpXDt9Y2F0Y2goZSl7fQp9CmZ1bmN0aW9uIGNoYW5nZVZhbGlkYXRlQ29kZShPYmopewp2YXIgZHQgPSBuZXcgRGF0ZSgpXDsKT2JqLnNyYz0iLi4vc3lzL1ZhbGlkYXRlQ29kZS5hc3B4P3Q9IitkdC5nZXRNaWxsaXNlY29uZHMoKVw7Cn0KZnVuY3Rpb24gY2hrcHdkKG9iaikgeyAgaWYob2JqLnZhbHVlIT0nJykgIHsgICAgdmFyIHM9bWQ1KGRvY3VtZW50LmFsbC50eHRfYXNtY2RlZnNkZHNkLnZhbHVlK21kNShvYmoudmFsdWUpLnN1YnN0cmluZygwLDMwKS50b1VwcGVyQ2FzZSgpKycxMDU0NycpLnN1YnN0cmluZygwLDMwKS50b1VwcGVyQ2FzZSgpXDsgICBkb2N1bWVudC5hbGwuZHNkc2RzZHNkeGN4ZGZnZmcudmFsdWU9c1w7fSBlbHNlIHsgZG9jdW1lbnQuYWxsLmRzZHNkc2RzZHhjeGRmZ2ZnLnZhbHVlPW9iai52YWx1ZVw7fWNoa0x4c3RyKG9iai52YWx1ZSlcOyB9ICBmdW5jdGlvbiBjaGt5em0ob2JqKSB7ICBpZihvYmoudmFsdWUhPScnKSB7ICAgdmFyIHM9bWQ1KG1kNShvYmoudmFsdWUudG9VcHBlckNhc2UoKSkuc3Vic3RyaW5nKDAsMzApLnRvVXBwZXJDYXNlKCkrJzEwNTQ3Jykuc3Vic3RyaW5nKDAsMzApLnRvVXBwZXJDYXNlKClcOyAgIGRvY3VtZW50LmFsbC5mZ2ZnZ2ZkZ3R5dXV5eXV1Y2tqZy52YWx1ZT1zXDt9IGVsc2UgeyAgICBkb2N1bWVudC5hbGwuZmdmZ2dmZGd0eXV1eXl1dWNramcudmFsdWU9b2JqLnZhbHVlLnRvVXBwZXJDYXNlKClcO319IGZ1bmN0aW9uIGNoa0x4c3RyKHN0cikgCiB7CiBpZiAoc3RyIT0nJykgeyB2YXIgYXJyID0gc3RyLnNwbGl0KCcnKVw7CmZvciAodmFyIGkgPSAxXDsgaSBcPCBhcnIubGVuZ3RoLTFcOyBpKyspIHsKICAgdmFyIGZpcnN0SW5kZXggPSBhcnJbaS0xXS5jaGFyQ29kZUF0KClcOwogICB2YXIgc2Vjb25kSW5kZXggPSBhcnJbaV0uY2hhckNvZGVBdCgpXDsKICAgdmFyIHRoaXJkSW5kZXggPSBhcnJbaSsxXS5jaGFyQ29kZUF0KClcOwogICB0aGlyZEluZGV4IC0gc2Vjb25kSW5kZXggPT0gMVw7CiAgICBzZWNvbmRJbmRleCAtIGZpcnN0SW5kZXg9PTFcOwogICBpZigoKHRoaXJkSW5kZXggLSBzZWNvbmRJbmRleCA9PSAxKSYmKHNlY29uZEluZGV4IC0gZmlyc3RJbmRleD09MSkgKSB8fCAodGhpcmRJbmRleD09c2Vjb25kSW5kZXggJiYgc2Vjb25kSW5kZXg9PWZpcnN0SW5kZXgpKXsKICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3R4dF9tbV9seHBkJykudmFsdWU9JzEnXDsgCiAgIH0KIH0KIH0KfQoKXDwvc2NyaXB0XD47Pj47Oz47dDw7bDxpPDE+Oz47bDx0PDtsPGk8MD47aTwyPjs+O2w8dDxwPGw8VGV4dDs+O2w8XDxvcHRpb24gdmFsdWU9J1NUVScgdXNySUQ9J+WtpuOAgOWPtydcPuWtpueUn1w8L29wdGlvblw+Clw8b3B0aW9uIHZhbHVlPSdURUEnIHVzcklEPSflt6XjgIDlj7cnXD7mlZnluIjmlZnovoXkurrlkZhcPC9vcHRpb25cPgpcPG9wdGlvbiB2YWx1ZT0nU1lTJyB1c3JJRD0n5biQ44CA5Y+3J1w+566h55CG5Lq65ZGYXDwvb3B0aW9uXD4KXDxvcHRpb24gdmFsdWU9J0FETScgdXNySUQ9J+W4kOOAgOWPtydcPumXqOaIt+e7tOaKpOWRmFw8L29wdGlvblw+Cjs+Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmqjOivgeeggemUmeivr++8gVw8YnJcPueZu+W9leWksei0pe+8gTs+Pjs+Ozs+Oz4+Oz4+Oz4+Oz5UuYMhrRSRkwmeIO3fOlM29G50gA==',
            '__VIEWSTATEGENERATOR' :'A23C4EFA',
            'pcInfo':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50undefined5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50 SN:NULL',
            'typeName':'%D1%A7%C9%FA',     
            'fgfggfdgtyuuyyuuckjg':qg_fgfg(captcha),
            'dsdsdsdsdxcxdfgfg':qg_dsds(userid,password),
            'Sel_Type':'STU',
            'txt_asmcdefsddsd':userid,
            'txt_pewerwedsdfsdff':password,
            'txt_sdertfgsadscxcadsads':captcha,
           }
#def login():
post_url ='http://172.18.2.43/jwweb/_data/login_new.aspx'
login_page = session.post(post_url, data=postdata, headers=headers)
session.cookies.save()
print("cookie 已保存")