import requests
import os
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
urls = ["https://www.dbmeinv.com/?pager_offset={}".format(str(i)) for i in range(1, 11)]
path = './美女图片/'


def get_girlphoto(url):
    try:
        data = requests.get(url + '1', headers=headers)
        selector = etree.HTML(data.text)
        girlphoto_urls = selector.xpath('//div/a/img/@src')

        for item in girlphoto_urls:
            if not os.path.exists(path):
                os.makedirs(path)
                print('path创建成功')
            data = requests.get(item, headers=headers)
            with open(path + item[-7:], 'wb') as f:
                f.write(data.content)
    except:
        print('Exception')


if __name__ == '__main__':
    for url in urls:
        get_girlphoto(url)
