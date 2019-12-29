from manage import db,app
from flask import current_app

app.app_context().push()
print(current_app.name)
db.create_all()