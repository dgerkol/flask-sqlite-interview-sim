import sqlite3



def create_db_file(db_dir = './init_db'):
    conn = None
    try:
        conn = sqlite3.connect(db_dir)
        
    except sqlite3.Error as err:
        print(err)
        
    finally:
        if conn:
            conn.close()


def init_db(db_dir = './init_db'):
    conn = sqlite3.connect(db_dir)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE "countries" 
                    ( "code_AI" INTEGER UNIQUE, 
                    "name" TEXT NOT NULL UNIQUE, 
                    PRIMARY KEY("code_AI" AUTOINCREMENT) );
                    ''')
    conn.commit()
    
    cursor.execute('''CREATE TABLE "flights" 
                    ( "flight_id" INTEGER UNIQUE, 
                    "timestamp" TEXT NOT NULL, 
                    "remaining_seats" INTEGER, 
                    "origin_country" INTEGER NOT NULL, 
                    "dest_country" INTEGER NOT NULL, 
                    PRIMARY KEY("flight_id"), 
                    FOREIGN KEY("origin_country") 
                    REFERENCES "countries"("code_AI"), 
                    FOREIGN KEY("dest_country") 
                    REFERENCES "countries"("code_AI") );
                    ''')
    conn.commit()
    
    cursor.execute('''CREATE TABLE "tickets" 
                    ( "ticket_id" INTEGER UNIQUE, 
                    "user_id" INTEGER NOT NULL UNIQUE, 
                    "flight_id" INTEGER NOT NULL, 
                    PRIMARY KEY("ticket_id"), 
                    FOREIGN KEY("flight_id") 
                    REFERENCES "flights"("flight_id") );
                    ''')
    conn.commit()
    
    cursor.execute('''CREATE TABLE "users" 
                    ( "id_AI" INTEGER, 
                    "full_name" TEXT NOT NULL, 
                    "password" TEXT NOT NULL, 
                    "real_id" TEXT NOT NULL UNIQUE, 
                    PRIMARY KEY("id_AI" AUTOINCREMENT), 
                    FOREIGN KEY("id_AI") 
                    REFERENCES "tickets"("user_id") );
                    ''')
    conn.commit()
    
    conn.close()



if __name__ == '__main__':
    if db_dir := input('DB file dir (default: ./init_db): '):
        create_db_file(db_dir)
        init_db(db_dir)
    else:
        create_db_file()
        init_db()
    