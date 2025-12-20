from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline using Jenkins & Docker from Surya kiran from git from github to local system !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
