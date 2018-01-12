from flask import Flask, render_template
app = Flask(__name__)

@app.route("/bcr/users/<username>")
def user(username):
    return render_template("users.html", username=username)

if __name__=='__main__'
    app.run()