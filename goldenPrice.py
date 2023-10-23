
from bs4 import BeautifulSoup
import requests

token = "B2lssd8Jwee3mumaTwLLMfUKHMKXCcAkc3FGTH7C1Gc" 
response = requests.get("https://rate.bot.com.tw/gold?Lang=zh-TW")
soup = BeautifulSoup(response.text, "html.parser")

priceCost = soup.find_all("td", {"class" : "text-right ebank"})[0].text.strip()[:4]
priceCost = float(priceCost)*3.75

priceRevenue = soup.find_all("td", {"class" : "text-right ebank"})[1].text.strip()[:4] #本行買進 == 我們賣出
priceRevenue = float(priceRevenue)*3.75

date = soup.find_all("span", {"id" : "h1_small_id"})[0].text.strip()

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/x-www-form-urlencoded"
}

# print(date_time)
# print ("\n我們賣出金價一錢為{}元\n\n我們買入金價一錢為{}元".format(priceRevenue, priceCost))

params = {"message": "\n{}\n\n我們賣出金價一錢為{}元\n\n我們買入金價一錢為{}元".format(date, priceRevenue, priceCost)}

r = requests.post("https://notify-api.line.me/api/notify",
    headers=headers, params=params)
print(r.status_code)  #200