import unittest
import requests


class GetEventListTest(unittest.TestCase):
    ''' 发送底部库列表查询请求信息'''

    def setUp(self):
        self.base_url = 'https://pro.lceda.cn/api/devices/search'
        # 账号信息
        self.auth_user = ('username', 'password')

    def test_search_library(self):
        ''' post 请求 '''
        r = requests.post(
            self.base_url,
            auth=self.auth_user,
            # 请求体
            params={
                'uid': '54c6d125f88940aca46b58a066f9754e',
                'wd': 'diamon',
                'pageSize': '50',
                'returnListStyle': 'classifyarr',
                'page': '1'
            })
        result = r.json()
        print(result)
