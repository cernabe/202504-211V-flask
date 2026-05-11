from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # controlador
def root():
    return render_template(template_name_or_list="base.html") #view

@app.route("/index") # controlador
def index():
    base_de_datos   =   ["jorge", "pepe","Juanito"] # modelos
    return render_template(template_name_or_list="index.html", datos=base_de_datos ) #view

@app.route("/home") # controlador
def home():
    return render_template(template_name_or_list="home.html") #view


