import DB

class User():
    
    def __init__(self):
        self.db = DB()
        self.session = self.db.getSession()
        
    def getName(self):
        rows = self.session.execute('SELECT Name FROM User')
        for row in rows : 
            print(row.Name)
            
    def Main(self):
        self.getName