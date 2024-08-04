import uuid

class UserCreate:
  def __init__(self, user_repository) -> None:
    self.__user_repository = user_repository

  def create(self, body):
    try:

      user_id = str(uuid.uuid4())

      user_infos = {
        "id": user_id,
        "name": body["name"],
        "email": body["email"],
        "password": body["password"],
        "profilePhoto": body["profilePhoto"],
      }

      self.__user_repository.create_user(user_infos)

      return {
        "body": { "user_id": user_id },
        "status_code": 201
      }
      

    except Exception as exception:
      return {
          "body": { "error": "Bad Request", "message": str(exception) },
          "status_code": 400
        }