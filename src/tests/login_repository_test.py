import pytest
from ..models.repositories.login_repository import LogIn
from ..models.settings.db_connection_handle import db_connection_handler

db_connection_handler.connect()

def test_login_user():
  conn = db_connection_handler.get_connection()
  login = LogIn(conn)

  user_infos = {
    "user_email": "junior@gmail.com",
    "user_password": "password",
  }

  login.user_login(user_infos)