from User import User

class UserQuery():
    
    def init(self):
        self.makeUser()
        
    def makeUser(self):
        self.user1 = User()
        self.user1.setUsername("Jack Miller")
        self.user1.setPassword("1111")
        self.user1.setRole("Staff")
        
        self.user2 = User()
        self.user2.setUsername("Reanna Maccey")
        self.user2.setPassword("2222")
        self.user2.setRole("Staff")
        
        self.user3 = User()
        self.user3.setUsername("Michaell Rave")
        self.user3.setPassword("3333")
        self.user3.setRole("Customer")
        
        self.list = [self.user1, self.user2, self.user3]
        
    def getAllUser(self):
        return self.list
    
    def getLogin(self, username, password):
        self.role = None
        for user in self.list:
            if username == user.username and password == user.password:
                self.role = user.role
                break
        
        return self.role