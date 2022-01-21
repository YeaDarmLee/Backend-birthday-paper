from flask_login import UserMixin
from .DbModule import Database

class CardRepository(UserMixin):

  def __init__(self, sender_nm, receiver_nm, receiver_idx, card_msg, c_date):
    self.sender_nm = sender_nm
    self.receiver_nm = receiver_nm
    self.receiver_idx = receiver_idx
    self.card_msg = card_msg
    self.c_date = c_date

  @staticmethod
  def findCardByReceiverIdx(userIdx):
    print('== card_data findCardByReceiverIdx ==')
    try:
      db_class = Database()
      sql = "SELECT * FROM bp_card_data WHERE RECEIVER_IDX = '" + str(userIdx) + "'"
      cardList = db_class.executeAll(sql)
      return cardList
    except Exception as e:
      print(e)

  @staticmethod
  def create(sender_nm, receiver_nm, receiver_idx, card_msg):
    print('== card_data create ==')
    try:
      db_class = Database()
      sql = "INSERT INTO bp_card_data (SENDER_NM, RECEIVER_NM, RECEIVER_IDX, CARD_MSG) VALUES ('%s', '%s', '%s', '%s')" % (
        str(sender_nm), str(receiver_nm), str(receiver_idx), str(card_msg))
      db_class.execute(sql)
      db_class.commit()
    except Exception as e:
      print(e)