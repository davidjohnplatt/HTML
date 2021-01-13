
	
import tkinter as tk
import sqlite3

 
window = tk.Tk()
 
window.title("Family Tree Submit Form")
window.minsize(600,500)
 
def clickMe():
    label.configure(text= 'Hello ' + name.get())

def insertPerson(person):
    try:
        conn = sqlite3.connect('famTree.db')
        d = conn.cursor()

        sql = '''INSERT INTO Person(firstname,DoB,Dod,Photo,PhotoYear) VALUES(?,?,?,?,?)'''

        d.execute(sql,person)

        conn.commit()

        
    except sqlite3.Error as error:
        print("Failed to insert data", error)
    finally:
        if (conn):
            conn.close()

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid
        
 
nameLabel = tk.Label(window, text = "Name:")
nameLabel.place(x = 8, y = 50)
name = tk.StringVar()
nameEntered = tk.Entry(window, width = 30, textvariable = name)
nameEntered.place(x = 100, y = 50)

bornLabel = tk.Label(window, text = "Born:")
bornLabel.place(x = 8, y = 75)
born = tk.StringVar()
bornEntered = tk.Entry(window, width = 8, textvariable = born)
bornEntered.place(x = 100, y = 75)

diedLabel = tk.Label(window, text = "Died:")
diedLabel.place(x = 8, y = 100)
died = tk.StringVar()
diedEntered = tk.Entry(window, width = 8, textvariable = died)
diedEntered.place(x = 100, y = 100)

photoLabel = tk.Label(window, text = "Photo:")
photoLabel.place(x = 8, y = 125)
photo = tk.StringVar()
photoEntered = tk.Entry(window, width = 30, textvariable = photo)
photoEntered.place(x = 100, y = 125)

pdateLabel = tk.Label(window, text = "Photo Year:")
pdateLabel.place(x = 8, y = 150)
pdate = tk.StringVar()
pdateEntered = tk.Entry(window, width = 4, textvariable = pdate)
pdateEntered.place(x = 100, y = 150)

wperson=( nameEntered.get(),bornEntered.get(),diedEntered.get(),photoEntered.get(),pdateEntered.get())
button = tk.Button(window, text = "Submit", command = insertPerson(wperson))
button.place(x = 100, y = 200)
 
window.mainloop()
