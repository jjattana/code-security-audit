import os
import pymysql
from urllib.request import urlopen

# Vulnerability: Hardcoded Credentials
# Credentials in code can be leaked or exposed.
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

# Vulnerability: Lack of Input Validation
# The user input is not validated or sanitized.
def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

# Vulnerability: Insecure Transport
# Using HTTP instead of HTTPS exposes data in transit.
def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

# Vulnerability: SQL Injection
# The query is constructed using string formatting, which is dangerous.
def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()



if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
