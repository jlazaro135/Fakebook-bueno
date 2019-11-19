from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aficiones")
def aficiones():
    return render_template("aficiones.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")



if __name__ == '__main__':
    app.run()