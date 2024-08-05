from sqlite3 import Connection
from typing import TypedDict

UserInfo = TypedDict("UserInfo",  {"user_email": str, "user_password": str})

class LogIn:
  def __init__(self, conn: Connection):
    self.__conn = conn

  def user_login(self, user_infos: UserInfo) -> None:
    cursor = self.__conn.cursor()

    verify_user_credentials = cursor.execute(
      ''' 
        SELECT *
        FROM users 
        WHERE user_email = ? AND user_password = ?
      ''', (
        user_infos["user_email"],
        user_infos["user_password"],
      )
    )

    if(not verify_user_credentials): 
      return {
      "body": {"error": "Email or password are incorrect"},
      "error": 400
      }
    else:
      return {
        "body": {"id": verify_user_credentials}
      }
    

    
    

    