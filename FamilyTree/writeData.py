import sqlite3



conn = sqlite3.connect('famTree.db')
c = conn.cursor()



id = []
name = []
dob = []
dod = []
photo = []
pyear = []
index = []

file_handle = open("data.js", "w") 

c.execute('SELECT * FROM Person')
data = c.fetchall()
for row in data:
    index.append(row[0] % 1000)
    id.append(str(row[0]))
    name.append(row[3] + " " + row[4])
    photo.append(row[7])
    pyear.append(row[8])
    dob.append(row[9])
    dod.append(row[10])
    file_handle.write("<div>\n")
    file_handle.write("   <ul>\n")
    file_handle.write("      <button onclick='popWindow(")
    file_handle.write(str(row[0] % 1000))
    file_handle.write(")'>")
    file_handle.write(row[3] + " " + row[4])
    file_handle.write("</button>\n")
    file_handle.write("   </ul>\n")
    file_handle.write("</div>\n")
    print(row[0])
    print(row[0] % 1000)
  

file_handle.write("const id  = ") 
file_handle.write(str(id))
file_handle.write(";\n") 

file_handle.write("const name  = ") 
file_handle.write(str(name))
file_handle.write(";\n") 

file_handle.write("const photo = ") 
file_handle.write(str(photo))
file_handle.write(";\n") 

file_handle.write("const pyear = ") 
file_handle.write(str(pyear))
file_handle.write(";\n") 

file_handle.write("const dob = ") 
file_handle.write(str(dob))
file_handle.write(";\n") 

file_handle.write("const dod = ") 
file_handle.write(str(dod))
file_handle.write(";\n") 

file_handle.write("const index = ") 
file_handle.write(str(index))
file_handle.write(";\n")




file_handle.close()
print("End")
