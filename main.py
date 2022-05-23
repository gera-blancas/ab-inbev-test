from flask import Flask
import services 
import logging

def runApp():
    app = Flask(__name__)
    services.registerRoutes(app=app)
    logging.basicConfig(level=logging.INFO)
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    runApp()