from flask import Flask
from flask_cors import CORS

from Routes.auth import auth
from Routes.jobs import jobs
from Routes.applications import applications

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(jobs, url_prefix="/api")
app.register_blueprint(applications, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "Placement Management Cell API Running"}

if __name__ == "__main__":
    app.run(debug=True)