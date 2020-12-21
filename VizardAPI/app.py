from flask import Flask
from application.entities.games.controller import games_controller_api
from application.entities.genres.controller import genres_controller_api
from application.entities.studios.controller import studios_controller_api

from application.entities.users_data.users.controller import users_api
from application.entities.users_data.user_to_games.controller import users_to_games_api
from application.entities.users_data.user_to_rates.controller import users_to_rates_api
from application.app import base

import time

app = Flask("Vizard API")

app.register_blueprint(games_controller_api)
app.register_blueprint(genres_controller_api)
app.register_blueprint(studios_controller_api)

app.register_blueprint(users_api)
app.register_blueprint(users_to_games_api)
app.register_blueprint(users_to_rates_api)

base.load()
start = time.time()
base.save()
end = time.time()

if __name__ == "__main__":
    app.run()

