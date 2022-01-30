from web.app.hashlogin import HashLogin
from web.app.hashpassword import HashPassword
from web.app.dbconnect import DBconnect
from web.config import Config

class DBLogin():
    def login(self,login,password):
        login = HashLogin().loginHash(login)
        password = HashPassword().passHashSalt(password)
        connect = DBconnect().conect(Config.DB_LOGIN,
                                     Config.BD_PASS,
                                     Config.DB_ADDRESS,
                                     Config.DB_NAME)
        cursor = connect.cursor()
        cursor.execute('SELECT status,privilage FROM users WHERE login={} AND password={}'. format(login,password))
        checkLogin = cursor.fetchall()
        if checkLogin:
            # статус пользователя 0-отключен
            if checkLogin[0][0] == 1:
                connect.close()
                return True
        else:
            connect.close()
            return False
