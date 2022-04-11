import sqlite3


def connClose(conn):
    conn.close()


def commitOpp(conn):
    conn.commit()
    conn.close()


def queryDB(db_file: str, opp: str):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    try:
        oppResult = cursor.execute(opp)
        
    except sqlite3.Error as err:
        return (False, err, conn)
    
    return (True, oppResult, conn)


def insertDB(db_file: str, opp: str):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        oppResult = cursor.execute(opp)
        
    except sqlite3.Error as err:
        return (False, err, conn)
    
    return (True, oppResult, conn)

