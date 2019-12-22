import pymysql.cursors

def main():
    try:
        conn = pymysql.connect(
            user = 'root',
            passwd = 'password',
            host='192.168.0.1',
            db='world'
            )
        c = conn.cursor()
        c.execute(sql)
        sql = 'select * from city;'
        for row in c.fetchall():
            print('no : ', row[0], 'content : ', row[1])
    except Exception as e:
            logger.error(e)
            logger.exception(e)
            raise
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        file_writer.close()    

main()
