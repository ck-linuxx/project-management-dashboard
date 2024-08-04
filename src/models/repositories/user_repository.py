from sqlite3 import Connection
from typing import Dict

class UserRepository:
  def __init__(self, conn: Connection):
    self.__conn = conn
  
  def creater_user(self, user_infos: Dict) -> None:
    cursor = self.__conn.cursor()



    find_email =  cursor.execute(
      '''
        SELECT user_email
        FROM users
      '''
    )

    if(find_email == user_infos["user_email"]):
      return {
        "body": {"error": "User already exits"}
      }


    cursor.execute(
      '''
        INSERT INTO users 
          (id, user_name, user_email, user_password, user_profile)
        VALUES
          (?,?,?,?,?)
      ''', (
        user_infos["id"],
        user_infos["user_name"],
        user_infos["user_email"],
        user_infos["user_password"],
        user_infos["user_profile"],
      )
    )

    self.__conn.commit()