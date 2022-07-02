import sqlite3

conn = sqlite3.connect('database.db', check_same_thread = False)

def printAllSubjects():
    print(conn.execute("SELECT * FROM subject").fetchall())

def printAllCells():
    print(conn.execute("SELECT * FROM cell").fetchall())

# def createNewSubject():
def processInfo(subjectName, title, typ, contributors):
    # create subject if it doesn't exist
    subjectId = 0
    if (int(conn.execute("SELECT COUNT(subjectName) FROM subject WHERE subjectName = \"" + str(subjectName) + "\"").fetchone()[0]) == 0):
        # subject doesn't exist.
        print("doesn't exist!")
        conn.execute("INSERT INTO subject values(\"" + str(subjectName) + "\", ?)")
        subjectId = int(conn.execute("SELECT COUNT (*) FROM subject").fetchone()[0])

    conn.commit()

    # create row with ID

    conn.execute("INSERT INTO row values(?, " + str(subjectId) + ")")
    rowId = int(conn.execute("SELECT COUNT(*) from row").fetchone())
    # create cell under that row
    print("row number: " + str(rowId))

    conn.execute("INSERT INTO cell values(?, \"" + str(title) + "\", \"" + str(typ) + "\", \"" + str(contributors) + "\", " + str(rowId) + ")")


def getAllCells(subjectName):
    x = conn.execute("SELECT c.title, c.type, c.contributors FROM cell c, row r, subject s WHERE s.subjectName = \"" + str(subjectName) + "\" AND r.subjectId = s.subjectId and c.rowId = r.rowId").fetchall()

    print("printing cells from " + subjectName)
    for i in x:
        print(i)

    return x
        

    


    


        