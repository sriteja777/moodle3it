import getpass
import logging
import os
import re
import signal
import sys
import threading
import warnings
from subprocess import call

import bs4
import requests
from humanize import naturalsize

from config import COLORS, END_COLOR
from connection import *
from getch import _GetchUnix

dashboard_url = 'https://moodle.iiit.ac.in/my/'
chunk_size = 100000
getch = _GetchUnix()
resume = threading.Event()
cancel = threading.Event()
kb_interrupt = threading.Event()
downloading = threading.Event()
# path_to_download = '/home/sriteja/iiit/academics/sem4/'

try:
    MOODLE_USERNAME = os.environ['MOODLE_USERNAME']
    MOODLE_PASSWORD = os.environ['MOODLE_PASSWORD']
    path_to_download = os.environ['MOODLE_FILES_PATH']
except KeyError:
    print(
        "You can set three environment variables MOODLE_USERNAME, MOODLE_PASSWORD & MOODLE_FILES_PATH in order to avoid typing every time.")
    MOODLE_USERNAME = input("Enter your email id: ")
    MOODLE_PASSWORD = getpass.getpass("Enter your password: ")
    while True:
        path_to_download = input(
            "Enter the path to the directory in which the files have to download: ")
        if os.path.isdir(path_to_download):
            break
        print("Sorry the path you given is not a correct path, please try again.")


class ObjectSetup(object):
    pass


page = ObjectSetup()
soup = ObjectSetup()
files = ObjectSetup()
names = ObjectSetup()
courses = ObjectSetup()

ASK_DOWNLOAD = False
DEBUG = False
while True:
    if len(sys.argv) > 1:
        if sys.argv[1] == '-a':
            ASK_DOWNLOAD = True
            print("ASK_DOWNLOAD setted")
        elif sys.argv[1] == '-p':
            del sys.argv[1]
            if 1 < len(sys.argv):
                if os.path.isdir(sys.argv[1]):
                    path_to_download = sys.argv[1]
                else:
                    print("Please enter a valid path after option -p")
                    raise SystemExit(10)
            else:
                print("Please provide a path to the argument -p")
                raise SystemExit(8)
        else:
            print(str(sys.argv[1]) + ': Invalid Option')
            raise SystemExit(9)
        del sys.argv[1]
    else:
        break


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
    """
    Returns whether the file is downloadable or not from the file's content-type

    :param content_type: content-type of the file header
    :return: True if the file is downloadable else False
    """
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_filename_from_cd(cd):
    """
    Get filename from content-disposition.

    :param cd: content-disposition of the file header
    :return: file name
    """
    if not cd:
        return None
    name = re.findall('filename=(.+)', cd)
    if len(name) == 0:
        return None
    return re.sub(r'[^\x00-\x7f]', r'', name[0].replace('"', ''))


