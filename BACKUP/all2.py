import requests
import bs4
import re
import os
from connection import *
import warnings
from subprocess import call
import logging
import time
from humanize import naturalsize
import tkinter
from getch import _GetchUnix
import threading
import signal

dashboard_url = 'https://moodle.iiit.ac.in/my/'
chunk_size = 100000
getch = _GetchUnix()
resume = threading.Event()
cancel = threading.Event()
kb_interrupt = threading.Event()


class ObjectSetup(object):
    pass


page = ObjectSetup()
soup = ObjectSetup()
files = ObjectSetup()
names = ObjectSetup()
courses = ObjectSetup()


# def is_downloadable(url):
#     """
#     Does the url contain a downloadable resource
#     """
#     global session
#     h = session.head(url, allow_redirects=True)
#     header = h.headers
#     content_type = header.get('content-type')
#     if 'text' in content_type.lower():
#         return False
#     if 'html' in content_type.lower():
#         return False
#     return True


def is_downloadable(content_type):
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
    name = re.findall('filename=(.+)', cd)
    if len(name) == 0:
        return None
    return name[0].replace('"', '')


def create_tables(courses_list):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            c, conn = connection()
            for course in courses_list:
                c.execute("create table if not exists {0} (filename varchar(100), link varchar(100))".format(course))
            conn.commit()
    except Exception as e:
        print("Looks like there is a problem in creating tables and the problem is {}.".format(e))
        raise SystemExit(6)
    return


def make_directories(courses_list):
    for course in courses_list:
        if not os.path.isdir(course):
            os.mkdir(course)
            print('Made directory', course)
    return


def set_login_data():
    url = 'https://login.iiit.ac.in/cas/login'
    execution_value = 'd774bde4-d1d9-4523-a19a-b69a200682b8_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVEVsWlRXcFNNVWhMWjI1S1NXdEJhM' \
                      'lJJWjJwcUwyY3JVM2xDTjJvd1MzQkdWMU4zY0VWSWRGTXJUMkozUWpaWGVtNHlTRGxYZVVScVdrOU1OMlpPSzFkaWNGSnJ' \
                      'kbmRyU0hOVlpHdHJLMHd2TWpsdlNYSTRXSEpCVDNwd2J6TlZlV05xVlVsdGVubFNlR2xxYVRWTFlrRjNUakJuTjBaTE5sV' \
                      'k1jVkZ6ZURCalVUSlNUV0pPZVhCemNGTnJZMWc0TlROa1FVRndhMDA1T1VrMWFETk1RWE5hWlVSMlRHcHdaV1ZHVjNkcU1' \
                      'uQnhUMnhCTDJOU1RTOURVM0J0YmtzMFRYUXlTR3Q2TkVkNVlXRnhaMU5NWkVsNVQxWnpMMEZVZDFGMVZYTjBlRGxrTUZWc' \
                      'lpuVlBWV3g1ZUVSM1kyZHBibEpEV1U5b2IwMTNWV3RvVTAxcU1rNHZiVTVwVmk5VFNtcDRZemMyUjBkS2NsTnJVbTlRTWp' \
                      'WdGJEWnlTM00zSzFSWU1YY3djelYyYm1KbmIwMWpVWFZLWTBSa1JEbEpaRFp4VDNGWlowWjZNREJsWVdwb1VVOU5jMmhXV' \
                      'jNoU01IRllTRkZyWWxSMFNGSjFRMGxWTVhKTlVFbEpTazAzYkZWTmRHeFBXRkpPTVUwMlNtTkRjVU5GV2pndlFrbElNVVF' \
                      '3ZVVWaGRtTlhVRGt6TVdoTlRWSkNjMVJRUXpKcVJHeFVjazFOVUdwb1FXRTRlakV4TW1wckwyazJVVzF0WW5BMFREUkNXV' \
                      '0puVkZOTlltdHJXbFZOU1ZSMk9UTkdSa2g2ZUc5MlNtTk9RV3hOYzNWMVIzZHZibFJFV0hjNFJXMTBjVXBTTXpCak9GZzF' \
                      'abmhNVkhGM1ltRXdZVkJ3ZDJKQ1UzWTRiMHRXVkhoTGREWktkMVZKYVhoWFR6Vlljek5vY210MU1GQmtaRU50WVhJdk0we' \
                      'HpiRmRJYUU4elJFUnhUMW8yTkZKQlFXOUdjV1JMTlhKNGFIa3lTWGxhYjBGU2JVUm5TbE5ZUzFOT2JXNVFZM0ZWVEc5alN' \
                      'GbE9aa0ZNUTJkaVpEbE9WbFZ4Y1M4ek9UZGtlR1ZGTnpaR2JWSm1Na3RqWVdsUk5uTlhaREpMSzJvNE5Xa3laa2swYUU1b' \
                      'U1WTjZaekV3YkVoRVZFbHhMMjFGV0VGVk1GRkplRUpJY1RCU1RtbzFNbFJpWlZoeVEzSlNlRTFtZUVwV1MzWjFXbGh0Ym1' \
                      'KSWJsTjBUMEpzVlRBNFFqTjFUM04yU1hkSk1GRnhXSFZMUVdKUGIwaHZaekJ6ZEdSWVlVbDNWa3BSTTBkU01YQjBhelZVY' \
                      'WxwNk9HOVlkbEJsTmk5a2NtZDFjalYyWkRSbGVXNDRTMDFpTmtWQkt6Um9VM1JPWTBjMksyUmtXRkprYldFeFZHOUhNbXd' \
                      '3U0RZMVZHZG1jMUk1YjNsNU1EVkhSSGRzY0RScFpEQllhVGdyTkROUFNXdG1SWEZCWjBseFZHVkJkVlo1UkZkME0zQTBlV' \
                      'EF3V1hjM1YwWm9UMGhrV1dwblZGUm1SbWhoUkdWblMwVktWVXR6VlcxU1ZUWjNaVUZsVVVFMlkzZFNNeXRLTTFsNGVWVjN' \
                      'RVTFhT0V0c2NsZDNaVkpsVkdkeU5GSm9VQzltUXpoRlBRLk5wTkVMcndkNmtPRmo0T0FWVHF1M1pZUWdic0VGWWE4SEg2e' \
                      'DBsYzgtRzNyVHFCX2dzeFh2cmtLWW5NNzFRQmlIUDJlWkw2SFIxdjlGN0h2TVRfdlJR'
    username = 'sriteja.sugoor@students.iiit.ac.in'
    password = 'Ajet@72sri'
    return url, execution_value, username, password


