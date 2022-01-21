import pymysql

MYSQL_HOST = '211.47.75.102'
class Database():
  def __init__(self):
    self.db = pymysql.connect(
      host=MYSQL_HOST,
      port=3306,
      user='public0917',
      passwd='public2423!',
      db='dbpublic0917',
      charset='utf8mb4'
    )
    self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

  def execute(self, query, args={}):
    self.cursor.execute(query, args)

  def executeOne(self, query, args={}):
    self.cursor.execute(query, args)
    row = self.cursor.fetchone()
    return row

  def executeAll(self, query, args={}):
    self.cursor.execute(query, args)
    row = self.cursor.fetchall()
    return row

  def commit(self):
    self.db.commit()
