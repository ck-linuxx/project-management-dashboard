import pytest
import uuid
from ..models.repositories.user_repository import UserRepository
from ..models.settings.db_connection_handle import db_connection_handler


db_connection_handler.connect()
user_id = str(uuid.uuid4)

# @pytest.mark.skip(reason= "interação com o banco")
def test_create_user():
  conn = db_connection_handler.get_connection()
  user_repository = UserRepository(conn)

  user_infos = {
    "id": user_id,
    "user_name": "Teste Junior",
    "user_email": "junior@gmail.com",
    "user_password": "password",
    "user_profile": "",
  }

  user_repository.creater_user(user_infos)