class DB():
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS urls(url text, state int)')
        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS IDX001 ON urls(url)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS IDX002 ON urls(state)')

    def __del__(self):
        self.conn.commit()
        self.cursor.close()

    def insertURL(self, url, state=0):
        try:
            self.cursor.execute("INSERT INTO urls VALUES ('%s', %d)"%(url, state))
        except:
            return 0
        else:
            return 1

    def selectUncrawledURL(self):
        self.cursor.execute('SELECT * FROM urls where state=0')
        return [ row[0] for row in self.cursor.fetchall() ]

    def updateURL(self, url, state=1):
        self.cursor.execute("UPDATE urls SET state=%d WHERE url='%s'"%(state, url))

    def isCrawledURL(self, url):
        self.cursor.execute("SELECT COUNT(*) FROM urls WHERE url='%s' and state=1"%url)
        ret = self.cursor.fetchone()
        return ret[0]



        
