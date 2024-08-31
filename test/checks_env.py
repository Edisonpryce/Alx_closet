from dotenv import load_dotenv
import os

load_dotenv()

print("MYSQL_USER:", os.getenv('MYSQL_USER'))
print("MYSQL_PWD:", os.getenv('MYSQL_PWD'))
print("MYSQL_HOST:", os.getenv('MYSQL_HOST'))
print("MYSQL_DB:", os.getenv('MYSQL_DB'))
