from flask import Flask, request
import pymysql

app = Flask(__name__)
class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost', 
            user='root', 
            password='ваш_пароль', 
            database='flask_auth'
        )
        self.cursor = self.conn.cursor()

 
    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE user_name = %s", (username,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        db = Database()
        user = db.get_user(username)
        db.close()

       
        if user and user[2] == password:  
            return "Успешный вход!"
        else:
            return "Ошибка: неверный логин или пароль"
            
    return '''
        <form method="post">
            Логин: <input name="username"><br>
            Пароль: <input name="password"><br>
            <button>Войти</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
