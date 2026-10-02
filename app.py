from flask import Flask, render_template,request

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        if name == "madhan" and password == "1234":
            return render_template("welcome.html",name=name)

        return render_template("login.html",error="Invalid input")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)