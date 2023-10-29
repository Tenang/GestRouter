from app import create_app,db
from flask import json

from projet.app.entity import MongoAPI
#from flask_migrate import Migrate, MigrateCommand, upgrade
#from flask_script import Manager

app = create_app()
#manager = Manager(app)
#migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)


#@manager.command
''' def recreate_db():
    with app.app_context():
        #db.drop_all()
        db.create_all()
        db.session.commit()
        print('ok')

if __name__ =='__main__':
    app.run(debug=True)
    
     '''
    
    
if __name__ == '__main__':
        data = {
        "database": "IshmeetDB",
        "collection": "people",
    }
mongo_obj = MongoAPI(data)
print(json.dumps(mongo_obj.read(), indent=4))