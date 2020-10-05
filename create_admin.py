from getpass import getpass
import sys
from app import create_app
from app.db import db
from app.user.models import User

app = create_app()
with app.app_context():
    username = input('Type user name: ')
    if User.query.filter(User.username == username).count():
        print('User name already exists')
        sys.exit(0)

    password = getpass('Type your password: ')
    password_repeat = getpass('Type your password again: ')
    if password != password_repeat:
        sys.exit(1)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    print('Added user {} with id {}'.format(username, new_user.id))
