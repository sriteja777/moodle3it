import bs4
import requests

from src import all

login_page = all.login()
index = 'https://mess.iiit.ac.in/mess/web/index.php'
home = 'https://mess.iiit.ac.in/mess/web/student_home.php'
pg = requests.get(index, cookies=login_page.cookies)
soup = bs4.BeautifulSoup(pg.text, 'lxml')
counter = 1
for i in soup.find('table').find_all('td')[7:13]:
    if counter % 2:
        print(i.text, ':', end='')
    else:
        print(i.text)
    counter = counter + 1
