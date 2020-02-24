import psycopg2

def Create():
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER, isbn REAL)")
    conn.commit()
    conn.close()

def View():
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def Insert(title,author,year,isbn):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (%s,%s,%s,%s)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def Delete(title):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE title = %s",(title,))
    conn.commit()
    conn.close()

def Update(title,author="",year="",isbn=""):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    if author != "": cur.execute("UPDATE books SET author=%s WHERE title=%s",(author, title))
    if year != "": cur.execute("UPDATE books SET year=%s WHERE title=%s",(year, title))
    if isbn != "": cur.execute("UPDATE books SET isbn=%s WHERE title=%s",(isbn, title))
    conn.commit()
    conn.close()

def Search(title="",author="",year="",isbn=""):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=%s OR author=%s OR year = %s OR isbn=%s",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

Create()