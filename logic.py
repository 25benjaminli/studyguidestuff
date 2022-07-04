import sqlite3

conn = sqlite3.connect('database.db', check_same_thread = False)

def printAllSubjects():
    print(conn.execute("SELECT * FROM subject").fetchall())

def printAllRows():
    print(conn.execute("SELECT * FROM row").fetchall())

# def createNewSubject():
def wipeRows():
    conn.execute("DELETE FROM row")
    conn.commit()

def wipeSubjects():
    conn.execute("DELETE FROM subject")
    conn.commit()

def wipeEverything():
    wipeRows()
    wipeSubjects()

def processInfo(subjectName, title, typ, contributors):
    # create subject if it doesn't exist
    subjectId = 0
    zz = conn.execute("SELECT COUNT(subjectName) FROM subject WHERE subjectName = \"" + str(subjectName) + "\"").fetchone()[0]
    zz2 = conn.execute("SELECT COUNT(subjectName), subjectId FROM subject WHERE subjectName = \"" + str(subjectName) + "\"").fetchone()[0]
    print('hello world')
    print(zz)
    
    print(zz2)
    
    if (int(zz) == 0):
        # subject doesn't exist.
        print("doesn't exist!")
        print("subject name: " + subjectName)
        ct = int(conn.execute("SELECT COUNT(*) FROM subject").fetchone()[0])
        print(str(ct))
        conn.execute("INSERT INTO subject values (?, ?)", (str(ct), subjectName,))
        conn.commit()

        subjectId = ct
        print("subject id new: " + str(subjectId))

    else:
        b = conn.execute("SELECT subjectId FROM subject WHERE subjectName = \"" + str(subjectName) + "\"").fetchone()[0]
        subjectId = int(b)
        print("subject id exists: " + str(subjectId))

    # create row with ID

    # create cell under that row
    print("hiel")
    # printAllRows()

    conn.execute("INSERT INTO row values(NULL, ?, ?, ?, ?)", (str(title), str(typ), str(contributors), str(subjectId)))

    conn.commit()

def getAllCells(subjectName):
    x = conn.execute("SELECT r.title, r.type, r.contributors FROM row r, subject s WHERE s.subjectName = \"" + str(subjectName) + "\" AND r.subjectId = s.subjectId and r.rowId = r.rowId").fetchall()

    print("printing cells from " + subjectName)
    for i in x:
        print(i)

    return x
def editSubjWithId(id):
    pass
def getEverything():
    subjects = conn.execute("SELECT subjectId FROM subject").fetchall()
    subjectNames = conn.execute("SELECT subjectName FROM subject").fetchall()
    rows = conn.execute("SELECT * FROM row").fetchall()
    print("subjects:")
    print(subjects)
    print("names:")
    print(subjectNames)
    print("rows:")
    print(rows)
    arr = [] # hold subject name
    for (sid, sname) in zip(subjects, subjectNames):
        print(sid, sname)
        r = conn.execute("SELECT * FROM row WHERE subjectId = " + str(sid[0])).fetchall()
        arr.append([sname[0], (r)])
    
    print(arr)
    
    return arr
    # rows = conn.execute("SELECT rowId")

    


    


        