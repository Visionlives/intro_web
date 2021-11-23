from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("base.html") 

@app.route("/add_contact")
def add_contact():
    return " "

@app.route("/edit")
def edit_contact():
    return "edit_contact"

@app.route("/delete")
def delete_contact():
    return "delete contact"

if __name__ == "__main__":
    app.run(port=3000,debug=True)