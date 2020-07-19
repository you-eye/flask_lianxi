# 配置文件# 公共配置
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/flasklianxi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dlfkjdklfdj'


# 开发环境配置
class DevelopmentConfig(Config):
    ENV = 'development'


# 生产环境配置
class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