def advanced_login():
    call(['/bin/bash', '-i', '-c', 'iiit -d'])
    pg = login()
    call(['/bin/bash', '-i', '-c', 'iiit -c'])
    return pg


def connect_to_moodle():
    global page
    try:
        setattr(page, 'dashboard', session.get('https://moodle.iiit.ac.in/my/'))
        print('Accessed to Moodle')
    except requests.ConnectionError:
        print("Looks like you are not connected to iiit vpn, run iiit -c command to connect to iiit vpn")
        raise SystemExit(4)
    return


def login():
    global session
    url, execution_value, username, password = set_login_data()
    success_text = 'You, sriteja.sugoor@students.iiit.ac.in, have successfully' \
                   ' logged into the Central Authentication Service.'
    try:
        pg = session.post(url,
                          data={'username': username, 'password': password,
                                'execution': execution_value, '_eventId': 'submit'},
                          timeout=10)
    except requests.ConnectionError:
        print("I think you are not connected to internet.")
        raise SystemExit(1)
    except requests.ReadTimeout:
        logging.warning("Looks like CAS is down as it does not support single Sign-Out, try logging out of all other "
                        "applications or increase the timeout. But as of now I am trying some advanced method. If you "
                        "see this message again and again then stop this program and try after some time.")
        return advanced_login()

    sp = bs4.BeautifulSoup(pg.text, 'lxml')
    setattr(soup, 'login', sp)
    if sp.find('p').text == success_text:
        print('Login Successful')
    else:
        print('Login Failure. Try checking credentials. Even if the problem persists try after some time.')
        raise SystemExit(3)
    return pg


def get_courses():
    global courses
    for i in courses.html:
        courses.list.append(i.text.replace(' ', '_').replace('-', ''))
        courses.links.append(i.find('a').get('href'))

    if not courses.list or not courses.html:
        print("Looks like there is some problem in getting moodle dashboard page, try after some time")
        raise SystemExit(5)
    else:
        print("You are registered to the following courses for this sem")
        [print(s_no, ') ', course, '(', link, ')', sep='') for course, s_no, link in zip(courses.list,
                                                                                         range(1, len(courses.list)+1),
                                                                                         courses.links)]
    return


def get_links(courses_list, courses_links):
    global soup, page, files, names
    print("Now getting the links of topics in the courses...")
    for course, link in zip(courses_list, courses_links):
        page.temp = session.get(link)
        setattr(page, course, page.temp)
        soup.temp = bs4.BeautifulSoup(getattr(page, course).text, 'lxml')
        setattr(soup, course, soup.temp)
        print(course, end='...')
        topics = getattr(soup, course).select('.accesshide')
        setattr(files, course, [])
        setattr(names, course, [])
        for i in topics:
            if i.text == " File":
                getattr(files, course).append(i.find_parent('a').get('href'))
                getattr(names, course).append(i.find_parent('span').find(text=True))
        if not getattr(files, course):
            print("looks like there are no topics in this course.")
        else:
            print("Accessed.")
    return


