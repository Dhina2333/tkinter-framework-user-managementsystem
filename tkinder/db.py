import sqlite3


class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS teams(
            id integer primary key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        );
        """
        self.cur.execute(sql)
        self.con.commit()
#insert function
    def insert(self,name,age,doj,email,gender,contact,address):
        
        self.cur.execute("insert into teams values (NULL,?,?,?,?,?,?,?)",
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()

#fetch All Data from DB
    def fetch(self):
        self.cur.execute("Select * from teams")
        rows=self.cur.fetchall()
        #print(rows)
        return rows


#Delete Record in DB
    def remove(self,id):
        self.cur.execute("delete from teams where id=?",(id,))
        self.con.commit()


#Update Record in DB
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update teams set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=? ",
                         (name,age,doj,email,gender,contact,address,id))
        self.con.commit()



        
        



