import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='University_db' user='postgres' password='usmanghani' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS student(reg_no VARCHAR,reg_date VARCHAR, category VARCHAR, names VARCHAR , degree VARCHAR, department VARCHAR, status VARCHAR, duration VARCHAR)')
    conn.commit()
    conn.close()


def insert_table(reg_no, reg_date, cat, name, degree, department, status, duration):
    conn = psycopg2.connect("dbname='University_db' user='postgres' password='usmanghani' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute('INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', (reg_no, reg_date, cat, name,
                                                                        degree, department, status, duration))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='University_db' user='postgres' password='usmanghani' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student;")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(reg_no):
    conn = psycopg2.connect("dbname='University_db' user='postgres' password='usmanghani' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM student Where reg_no=%s;", (reg_no,))
    conn.commit()
    conn.close()


def update(reg_no, cat, status):
    conn = psycopg2.connect("dbname='University_db' user='postgres' password='usmanghani' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE student SET status=%s, category=%s WHERE reg_no=%s;", (status, cat, reg_no))
    conn.commit()
    conn.close()


def search(reg_no=None, reg_date=None, cat=None, name=None, degree=None, department=None, status=None, duration=None):
    conn = psycopg2.connect("dbname='University_db' user='postgres' password='usmanghani' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE reg_no=%s OR reg_date=%s OR category=%s OR names=%s OR degree=%s OR department=%s OR status=%s OR duration=%s; ",
                (reg_no, reg_date, cat, name, degree, department, status, duration))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


create_table()
