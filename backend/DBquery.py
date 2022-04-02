from DBclient import *
from processDBoutput import *

DB_FILE='db_files/init_db'

#* Handle DB operatrions *#

#* users table requests *#

def selectUser(uid = None):
    
    if uid:
        res = queryDB(DB_FILE, f"SELECT * FROM users WHERE id_AI = {uid}")
    else:
        res = queryDB(DB_FILE, "SELECT * FROM users")
        
    # if db query was successful
    # process users table records to list of users
    if res[0]:
        userList = [User(col[0], col[1], col[2], col[3]).data for col in res[1]]
        #return (query success, user dict) 
        return (True, userList)
    #return (query fail, sqlite type error)
    return (False, res[1])


def createUser(name: str, password: str, uid: str):
    res = insertDB(DB_FILE, f'''INSERT INTO users
                                (full_name, password, real_id)
                                VALUES
                                ("{name}", "{password}", "{uid}");
                            ''')

#* tickets table requests *#

def selectTicket(tid = None):
    
    if tid:
        res = queryDB(DB_FILE, f"SELECT * FROM tickets WHERE ticket_id = {tid}")
    else:
        res = queryDB(DB_FILE, "SELECT * FROM tickets")
        
    # if db query was successful
    # process tickets table records to list of tickets
    if res[0]:
        userList = [Ticket(col[0], col[1], col[2]).data for col in res[1]]
        #return (query success, tickets dict) 
        return (True, userList)
    #return (query fail, sqlite type error)
    return (False, res[1])


def createTicket(uid: int, fid: int):
    res = insertDB(DB_FILE, f'''INSERT INTO tickets
                                (user_id, flight_id)
                                VALUES
                                ({uid}, {fid});
                            ''')


#* flights table requests *#

def selectFlight(fid = None):
    
    if fid:
        res = queryDB(DB_FILE, f"SELECT * FROM flights WHERE flight_id = {fid}")
    else:
        res = queryDB(DB_FILE, "SELECT * FROM flights")
        
    # if db query was successful
    # process flights table records to list of flights
    if res[0]:
        userList = [Flight(col[0], col[1], col[2], col[3], col[4]).data for col in res[1]]
        #return (query success, flights dict) 
        return (True, userList)
    #return (query fail, sqlite type error)
    return (False, res[1])


def createFlight(timestamp: str, seats: int, orig: int, dest: int):
    res = insertDB(DB_FILE, f'''INSERT INTO users
                                (timestamp, remaining_seats, origin_country_id, dest_country_id)
                                VALUES
                                ("{timestamp}", {seats}, {orig}, {dest});
                            ''')
#* countries table requests *#

def selectCountry(cid = None):
    
    if cid:
        res = queryDB(DB_FILE, f"SELECT * FROM countries WHERE code_AI = {cid}")
    else:
        res = queryDB(DB_FILE, "SELECT * FROM countries")
        
    # if db query was successful
    # process countries table records to list of countries
    if res[0]:
        userList = [Country(col[0], col[1]).data for col in res[1]]
        #return (query success, countries dict) 
        return (True, userList)
    #return (query fail, sqlite type error)
    return (False, res[1])


def createCountry(name):
    res = insertDB(DB_FILE, f'''INSERT INTO users
                                (name)
                                VALUES
                                ("{name}");
                            ''')