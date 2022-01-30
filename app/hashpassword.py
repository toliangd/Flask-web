import hashlib,uuid
from web.config import Config

class HashPassword():
    def passHashSalt(self,password):
        # соль берем из файла config
        salt = Config().SALT
        # объединяем соль и пароль в одну строку
        passwordSalt = password + salt
        # перводим формат строки в байты
        passwordSaltBytes = str.encode(passwordSalt)
        # хэшируем последовательность байтов алгоритмом sha512 и ограничиваем длинну hexdigest
        hashed_password = "'" + hashlib.sha512(passwordSaltBytes).hexdigest() + "'"
        return hashed_password

