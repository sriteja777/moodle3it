import all
import requests
import  bs4
login_page = all.login()
index = 'https://mess.iiit.ac.in/mess/web/index.php'
home = 'https://mess.iiit.ac.in/mess/web/student_home.php'
pg = requests.get(index, cookies=login_page.cookies)
soup = bs4.BeautifulSoup(pg.text, 'lxml')
k=1
for i in soup.find('table').find_all('td')[7:13]:
    if k%2:
        print(i.text, ':', end='')
    else:
        print(i.text)
    k = k + 1