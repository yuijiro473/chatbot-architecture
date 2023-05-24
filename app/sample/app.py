from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db' # use the name of the service in docker-compose.yml
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_DB'] = 'test_db'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS hello_world_table (text VARCHAR(255))''')
    cur.execute('''INSERT INTO hello_world_table (text) VALUES ("Hello, World!")''')
    mysql.connection.commit()
    cur.execute('''SELECT * FROM hello_world_table''')
    greeting = cur.fetchone()
    return greeting[0] # return the first row

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
