# coding=utf-8

from ihome import Create_APP,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


#创建flask应用对象
app = Create_APP('develop')
manager = Manager(app)

Migrate(app,db)
manager.add_command("db",MigrateCommand)





if __name__ == '__main__':
    manager.run()