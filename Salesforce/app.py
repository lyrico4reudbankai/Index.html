
from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = "my_secret_key_123"

USERNAME = "admin"
PASSWORD = "12345"


def check_login(username, password):
    return username == USERNAME and password == PASSWORD


@app.route("/", methods=["GET", "POST"])
def login():

    error = ""
    success = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if check_login(username, password):
            success = "LOGIN SUCCESSFUL! Welcome, " + username
        else:
            error = "Incorrect Username or Password!"

    return render_template(
        "index.html",
        error=error,
        success=success
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)