# Replace your database credentials with each below parameters


PGHOST = "localhost"
PORT = "5432"
PGDATABASE = "env_db"
PGUSER = "env_master"
PGPASSWORD = "M123xyz"
URL = "postgresql://" + PGUSER + ":" + PGPASSWORD + \
    "@" + PGHOST + ":" + PORT + "/" + PGDATABASE
