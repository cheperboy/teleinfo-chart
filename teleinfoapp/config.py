import os

currentpath = os.path.abspath(os.path.dirname(__file__)) # /home/pi/Development/teleinfo/teleinfoapp
projectpath = os.path.dirname(currentpath)               # /home/pi/Development/teleinfo
envpath = os.path.dirname(projectpath)                   # /home/pi/Development
envname = os.path.basename(envpath)                      # Development
"""
print 'currentpath '+currentpath
print 'projectpath '+projectpath
print 'envpath '+envpath
print 'ENVNAME '+envname
"""
print 'ENVNAME : '+envname
print 'db path '+os.path.join(projectpath + '\db\\', 'teleinfo.db')
"""Base configuration."""
APP_NAME = "Teleinfo"
SECRET_KEY = os.getenv('SECRET_KEY', default='my_secret')
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False

#detect env from filesystem location (Proc/Dev)
if envname == 'Development' :
    """Development configuration."""
    APP_NAME += ' Dev'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(projectpath + '/db/', 'app.db'))
    SQLALCHEMY_BINDS = {
        'teleinfo':         'sqlite:///' + os.path.join(projectpath + '/db/', 'teleinfo.db'),
        'teleinfo_minute':  'sqlite:///' + os.path.join(projectpath + '/db/', 'teleinfo_minute.db'),
        'teleinfo_hour':    'sqlite:///' + os.path.join(projectpath + '/db/', 'teleinfo_hour.db')
    }
    
elif envname == 'Production':
    """Production configuration."""
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    WTF_CSRF_ENABLED = True
    
elif envname == 'flask-dev' :
    """Windows Development configuration."""
    APP_NAME += ' Win Dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(
        os.path.join(projectpath + '\db\\', 'teleinfo.db'))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(projectpath + '\db\\', 'app.db'))
    SQLALCHEMY_BINDS = {
        'teleinfo':         'sqlite:///' + os.path.join(projectpath + '\db\\', 'teleinfo.db'),
        'teleinfo_minute':  'sqlite:///' + os.path.join(projectpath + '\db\\', 'teleinfo_minute.db'),
        'teleinfo_hour':    'sqlite:///' + os.path.join(projectpath + '\db\\', 'teleinfo_hour.db')
    }
    

else:
    """Undefined configuration."""
    APP_NAME += ' /!\\'
    
