import requests

login_url = "https://idp.nchu.edu.tw/nidp/idff/sso?sid=1&sid=1"
portal_url1 = "https://portal.nchu.edu.tw/portal/"
j_security_url = "https://portal.nchu.edu.tw/portal/j_spring_security_check"

s = requests.session()
res = s.get(portal_url1)
JSESSIONID = res.cookies['JSESSIONID']
headers = {
    "Host" : "portal.nchu.edu.tw",
    "Origin" : "https://portal.nchu.edu.tw",
    "Referer" : "https://portal.nchu.edu.tw/portal/login",
    "Cookie" : "JSESSIONID={};NchuSSOLang=zh_TW;".format(JSESSIONID),
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
data1 = {"Ecom_User_ID": "學號", 
        "Ecom_Password": "密碼",
        "option": "credential",
        "target": "https://portal.nchu.edu.tw/portal"
}
data2 = {"j_username":"學號", 
        "j_password": "密碼"
}
res = s.post(login_url, headers=headers, data=data1)
res = s.post(j_security_url, headers=headers, data=data2)
# res = s.get(portal_url1)
print(res.text)