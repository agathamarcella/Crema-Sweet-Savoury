from cassandra.cluster import Cluster

class DB():
    
    def __init__(self):
        cluster = Cluster()
        self.session = cluster.connect()
        self.session.execute('USE crema')
        
    def getSession(self):
        return self.session