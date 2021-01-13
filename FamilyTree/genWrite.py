import sqlite3

def getWife(wifePid):
    d = conn.cursor()
    d.execute('SELECT FirstName,LastName FROM Person WHERE Pid = ' + str(wifePid))
    ddata = d.fetchmany(1)
    for row in ddata:     
        return (row[0] + " " + row[1])



try:
    conn = sqlite3.connect('famTree.db')
    c = conn.cursor()


    gen = 0
    id = []
    name = []
    dob = []
    dod = []
    photo = []
    pyear = []
    index = []

    file_handle = open("data.html", "w") 

    c.execute('SELECT * FROM Person WHERE sex = "M" OR MarriedTo = 0 ORDER BY Gen DESC')
    data = c.fetchall()
    for row in data:
        if (row[1] != gen):
           print(" ")
        gen = row[1]
        print(row[0], row[1], row[4], row[5],getWife(row[7]))

    c.close()
    
except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (conn):
        conn.close()
        print("The SQLite connection is closed")




file_handle.close()
print("End")
