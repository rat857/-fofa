import requests
from lxml import html
etree = html.etree

if __name__ == "__main__":
    url1 = "https://fofa.info/result?qbase64="
    qbase64 = ["IlRlcnJhTWFzdGVyIiAmJiBoZWFkZXI9IlRPUyIgJiYgY291bnRyeT0iQ04i","IlRlcnJhTWFzdGVyIiAmJiBoZWFkZXI9IlRPUyI%3D","IlRlcnJhTWFzdGVyIiAmJiBoZWFkZXI9IlRPUyIgJiYgY291bnRyeT0iVVMi","IlRlcnJhTWFzdGVyIiAmJiBoZWFkZXI9IlRPUyIgJiYgY291bnRyeT0iR0Ii","IlRlcnJhTWFzdGVyIiAmJiBoZWFkZXI9IlRPUyIgJiYgY291bnRyeT0iSVQi","IlRlcnJhTWFzdGVyIiAmJiBoZWFkZXI9IlRPUyIgJiYgY291bnRyeT0iRVMi"]
    headers = {
        'cookie': 'Hm_lvt_19b7bde5627f2f57f67dfb76eedcf989=1657086751,1657163347,1657181959,1657247652; Hm_lpvt_19b7bde5627f2f57f67dfb76eedcf989=1657247692; isUpgrade=; befor_router=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTI2NjI0LCJtaWQiOjEwMDA3NTM4OCwidXNlcm5hbWUiOiLoh6rmibAiLCJleHAiOjE2NTc0NTAxMjB9.QII78JiD2fb2qumJ_5n2WFW3NmJD2Rdnr8YelI1znp9qbsZYOYTsYJODDy_6kYNtkNA2LLNV32oQRGfO6S8fjw; user=%7B%22id%22%3A126624%2C%22mid%22%3A100075388%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22%E8%87%AA%E6%89%B0%22%2C%22nickname%22%3A%22%E8%87%AA%E6%89%B0%22%2C%22email%22%3A%222269264191%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FG26CVkQicUfCjzVVq26fotRrCO77eVibRChmayypibyXLzwe8xP4nIZibVerJK7SyEcaC1rU6kKwC7DPiaRkibE1bB1w%2F132%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FG26CVkQicUfCjzVVq26fotRrCO77eVibRChmayypibyXLzwe8xP4nIZibVerJK7SyEcaC1rU6kKwC7DPiaRkibE1bB1w%2F132%22%2C%22key%22%3A%222e594b67537fdcf1adfdf0fb6dbdae53%22%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22rank_level%22%3A0%2C%22company_name%22%3A%22%E8%87%AA%E6%89%B0%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A1657190920%7D',
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
                print(",,,")