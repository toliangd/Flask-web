from web.app.dbconnect import DBconnect
from web.config import Config
import re
from web.app.hashpassword import HashPassword
from web.app.hashlogin import HashLogin

conf = Config()

class DBCreateUser():
    def createUser(self,login,password):
        conect = DBconnect()
        con = conect.conect(conf.DB_LOGIN,
                            conf.BD_PASS,
                            conf.DB_ADDRESS,
                            conf.DB_NAME)
        cursor = con.cursor(buffered=True)
        # экранируем спецсимволы логина и пароля
        login = re.escape(login)
        password = re.escape(password)
        # создаем экземпляр класса, передаем в его метод пароль для добавления соли и хэширования
        password = HashPassword().passHashSalt(password)
        # создаем экземпляр класса, передаем в его метод логин для хэширования
        login = HashLogin().loginHash(login)
        # ищем пользователя с таким логином
        cursor.execute('SELECT login FROM users WHERE login={}'.format(login))
        checkLogin = cursor.fetchall()
        # если есть, то выводим ошибку
        if checkLogin:
            con.close()
            return 'login incorrect'
        # если нет, то создаем запись в БД
        else:
            cursor.execute('INSERT INTO users (login,password,privilage) VALUE ({},{},"user")'.format(login,password))
            con.commit()
            con.close()

