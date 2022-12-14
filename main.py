
from app import socket
from app import app
from app import db
import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        socket.run(app, debug=True, port=os.getenv("PORT", default=5000))
