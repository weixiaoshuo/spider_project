import os


# Application
settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'cookie_secret': "sfhksfhfkasfhshfhjehwfhsdfascmkaspqqwrrffweff",
    'xsrf_cookies': True,
    'debug': True
}


# mysql
mysql_options= dict(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'ihome',
)

# mongodb
mongodb_options = dict(
    host='127.0.0.1',
    port=27017
)

# log file path
log_lever = 'debug'
log_file = os.path.join(os.path.dirname(__file__), 'logs/log')
