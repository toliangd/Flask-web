import hashlib,uuid

class HashLogin():
    def loginHash(self,login):
        # перводим формат строки в байты
        loginBytes = str.encode(login)
        # хэшируем последовательность байтов алгоритмом sha512 и ограничивае длинну hexdigest
        hashed_login = "'" + hashlib.sha512(loginBytes).hexdigest() + "'"
        return hashed_login