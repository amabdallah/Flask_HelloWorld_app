from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World from GCP (Salt Lake City)!"

if __name__ == '__main__':
    #  This is only for local development. In GCP, the server is managed
    #  by the platform.
    app.run(host='0.0.0.0', port=int("8080"), debug=True)
