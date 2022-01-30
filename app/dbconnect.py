

class DBconnect():

    def conect(self,username,password,path,database):
        import mysql.connector
        conn = mysql.connector.connect(host = path,
                             user = username,
                             password = password,
                             database = database)

        return conn