import pymysql


def connection():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Sriteja@27",
                           db="dfr_2_1",
                           use_unicode=True,
                           charset="utf8")
    c = conn.cursor()
    return c, conn


def dict_connection():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Sriteja@27",
                           db="dfr_1_2",
                           use_unicode=True,
                           charset="utf8",
                           cursorclass=pymysql.cursors.DictCursor
                           )
    c = conn.cursor()
    return c, conn


# c, conn = connection()
# course = 'Mathematics_II'
# # sql = "create table if not exists " + course + " (filename varchar(100), link varchar(100))"
# c.execute("create table if not exists {0} (filename varchar(100), link varchar(100))".format(course))
# c.execute(sql)
# link = 'https://moodle.iiit.ac.in/mod/resource/view.php?id=11837'
# c.execute("select * from {0} where link='{1}'".format(course, link))
# filename = "temp"
# c.execute("insert into {0} (filename, link) values ('{1}','{2}')".format(filename, link))
# c.execute("select * from Mathematics_II")
