# Database connection
import pymssql

SERVER="localhost"
USER="sa"
PASSWORD="Pa$$w0rd"
DB="DEMO_PYTHON"

connection = pymssql.connect(SERVER, USER, PASSWORD, DB)
cursor = connection.cursor()

