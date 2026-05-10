from flask import Flask, render_template

app = Flask(__name__)



@app.route("/index") # controlador
def hello():
    base_de_datos   =   ["jorge", "pepe","Juanito"] # modelos
    return render_template(
        "index.html",
        datos=base_de_datos
    )
 #view

if __name__ == "__main__":
    app.run(debug=True)
