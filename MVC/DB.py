from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster

class DB():
    
    def __init__(self):
        cluster = Cluster()
        cluster.connection_class= LibevConnection
        self.session = cluster.connect()
        self.session.execute('USE crema')
        
    def getSession(self):
        return self.session