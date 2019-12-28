import sqlite3
import json
from collections import OrderedDict
import tkinter as tk
from tkinter import filedialog


con = sqlite3.connect('test.db')
cur = con.cursor()

def insert():
    root = tk.Tk()
    root.withdraw()
    json_path = filedialog.askopenfilename(initialdir="./", title='디바이스정보 불러오기', filetypes=[('.JSON files', '.json'), ("All files", "*.*")])
    if len(json_path) > 0:
        with open(json_path) as json_file:
            json_data = json.load(json_file)
            json_data2 = json.dumps(json_data)
            # json_data = json.dumps(json_data, indent=4, sort_keys=True)
        print(type(json_data2))
        print(json_data)
        query = "INSERT INTO  IoT(data) values (?)"
        cur.execute(query, [json_data2])
        # someitem = next(iter(json_data.values()))
        # columns = list(someitem.keys())
        # print(someitem)
        # print(columns)

def search():
    search = """SELECT json_value(data, '$.topic') as topic from IoT"""
    cur.execute(search)
    result = cur.fetchall()
    print(result)

"""cur.execute("CREATE TABEL IoT (ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY CLUSTERED, "
            "UserID AS 'UID' + RIGHT('0000' + CAST(ID AS VARCHAR(8)), 4) PERSISTED, "
            "name text);")"""
# cur.execute("CREATE TABLE dbtest(ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY CLUSTERED, UserID AS 'UID' + RIGHT('00000000' + CAST(ID AS VARCHAR(8)), 8) PERSISTED);")
cur.execute("""
create table if not exists IoT (ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
data json);""")

# insert()
search()
con.commit()
con.close()
