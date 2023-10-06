from flask import Flask
from flask_jwt_extended import JWTManager

class MyFlaskApp(Flask):
    def init(self, args, **kwargs):
        super(MyFlaskApp, self).init(args, **kwargs)
        self.config['JWT_SECRET_KEY'] = 'your-secret-key'
        jwt = JWTManager(self)

app = MyFlaskApp(__name__)
