from flask import Flask

from app.posts.views import posts_blueprint
from app.api.views import api_blueprint
from app import logger


app = Flask(__name__)

logger.create_logger()

app.config['JSON_AS_ASCII'] = False
#app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

if __name__ != "__main__":
    app.run(port=8002)


