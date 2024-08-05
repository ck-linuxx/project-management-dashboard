

class UserLogin:
  def __init__(self, login):
    self.__login = login

  def login(self, body):
    try:

      user_infos = {
        "user_email": body["email"],
        "user_password": body["password"],
      }

      self.__login.user_login(user_infos)

      return {
        "body": { "user_id": user_infos["id"] },
        "status_code": 200
      }

    except Exception as exception:
      return {
        "body": { "error": "Bad Request", "message": str(exception) },
        "status_code": 400
      }