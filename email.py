from fileinput import close
from itertools import count
import sqlite3
import re
conn = sqlite3.connect('mail.db')

c = conn.cursor()

# c.execute(""" CREATE TABLE Mails (
#     sender text,
#     reciever text,
#     subject text
# )  """)

# c.execute("INSERT INTO Mails VALUES ('OMRI','BEN','WORK')")

# conn.commit()
# conn.close()

def check_file():
    f = open('mail.txt')
    all_lines = []
    counter = 0
    for line in f:
        counter +=1
        if counter < 4:
            value = re.findall('"([^"]*)"', line)# retunes the needed value of the line 
            all_lines.append(value[0]) # create array of the data
    sql = """ INSERT INTO Mails (sender,reciever,subject) VALUES (?,?,?)"""
    val =(all_lines[0],all_lines[1],all_lines[2])
    conn.cursor().execute(sql, val)
    conn.commit()

check_file()