import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def counter():
    count = r.incr("visits")
    return f"Visitas: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
