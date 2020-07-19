from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import settings
from apps import create_app
from apps.user.model import User
from ext import db

app = create_app()
app.config.from_object(settings)
manager = Manager(app=app)

# 命令工具
migrate = Migrate(app=app, db=db)  # 命令与app关联
manager.add_command('db', MigrateCommand)  # 命令与manager关联
if __name__ == '__main__':
    manager.run()
