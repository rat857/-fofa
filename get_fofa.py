import requests
from lxml import html
etree = html.etree

if __name__ == "__main__":
    url1 = "https://fofa.info/result?qbase64="
    qbase64 = [""]
    headers = {
        'cookie': '',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    for bs in range(len(qbase64)):
        qbase = qbase64[bs]
        for pa in range(1, 4, 1):
            pa1 = str(pa)
            page = "&page=" + pa1
            url = url1 + qbase + page + "&page_size=20"
            response = requests.get(url=url,headers=headers)
            page_text = response.text
            # print(page_text)
            tree =etree.HTML(page_text)
            try:
                ip = tree.xpath('//span[@class="aSpan"]/a/@href')
                print(ip)
            except IndexError:
                print("erro")
