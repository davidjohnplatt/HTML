import sqlite3

def getWife(wifePid):
    d = conn.cursor()
    d.execute('SELECT FirstName,LastName FROM Person WHERE Pid = ' + str(wifePid))
    ddata = d.fetchmany(1)
    for row in ddata:     
        return (row[0] + " " + row[1])

def countGen(gen,row):
    kount = 0
    for i in range(0, (len(row))):
        if (str(row[i][0:1]) == str(gen)): 
            kount = kount + 1
            
    return kount
   
    

def getParent(PPid):
    
    d = conn.cursor()
    DPid = 0
    MPid = 0
    
    d.execute('SELECT * FROM Person WHERE Pid = ' + str(PPid))
    ddata = d.fetchmany(1)
    for row in ddata:
        DPid = row[2]
        MPid = row[3]
        nameDict[row[0]] = row[4] + " " + row[5]
        dobDict[row[0]] = row[10]
        dodDict[row[0]] = row[11] 
        photoDict[row[0]] = row[8]
        pdateDict[row[0]] = row[9]
        genDict[row[0]] = row[1]
        rowData.append(str(row[1]) + str(row[0]))      
     
    if (DPid != 0):
          getParent(DPid)
    if MPid != 0:
          getParent(MPid)
              


try:
    print("Start...")
    conn = sqlite3.connect('famTree.db')


    rowData = []
    Pid = 1015
    nameDict = { }
    dobDict = { }
    dodDict = { }
    photoDict = { }
    pdateDict = { }
    genDict = { }
    

    file_handle = open("walktree.html", "w") 

    getParent(1015)
    sRowData = (sorted(rowData,reverse=True))
    firstRow = True
    
    saveGen = 0
    for i in range(0, (len(sRowData))):      
        Gen = sRowData[i][0:1]       

        if Gen != saveGen:
            saveGen = Gen
            if firstRow:
                firstRow = False
                file_handle.write("<div id = grid" + str(countGen(Gen,sRowData)) + "> \n" )
            else:
                file_handle.write("</div> \n" )
                file_handle.write("<div id = grid" + str(countGen(Gen,sRowData)) + "> \n" )
                 
        Pid = int(sRowData[i][1:5])
        print(sRowData[i], nameDict[Pid], dobDict[Pid], dodDict[Pid], photoDict[Pid], dobDict[Pid])
        file_handle.write("   <div>\n")
        file_handle.write("      <ul>\n")
        file_handle.write("         <button onclick='popWindow(" + chr(34) + nameDict[Pid] + chr(34))
        file_handle.write("," + chr(34) + dobDict[Pid] + chr(34))
        file_handle.write("," + chr(34) + dodDict[Pid] + chr(34))
        file_handle.write("," + chr(34) + photoDict[Pid] + chr(34))
        file_handle.write("," + chr(34) + str(pdateDict[Pid]) + chr(34))
        file_handle.write(")'>"  + nameDict[Pid] + "</button>\n")
        file_handle.write("      </ul>\n")
        file_handle.write("   </div>\n")
        
  
    file_handle.write("</div> \n" )
    print(sRowData)
      
except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (conn):
        conn.close()
        print("The SQLite connection is closed")




file_handle.close()
print("End")
