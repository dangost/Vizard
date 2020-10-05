from flask import Flask
from application.entities.games.controller import games_controller_api
from application.entities.genres.controller import genres_controller_api
from application.entities.studios.controller import studios_controller_api
from application.app import base

import time

app = Flask(__name__)

app.register_blueprint(games_controller_api)
app.register_blueprint(genres_controller_api)
app.register_blueprint(studios_controller_api)

base.load()
start = time.time()
base.save()
end = time.time()
print(end-start)

if __name__ == "__main__":
    app.run()

