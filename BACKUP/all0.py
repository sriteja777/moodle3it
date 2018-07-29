import requests
import bs4
import re
import os
from connection import *

dashboard_url = 'https://moodle.iiit.ac.in/my/'


class ObjectSetup(object):
    pass


page = ObjectSetup()
soup = ObjectSetup()
files = ObjectSetup()
names = ObjectSetup()


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True, cookies=page.login.cookies)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def create_tables(courses_list):
    c, conn = connection()
    for course in courses_list:
        c.execute("create table if not exists {0} (filename varchar(100), link varchar(100))".format(course))
    conn.commit()
    return




def login():
    url = 'https://login.iiit.ac.in/cas/login'
    execution_value = 'd774bde4-d1d9-4523-a19a-b69a200682b8_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVEVsWlRXcFNNVWhMWjI1S1NXdEJhMlJJWjJwcUwyY3JVM2xDTjJvd1MzQkdWMU4zY0VWSWRGTXJUMkozUWpaWGVtNHlTRGxYZVVScVdrOU1OMlpPSzFkaWNGSnJkbmRyU0hOVlpHdHJLMHd2TWpsdlNYSTRXSEpCVDNwd2J6TlZlV05xVlVsdGVubFNlR2xxYVRWTFlrRjNUakJuTjBaTE5sVk1jVkZ6ZURCalVUSlNUV0pPZVhCemNGTnJZMWc0TlROa1FVRndhMDA1T1VrMWFETk1RWE5hWlVSMlRHcHdaV1ZHVjNkcU1uQnhUMnhCTDJOU1RTOURVM0J0YmtzMFRYUXlTR3Q2TkVkNVlXRnhaMU5NWkVsNVQxWnpMMEZVZDFGMVZYTjBlRGxrTUZWclpuVlBWV3g1ZUVSM1kyZHBibEpEV1U5b2IwMTNWV3RvVTAxcU1rNHZiVTVwVmk5VFNtcDRZemMyUjBkS2NsTnJVbTlRTWpWdGJEWnlTM00zSzFSWU1YY3djelYyYm1KbmIwMWpVWFZLWTBSa1JEbEpaRFp4VDNGWlowWjZNREJsWVdwb1VVOU5jMmhXVjNoU01IRllTRkZyWWxSMFNGSjFRMGxWTVhKTlVFbEpTazAzYkZWTmRHeFBXRkpPTVUwMlNtTkRjVU5GV2pndlFrbElNVVF3ZVVWaGRtTlhVRGt6TVdoTlRWSkNjMVJRUXpKcVJHeFVjazFOVUdwb1FXRTRlakV4TW1wckwyazJVVzF0WW5BMFREUkNXV0puVkZOTlltdHJXbFZOU1ZSMk9UTkdSa2g2ZUc5MlNtTk9RV3hOYzNWMVIzZHZibFJFV0hjNFJXMTBjVXBTTXpCak9GZzFabmhNVkhGM1ltRXdZVkJ3ZDJKQ1UzWTRiMHRXVkhoTGREWktkMVZKYVhoWFR6Vlljek5vY210MU1GQmtaRU50WVhJdk0weHpiRmRJYUU4elJFUnhUMW8yTkZKQlFXOUdjV1JMTlhKNGFIa3lTWGxhYjBGU2JVUm5TbE5ZUzFOT2JXNVFZM0ZWVEc5alNGbE9aa0ZNUTJkaVpEbE9WbFZ4Y1M4ek9UZGtlR1ZGTnpaR2JWSm1Na3RqWVdsUk5uTlhaREpMSzJvNE5Xa3laa2swYUU1bU1WTjZaekV3YkVoRVZFbHhMMjFGV0VGVk1GRkplRUpJY1RCU1RtbzFNbFJpWlZoeVEzSlNlRTFtZUVwV1MzWjFXbGh0Ym1KSWJsTjBUMEpzVlRBNFFqTjFUM04yU1hkSk1GRnhXSFZMUVdKUGIwaHZaekJ6ZEdSWVlVbDNWa3BSTTBkU01YQjBhelZVYWxwNk9HOVlkbEJsTmk5a2NtZDFjalYyWkRSbGVXNDRTMDFpTmtWQkt6Um9VM1JPWTBjMksyUmtXRkprYldFeFZHOUhNbXd3U0RZMVZHZG1jMUk1YjNsNU1EVkhSSGRzY0RScFpEQllhVGdyTkROUFNXdG1SWEZCWjBseFZHVkJkVlo1UkZkME0zQTBlVEF3V1hjM1YwWm9UMGhrV1dwblZGUm1SbWhoUkdWblMwVktWVXR6VlcxU1ZUWjNaVUZsVVVFMlkzZFNNeXRLTTFsNGVWVjNRVTFhT0V0c2NsZDNaVkpsVkdkeU5GSm9VQzltUXpoRlBRLk5wTkVMcndkNmtPRmo0T0FWVHF1M1pZUWdic0VGWWE4SEg2eDBsYzgtRzNyVHFCX2dzeFh2cmtLWW5NNzFRQmlIUDJlWkw2SFIxdjlGN0h2TVRfdlJR'
    pg = requests.post(url, data={'username': 'sriteja.sugoor@students.iiit.ac.in', 'password': 'Ajet@72sri',
                                  'execution': execution_value, '_eventId': 'submit'})
    return pg


