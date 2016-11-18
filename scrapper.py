import requests, bs4
res = requests.get('http://www.accuweather.com/en/us/melbourne-fl/32901/weather-forecast/332282')
res.raise_for_status()
playFile = open('web.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
playFile.close()
soup = bs4.BeautifulSoup(res.text, "html.parser")
temp = soup.select('.large-temp')
disp = soup.select('.cond')
print("the tempature outside is", temp[0].getText(), 'and it is', disp[0].getText(), 'outside')
