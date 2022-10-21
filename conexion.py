class Config:
    SECRET_KEY = "3ckoKxOIJG_4?Ffda9hjps*%#$0c"

class DevelopmentConfig(Config):
    DEBUG = True;
    MYSQL_HOST = '34.176.177.146'
    MYSQL_USER = 'lautaro'
    MYSQL_PORT = 3306
    MYSQL_PASSWORD = 'lautikapo11'
    MYSQL_DB = 'bd_florida'
    
    #MYSQL_UNIX_SOCKET = '/opt/lampp/var/mysql/mysql.sock'


config = {
    'development' :DevelopmentConfig
}