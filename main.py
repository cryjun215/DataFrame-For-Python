import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


URL = "https://www.kma.go.kr/weather/observation/currentweather.jsp"

res = requests.get(URL)
soup = bs(res.content, 'html.parser')
table = soup.find('table', {'class' : 'table_develop3'})

data = []
for tr in table.find_all('tr'):
        tds = list(tr.find_all('td'))
        for td in tds:
                if td.find('a'):
                        point = td.find('a').text
                        temperature = tds[5].text
                        humidity = tds[9].text
                        data.append([point, temperature, humidity])

with open ('weather.csv','w', encoding='UTF-8') as file:
        file.write('point, temperature, humidity\n')
        for i in data:
                file.write('{0}, {1}, {2}\n'.format(i[0], i[1], i[2]))
                
df = pd.read_csv('weather.csv', index_col='point', encoding='UTF-8')

font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

ax = df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온', '습도'], fontsize=12)

plt.show()