def create_tables(courses_list):
    """
    Create tables in the database.

    :param courses_list:
    :return: int -- the return code
    :raise: SystemExit
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            c, conn = connection()
            for course in courses_list:
                c.execute(
                    "create table if not exists {0} (filename varchar(100), link varchar(100))".format(
                        course))
            conn.commit()
    except Exception as e:
        print("Looks like there is a problem in creating tables and the problem is {}.".format(e))
        raise SystemExit(6)
    return 0


def make_directories(courses_list):
    """
    Makes courses directories.

    :param courses_list:
    :return: int -- the return code
    """
    os.chdir(path_to_download)
    for course in courses_list:
        if not os.path.isdir(course):
            os.mkdir(course)
            print('Made directory', course)
    return 0


def set_login_data():
    """
    Returns the values required for logging in.
    :returns: the login data.
    """
    url = 'https://login.iiit.ac.in/cas/login'
    execution_value = "461b10b6-4711-4b1e-8ae6-45a5c194f0a0_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVWpVNWFsQTFWbVpMTlRsalNVNTBXVzFKWVZKYVMyczFWRlEyVDNZNFpsVTNWekJwZGxaVk5VNDFjbEp0YmxkeVZqQmxNbk0wZERSa09FOUdObGQyVG1NNGRGbDRla3hxVGt4a1kxZzJUVXRWY2xwSmNYaHJUM2d2U1hsaFVHbzFURloxWmpOV1ZtZDZUbFJVVURoVldrWnNVbWsyTXpOaWJHMU5lbHBTUWxscmRuRTJTRkZ0Um01UFVGUnNka1ZoTHpWaFkzQnNNRVkzTjNOUGVrNTRlSEkyUms5WmFVZENSV2hqTjJKdVNqWkZUSGgyY1RNeFlXdFlibmR2Y0dVMVZtOVVRa1J2WlZSQlZXTTJLMnczV2tNemRHWm9ZVlYzTVd0Vk1UUjBSM2t3YVdVMmJWcFhZVTF2SzJrMFdYSnVla0Z2ZFZWeGMxbDVlVFpCYm1aS1pEZEdRbE5tY1VWRWFHZFZWMk5sTkRCUlpFUkRibTVxTkRWbmJEQXdLMU55YVVFNFZtbHBWV0ZGTmtVelRHNXZSRmhxYVdRelNsTnVVbVpIV25CQk4xaENMM1ZvTkhvNGEybEhRMUo0VFVJeldXRkhhMjF0ZUZwUk5WUldNRWRFYXpGRVZtZE5NemQ1UWtwdFQwYzNiRlZsVUU1eGMwOVVPVEozWkdsUGFrWTNOMm95V1RKNk9IbHNLek16ZVdNNWFXVlJObXhvVGpoTk9YQkJVMXBHU25wck5XMHhTMXBNVGxWcldrbHJVbmRxVGk5MWEzSXZiakZWY0RCdmVEUlZWU3RwZURSRFlWbFpNR0Z1ZFhrNVZFMVhhMWNyYTIwclRrbGxaM2cyVDFJNGMxSlljRWszVWpSWlV6QlJhVEUwUmxOdE1WVndXbVJXVldSc1RtMURUREZ2YmpsVFJFNW9NRE55YW1WTVJVWnZRMGxQTmxSTU9ETlJlbXd3WVdnNGVGQjNkMVpWYkdkeU5uVlRjVTlFYTBaRmFIWXlRME5pUm5GUVZXTXdjMnMxTm5OelRrRnNlR1EyVjBwSmNtOUdkRzFsTjA1aGNXTkZaRGQ2ZFRoVGQyVXlRa2hyZVUxc2JtSnJObFZTYm1JM1pHNUNkV2hNU0hOaFIzSklOR0ZUY0RsS01XRmFNWFZFTW5sWlQzWmhia1V4YTNodGNIaHVOa0V6VGpaTU5HWmlaMFU0VkZwMk1uSkZRbGxLYVcxeFdVMVBOMUZLVm14RFFuQXJSbXBFUW5reFVHcHhkVkZIZDB4QmNEUjVPVVZ4ZG5JeWVpOVVNR1JDVDBWbEwxVmhUV0ZYZW5CelZsZGhia3RTUTBWQ1dEbEpWMmRMSzJadGNUWmlTV3gyWkZkQ2MwVTNXRTlJWlc1TFNGbGlTRXhpTVhCWVVubFllVXRpTkRoeGRTdFZRekZUTjFsb1Jpc3lUbEowTDB0aFEwRXdZbFZaTm1oQ1JWQk5abEJVUjI1NlYwbGlVekZUV1VGMFNFSlVOR3hMUWs4NVJWVTRUaTltYW1wRlZreGlPRFJQZVdJMGFWaEhMeXMxV0VZM2FucEtUR0ZITUU1Uk0wWlFiVVphZVU5bVpYQlNhalpEVnpOWWRHZEplQzlWVGxsSlRGUk5SMnRWVms1U1VVMHJORmRTSzNaVlRVNWxSSEpCV21WTlBRLnhOTXo4RllhWXBZcmJFclBEVndpNnlseU93a3hEQnN0RjZEODNYSmFfUngyc1p0TU9LSXBFSDM4NGV5cFpjMGZyTXlnUmNYMmZvZEsxaHpxM3g5TEhn"
    username = MOODLE_USERNAME
    password = MOODLE_PASSWORD
    return url, execution_value, username, password


def advanced_login():
    """
    Tries logging in by reconnecting to iiit vpn.

    :return: the login request page
    """
    call(['/bin/bash', '-i', '-c', 'iiit -d'])
    pg = login()
    call(['/bin/bash', '-i', '-c', 'iiit -c'])
    return pg


def connect_to_moodle():
    """
    Tries connecting to moodle.

    :return: int -- the return status
    :raise: SystemExit
    """
    global page
    try:
        pg = session.get('https://moodle.iiit.ac.in/my/')
        print(COLORS['Green'] + 'Accessed to Moodle' + END_COLOR)
    except requests.ConnectionError:
        print(
            "Looks like you are not connected to iiit vpn, run iiit -c command to connect to iiit vpn")
        raise SystemExit(4)
    return pg


def get_courses():
    """
    Get the course from the Moodle dashboard page.

    :return: int -- the return status
    :raise: SystemExit
    """
    global courses
    for i in courses.html:
        courses.list.append(i.text.replace(' ', '_').replace('-', '').replace('.', ''))
        courses.links.append(i.find('a').get('href'))

    if not courses.list or not courses.html:
        print(
            COLORS[
                'Red'] + "Looks like there is some problem in getting moodle dashboard page, try after some time" + END_COLOR
        )
        raise SystemExit(5)
    else:
        print(
            COLORS['Pink'] + "You are registered to the following courses for this sem" + END_COLOR)
        [print(s_no, ') ', course, '(', COLORS['Blue'] + link + END_COLOR, ')', sep='') for
         course, s_no, link in
         zip(courses.list,
             range(1, len(courses.list) + 1),
             courses.links)]
    return 0


def login():
    """
    Login the user to iiit sites.

    :return: the login request page
    :raise: SystemExit
    """
    global session, soup
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
        logging.warning(
            "Looks like CAS is down as it does not support single Sign-Out, try logging out of all other "
            "applications or increase the timeout. But as of now I am trying some advanced method. If you "
            "see this message again and again then stop this program and try after some time.")
        return advanced_login()

    sp = bs4.BeautifulSoup(pg.text, 'lxml')
    setattr(soup, 'login', sp)

    if sp.find('p').text == success_text:
        print(COLORS['Green'] + 'Login Successful' + END_COLOR)
    else:
        # print(username, password)
        # print(pg.text)
        # print(soup.login)
        print(
            'Login Failure. Try checking credentials or change the execution value. Even if the problem persists try after some time.')
        raise SystemExit(3)
    return pg


def get_links(courses_list, courses_links):
    """
    Get the download links of the files.

    :param courses_list: List of courses for the files to get.
    :param courses_links: The links for the course in the courses_list.
    :return: int -- the return status.
    """
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
        if DEBUG:
            print(topics)
        for i in topics:
            if i.text == " File":
                getattr(files, course).append(i.find_parent('a').get('href'))
                getattr(names, course).append(i.find_parent('span').find(text=True))
        if not getattr(files, course):
            print("looks like there are no topics in this course.")
        else:
            print("Accessed.")
    return 0


def get_all_courses():
    global session, courses, DEBUG

    link = 'https://moodle.iiit.ac.in/blocks/custom_course_menu/interface.php'
    pg = session.get(link)
    sp = bs4.BeautifulSoup(pg.text, 'lxml')

    if DEBUG:
        print(sp.prettify())
        for i in sp.select('.custom_course_menu_category'):
            print('got')
            print(i.text)
        print()
        for i in sp.select('.custom_course_menu_category')[0]:
            if isinstance(i, bs4.element.NavigableString):
                print(i.strip())
    print()
    for i in sp.select('.custom_course_menu_category'):
        for j in i:
            if isinstance(j, bs4.element.NavigableString):
                print(COLORS['Yellow'] + j.strip().replace(' ', '_') + END_COLOR)
        for li in i.select('.custom_course_menu_course'):
            print(COLORS['Brown'] + li.text + END_COLOR + '(' + COLORS['Blue'] + li.find('a').get(
                'href') + END_COLOR + ')')
        print()

    return


def get_selected_courses():
    """
    Get the selected courses to download files from the user.

    :return: Selected courses by the user along with their moodle courses links.
    """
    print(
        'Select the course you want to update from the above registered courses list by typing the number of the '
        'course. If you want to update multiple courses other than "All Courses" then multiple numbers seperated '
        'by spaces.')
    while True:
        try:
            input_list = list(map(int, input().split()))
        except ValueError:
            print("Invalid Input, please read the above statement")
        else:
            if len(input_list) == 1:
                if not 0 < input_list[0] < len(courses.list) + 2:
                    print("Sorry your input must be in between 0 and", len(courses.list) + 2)
                else:
                    if input_list[0] == len(courses.list) + 1:
                        sel_courses = courses.list
                        sel_courses_link = courses.links
                    else:
                        sel_courses = [courses.list[input_list[0] - 1]]
                        sel_courses_link = [courses.links[input_list[0] - 1]]
                    break

            else:
                for num in input_list:
                    if not 0 < num < len(courses.list) + 1:
                        print("For multiple courses your inputs must be between 0 and",
                              len(courses.list) + 1)
                        break
                else:
                    sel_courses = list(courses.list[x - 1] for x in input_list)
                    sel_courses_link = list(courses.links[x - 1] for x in input_list)
                    break

    return sel_courses, sel_courses_link


def print_downloading_file():
    return


def cancel_download(filename):
    """
    Removes the file and prints cancelled.

    :param filename: Name of the file to remove
    :return: int -- the return status
    """
    print(15 * ' ', 15 * '\b', sep='', end='')
    print('cancelled')
    if os.path.isfile(filename):
        os.remove(filename)
    return


def to_download(filename):
    if ASK_DOWNLOAD:
        print('\r' + 'Are you sure want to download', filename, '?(y/n):', end='')
        go_to_next = False
        while True:
            reply = input()
            if reply == 'y':
                break
            elif reply == 'n':
                go_to_next = True
                break
            else:
                print('Please reply (y/n):', end='')
        if go_to_next:
            return False
        else:
            return True
    return True


def download_from_course(course):
    """
    Download files from the given course.

    :param course: Name of the course to download the files from.
    :return: int -- the return status.
    :raise: SystemExit
    """
    # course = 'Mathematics_II'
    # cur_wor_dir = os.getcwd()
    os.chdir(path_to_download)
    os.chdir(course)
    c, conn = connection()
    print('\r' + "Now downloading files from the course", course, '...')
    for link, name in zip(getattr(files, course), getattr(names, course)):
        x = c.execute("select filename from {0} where link='{1}'".format(course, link))
        if not int(x) > 0:
            # start = time.clock()
            file_headers = session.head(link, allow_redirects=True).headers
            # print(time.clock() - start)
            filename = get_filename_from_cd(file_headers.get('content-disposition'))
            if is_downloadable(file_headers.get('content-type')):
                try:

                    if ASK_DOWNLOAD and not to_download(filename):
                        continue

                    file_size = int(file_headers['content-length'])
                    print('\r', filename, '(', naturalsize(file_size), ')',
                          ' downloading... ', flush=True, sep='', end='')
                    downloaded = 0
                    downloading.set()
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
                                downloading.clear()
                                break
                            if chunk:
                                f.write(chunk)
                                downloaded += len(chunk)
                            downloaded_percentage = int((downloaded / file_size) * 100)
                            print('{0}% Completed'.format(downloaded_percentage),
                                  '\b'.rjust(12 + len(str(downloaded_percentage)), '\b'), end='',
                                  flush=True)
                        else:
                            downloading.clear()
                            c.execute(
                                "insert into {0} (filename, link) values  ('{1}','{2}')".format(
                                    course, filename, link))
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
    os.chdir(path_to_download)
    return 0


def download_without_database(course):
    global session
    os.chdir(path_to_download)
    os.chdir(course)

    for link, name in zip(getattr(files, course), getattr(names, course)):
        file_headers = session.head(link, allow_redirects=True).headers
        filename = get_filename_from_cd(file_headers.get('content-disposition'))
        if is_downloadable(file_headers.get('content-type')):
            try:
                if not os.path.isfile(filename):
                    file_size = int(file_headers.get('content-length'))
                    print('\r', filename, '(', naturalsize(file_size), ')',
                          ' downloading... ', flush=True, sep='', end='')
                    downloaded = 0
                    downloading.set()
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
                                downloading.clear()
                                break
                            if chunk:
                                f.write(chunk)
                                downloaded += len(chunk)
                            downloaded_percentage = int((downloaded / file_size) * 100)
                            print('{0}% Completed'.format(downloaded_percentage),
                                  '\b'.rjust(12 + len(str(downloaded_percentage)), '\b'), end='',
                                  flush=True)
                        else:
                            downloading.clear()
                            print(15 * ' ', 15 * '\b', sep='', end='')
                            print('finished.')

                        file.close()

            except KeyboardInterrupt:
                # print('cancelled')
                cancel_download(filename)
                file.close()
                raise SystemExit
        else:
            print('\r' + name + ' is not downloadable')


def inp():
    """
    Take input from the user while downloading the files.

    :return: int -- the return status
    """
    while True:
        c = getch()
        if downloading.is_set():
            if c == ' ':
                # pause the download
                if resume.is_set():
                    resume.clear()
                else:
                    resume.set()
            elif c == 'c':
                # cancel the running download
                resume.set()
                cancel.set()
        if c == 'q':
            # disable interaction
            break
        elif c == '\x03':
            # when ctrl+c is received
            resume.set()
            kb_interrupt.set()
            break
        elif c == '\x1a':
            # send ctrl+z signal to program
            os.kill(os.getpid(), signal.SIGTSTP)
    return


def get_custom_file(course, link, filename=None):
    os.chdir(path_to_download + course)
    downloaded = 0
    file = session.get(link, stream=True, allow_redirects=True)
    if not filename:
        filename = get_filename_from_cd(file.headers.get('content-disposition'))
    file_size = int(file.headers['content-length'])
    print('\r', filename, '(', naturalsize(file_size), ')',
          ' downloading... ', flush=True, sep='', end='')
    with open(filename, 'wb') as f:
        for chunk in file.iter_content(chunk_size):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
            downloaded_percentage = int((downloaded / file_size) * 100)
            print('{0}% Completed'.format(downloaded_percentage),
                  '\b'.rjust(12 + len(str(downloaded_percentage)), '\b'), end='', flush=True)
        print(15 * ' ', 15 * '\b', sep='', end='')
        print('finished.')

    file.close()
    return


def run_engine():
    global session, files, names
    setattr(page, 'login', login())
    setattr(page, 'dashboard', connect_to_moodle())
    get_all_courses()

    setattr(soup, 'dashboard', bs4.BeautifulSoup(page.dashboard.text, 'lxml'))
    setattr(courses, 'html', soup.dashboard.select('.course_title'))
    setattr(courses, 'list', [])
    setattr(courses, 'links', [])
    get_courses()
    print(len(courses.list) + 1, ') All Courses', sep='')
    create_tables(courses.list)
    make_directories(courses.list)
    selected_courses, selected_courses_links = get_selected_courses()

    # Uncomment the below lines if you want to download files from a specific course.
    # selected_courses = ["Operating_Systems"]
    # selected_courses_links = ["https://moodle.iiit.ac.in/course/view.php?id=1377"]

    setattr(page, 'temp', '')
    setattr(soup, 'temp', '')
    get_links(selected_courses, selected_courses_links)
    if DEBUG:
        print(files.Operating_Systems, names.Operating_Systems)
    if not ASK_DOWNLOAD:
        inp_thread = threading.Thread(target=inp)
        inp_thread.daemon = True
        inp_thread.start()
    resume.set()
    for selected_course in selected_courses:
        if DEBUG:
            print('files.' + selected_course + '->', getattr(files, selected_course))
        if getattr(files, selected_course) and getattr(names, selected_course):
            download_from_course(selected_course)
            print()
            # download_without_database(selected_course)
        else:
            print("\rNo files or topics in " + selected_course + ' course')

    print('\r')


with requests.Session() as session:
    if __name__ == "__main__":
        run_engine()
