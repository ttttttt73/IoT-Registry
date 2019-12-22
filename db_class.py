import MySQLdb


class DB:
    def __init__(self):
        self.conn = MySQLdb.connect("localhost", "pi", "pi", "dev_regi")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS SensorINFO(topic text, dev_name text, sensor_name text, interface text, sensor_type text, data_type text, delay_time text, valid_max text, valid_min text)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Reading(topic text, value float, time timestamp)')

    def __del__(self):
        self.conn.commit()
        self.cursor.close()

    def insertSensorINFO(self, url, state=0):
        query = "INSERT SensorINFO (topic, dev_name, sensor_name, interface, sensor_type, data_type, delay_time, valid_max, valid_min) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(query, (
            topic, dev_name, sensor_name, interface, sensor_type, data_type, delay_time, valid_max, valid_min))
        except:
            print("Got exception " + str(e))

    def insertReading(self, topic, value, time):
        query = "INSERT INTO Reading (topic, value, time) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(query, (topic, value, time))
        except:
            print("Got exception " + str(e))

    def selectSensorINFO(self, topic):
        self.cursor.execute("SELECT * FROM SensorINFO where topic= '" + topic + "'")
        # self.cursor.execute("SELECT * FROM SensorINFO where topic = 'reading/temperature/test1'")
        # print( [ row[0] for row in self.cursor.fetchall() ])
        # return [ row[0] for row in self.cursor.fetchall() ]
        ret = self.cursor.fetchone()
        return ret[0]

    def selectReading(self, topic):
        self.cursor.execute("SELECT * FROM Reading where topic = '" + topic + "'")
        return [row[0] for row in self.cursor.fetchall()]

    def updateURL(self, url, state=1):
        self.cursor.execute("UPDATE urls SET state=%d WHERE url='%s'" % (state, url))

    def isCrawledURL(self, url):
        self.cursor.execute("SELECT COUNT(*) FROM urls WHERE url='%s' and state=1" % url)
        ret = self.cursor.fetchone()
        return ret[0]
