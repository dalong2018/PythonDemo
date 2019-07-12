import requests


class MyRequests:

    def send_request(self, method, url, **kwargs):
        response = requests.request(method, url, **kwargs)
        return response

# 重定向的url


if __name__ == '__main__':
    method = "post"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Cookie": "username=test001; csrftoken=LiQZ1WkKLbAUi7Is8E672IewaTscxxUwwnpKYJche1mdBuq5dtV3QTEesxvlgxwc",
    }
    url = "https://test.risk.akulaku.com:9443/risk/rules/admin/login/?next=/risk/rules/admin/"
    data = {"username": "test001", "password": "QN22Tu79", "next": "/risk/rules/admin/", "csrfmiddlewaretoken":"LiQZ1WkKLbAUi7Is8E672IewaTscxxUwwnpKYJche1mdBuq5dtV3QTEesxvlgxwc"}

    result = MyRequests().send_request(method=method, url=url, data=data, headers=headers, verify=False, allow_redirects=False)
    data = requests.utils.dict_from_cookiejar(result.cookies)
    print(data)
    print(data['sessionid'])