setattr(page, 'login', login())
print(page.login.cookies, page.login.text)
print("Logged in")

setattr(page, 'dashboard', requests.get('https://moodle.iiit.ac.in/my/', cookies=page.login.cookies))
print(page.dashboard.text)
print("Accessed to Moodle")
setattr(soup, 'dashboard', bs4.BeautifulSoup(page.dashboard.text, 'lxml'))
courses_html = soup.dashboard.select('.course_title')
courses_list = []
courses_links = []
for i in courses_html:
    courses_list.append(i.text.replace(' ', '_').replace('-', ''))
    courses_links.append(i.find('a').get('href'))
print(courses_list, courses_links)
create_tables(courses_list)


setattr(page, 'temp', '')
setattr(soup, 'temp', '')
for course, link in zip(courses_list, courses_links):
    page.temp = requests.get(link, cookies=page.login.cookies)
    setattr(page, course, page.temp)
    soup.temp = bs4.BeautifulSoup(getattr(page, course).text, 'lxml')
    setattr(soup, course, soup.temp)
    print(course)
    course_topics = getattr(soup, course).select('.accesshide')
    setattr(files, course, [])
    setattr(names, course, [])
    for i in course_topics:
        if i.text == " File":
            getattr(files, course).append(i.find_parent('a').get('href'))
            getattr(names, course).append(i.find_parent('span').find(text=True))
            # print(i.find_parent('span').find(text=True), i.find_parent('a').get('href'))
    # print()
    print(getattr(files, course), getattr(names, course))
    print()
print(dir(files))
# try 1

# k = files.Basic_Electronic_Circuits
# cd = requests.get(k, cookies=page.login.cookies)
# make directories
for course in courses_list:
    if not os.path.isdir(course):
        os.mkdir(course)
print("made directories")
course = 'Mathematics_II'
os.chdir(os.getcwd() + '/' + course)
c,conn = dict_connection()
for link, name in zip(getattr(files, course), getattr(names, course)):
    x = c.execute("select * from {0} where link='{1}'".format(course, link))
    if not int(x) > 0:
        if is_downloadable(link):
            print(filename + ' downloading...')
            file = requests.get(link, cookies=page.login.cookies)
            filename = get_filename_from_cd(file.headers.get('content-disposition'))
            print(filename, link, name)
            open(filename, 'wb').write(file.content)
            c.execute("insert into {0} (filename, link) values ('{1}','{2}')".format(course, filename, link))
            conn.commit()
            print(filename + ' downloaded')
        else:
            print(name + ' is not downloadable')
    else:
        print(name + ' is already downloaded')
conn.commit()
c.close()