def get_selected_courses():
    print('Select the course you want to update from the above registered courses list by typing the number of the '
          'course. If you want to update multiple courses other than "All Courses" then multiple numbers seperated '
          'by spaces.')
    while True:
        try:
            input_list = list(map(int, input().split()))
        except ValueError:
            print("Invalid Input, please read the above statement")
        else:
            if len(input_list) == 1:
                if not 0 < input_list[0] < len(courses.list)+2:
                    print("Sorry your input must be in between 0 and", len(courses.list)+2)
                else:
                    if input_list[0] == 8:
                        sel_courses = courses.list
                        sel_courses_link = courses.links
                    else:
                        sel_courses = [courses.list[input_list[0]-1]]
                        sel_courses_link = [courses.links[input_list[0]-1]]
                    break

            else:
                for num in input_list:
                    if not 0 < num < len(courses.list)+1:
                        print("For multiple courses your inputs must be between 0 and", len(courses.list)+1)
                        break
                else:
                    sel_courses = list(courses.list[x - 1] for x in input_list)
                    sel_courses_link = list(courses.links[x-1] for x in input_list)
                    break

    return sel_courses, sel_courses_link


def print_downloading_file():
    return


def cancel_download(filename):
    print(15 * ' ', 15 * '\b', sep='', end='')
    print('cancelled')
    if os.path.isfile(filename):
        os.remove(filename)
    return


def download_from_course(course):
    # course = 'Mathematics_II'
    cur_wor_dir = os.getcwd()
    os.chdir(os.getcwd() + '/' + course)
    c, conn = connection()
    print("Now downloading files from the course", course, '...')
    for link, name in zip(getattr(files, course), getattr(names, course)):
        x = c.execute("select filename from {0} where link='{1}'".format(course, link))
        if not int(x) > 0:
            # start = time.clock()
            file_headers = session.head(link, allow_redirects=True).headers
            # print(time.clock() - start)
            filename = get_filename_from_cd(file_headers.get('content-disposition'))
            if is_downloadable(file_headers.get('content-type')):
                try:
                    file_size = int(file_headers['content-length'])
                    print('\r', filename, '(', naturalsize(file_size), ')',
                          ' downloading... ', flush=True, sep='', end='')
                    downloaded = 0
                    # sec_sta = time.clock()
                    resume.wait()
                    if kb_interrupt.isSet():
                        raise KeyboardInterrupt
                    file = session.get(link, stream=True)
                    # print(time.clock() - sec_sta)
                    with open(filename, 'wb') as f:
                        for chunk in file.iter_content(chunk_size):
                            if kb_interrupt.isSet():
                                raise KeyboardInterrupt
                            resume.wait()
                            if cancel.isSet():
                                cancel_download(filename)
                                cancel.clear()
                                break
                            if chunk:
                                f.write(chunk)
                                downloaded += len(chunk)
                            downloaded_percentage = int((downloaded/file_size)*100)
                            print('{0}% Completed'.format(downloaded_percentage),
                                  '\b'.rjust(12+len(str(downloaded_percentage)), '\b'), end='', flush=True)
                        else:
                            c.execute(
                                "insert into {0} (filename, link) values  ('{1}','{2}')".format(course, filename, link))
                            conn.commit()
                            print(15 * ' ', 15 * '\b', sep='', end='')
                            print('finished.')

                    file.close()

                except KeyboardInterrupt:
                    # print('cancelled')
                    cancel_download(filename)
                    c.execute("delete from {0} where link = '{1}'".format(course, link))
                    conn.commit()
                    c.close()
                    file.close()
                    # if os.path.isfile(filename):
                    #     os.remove(filename)
                    raise SystemExit
            else:
                print('\r' + name + ' is not downloadable')
        else:
            filename = c.fetchone()[0]
            print('\r' + filename + ' is already downloaded')
    conn.commit()
    c.close()
    print("\rFinished downloading files from the course", course)
    os.chdir(cur_wor_dir)
    return


def inp():
    while True:
        # r.wait()
        c = getch()
        if c == ' ':
            if resume.is_set():
                resume.clear()
            else:
                resume.set()
        elif c == 'c':
            resume.set()
            cancel.set()
        elif c == 'q':
            break
        elif c == '\x03':
            kb_interrupt.set()
            break
        if c == '\x1a':
            os.kill(os.getpid(), signal.SIGTSTP)

    return


with requests.Session() as session:
    setattr(page, 'login', login())
    connect_to_moodle()
    setattr(soup, 'dashboard', bs4.BeautifulSoup(page.dashboard.text, 'lxml'))
    setattr(courses, 'html', soup.dashboard.select('.course_title'))
    setattr(courses, 'list', [])
    setattr(courses, 'links', [])
    get_courses()
    print(len(courses.list)+1, ') All Courses', sep='')
    create_tables(courses.list)
    make_directories(courses.list)
    selected_courses, selected_courses_links = get_selected_courses()
    setattr(page, 'temp', '')
    setattr(soup, 'temp', '')
    get_links(selected_courses, selected_courses_links)
    inp_thread = threading.Thread(target=inp)
    inp_thread.daemon = True
    inp_thread.start()
    resume.set()
    for selected_course in selected_courses:
        download_from_course(selected_course)
    session.close()
