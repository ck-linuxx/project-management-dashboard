CREATE TABLE IF NOT EXISTS "users" (
  id TEXT PRIMARY KEY,
  user_name TEXT NOT NULL,
  user_email TEXT NOT NULL,
  user_password TEXT NOT NULL,
  profilePhoto BLOB,
  tasks TEXT,
)

CREATE TABLE IF NOT EXISTS "projects" (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  members ARRAY NOT NULL
  todos ARRAY,
  onProgress ARRAY,
  done ARRAY,
  projectImage TEXT,
  data BLOB NOT NULL,
  created_at DATE,
  finish_at DATE,
  level_priority TEXT NOT NULL
)

CREATE TABLE IF NOT EXISTS "messages" (
  id TEXT PRIMARY KEY,
  user ARRAY NOT NULL
)