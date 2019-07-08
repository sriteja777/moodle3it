import sqlite3
import os


class Database:
    def __init__(self, database):
        direc = os.path.expanduser("~/.moodle3it")
        if not os.path.isdir(direc):
            os.mkdir(direc)
        os.chdir(direc)

        self.conn = sqlite3.connect(database)

    def create_course_tables(self, courses_list):
        for course in courses_list:
            self.conn.execute("create table if not exists {0} (filename varchar(100), link varchar(100))".format(
                        course))

    def check_file(self, course, link):
        x = self.conn.execute("select filename from {0} where link='{1}'".format(course, link))
        data = x.fetchone()
        # print('\r', data, '\n\n')
        if data is None:
            return -1, None
        else:
            return 1, data[0]
        # exit(2)
        # return data

    def delete_entry(self, course, link):
        self.conn.execute("delete from {0} where link = '{1}'".format(course, link))

    def insert_file(self, course, link, filename):
        x = self.conn.execute("insert into {0} (filename, link) values  ('{1}','{2}')".format(
                                    course, filename, link))
        self.conn.commit()
        return

    def close(self):
        self.conn.close()

