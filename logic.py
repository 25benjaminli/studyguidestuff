from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3
import os
from werkzeug.utils import secure_filename

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

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


def processInfo(subjectName, title, url, typ, contributors, category):
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
        conn.execute("INSERT INTO subject values (?, ?, ?)", (str(ct), subjectName, category))
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

    conn.execute("INSERT INTO row values(NULL, ?, ?, ?, ?, ?, ?)", (str(title), str(url), str(typ), str(contributors), str(subjectId), str(0)))

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
  
    categories = conn.execute("SELECT category FROM subject").fetchall()
  
    rows = conn.execute("SELECT * FROM row").fetchall()
  
    print("subjects:")
    print(subjects)
    print("names:")
    print(subjectNames)
    print("rows:")
    print(rows)
    arr = [] # hold everything
    di = {}
    for category in categories: # overarching category
      # two categories - Science & Other
      subjectArr = []
      print("hi")
      for (sid, sname) in zip(subjects, subjectNames): # for each subject
        # two subjects - AP Biology & 10th grade electives
        
          if int(conn.execute("SELECT COUNT(*) FROM row WHERE isaccepted = 1 AND subjectId = " + str(sid[0])).fetchone()[0]) >= 1:
            
            print("category: ")
            print(category[0])
            print(sid, sname)
            print(conn.execute("SELECT r.*, s.category FROM row r, subject s WHERE r.subjectId = s.subjectId AND s.category == \"" + str(category[0]) + "\"").fetchall())
            r = conn.execute("SELECT r.* FROM row r, subject s WHERE r.subjectId = s.subjectId AND s.category == \"" + str(category[0]) + "\" AND isaccepted = 1").fetchall()
            print("RNAME")
            rname = conn.execute("SELECT s.subjectName FROM row r, subject s WHERE r.subjectId = s.subjectId AND s.category == \"" + str(category[0]) + "\" AND isaccepted = 1").fetchall()
            print(rname)
            if len(r) > 0 and di.get(rname[0][0], 1) == 1:
              subjectArr.append([rname[0][0], (r), category[0]])
              di[rname[0][0]] = 0;
      print("ARRRRRR")
      print(subjectArr)
      arr.append([category[0], subjectArr])
    print(arr)
    
    return arr
    # rows = conn.execute("SELECT rowId")

    


def checkEmail(email):
  # print(conn.execute("SELECT isapproved FROM moderator WHERE email = ?", ((email),)).fetchone())
  print(conn.execute("SELECT * from moderator").fetchall())
  if conn.execute("SELECT isapproved FROM moderator WHERE email = ?", ((email),)).fetchone() != None:
    
    asdf = conn.execute("SELECT isapproved FROM moderator WHERE email = ?", ((email),)).fetchone()[0]
    appr = int(asdf)
    modId = int(conn.execute("SELECT id FROM moderator WHERE email = ?", ((email),)).fetchone()[0])

    print("isapproved: " + str(appr))
    print("modid: " + str(modId))

    return (appr, modId)
  else:
    return False


# def createAndAuth(email, passw):
#     conn.execute("INSERT INTO moderator values (NULL, ?, ?, ?)", ((email), (generate_password_hash(passw, method="sha256")), (1)))
#     conn.commit()

def getPassHash(email):
    x = conn.execute("SELECT passw FROM moderator WHERE email = ?", ((email),)).fetchone()[0]
    print("x: " + x)
    return x
    
