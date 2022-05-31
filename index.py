#Importacion de flask
from flask import Flask, render_template

#variable para el main
app = Flask(__name__, template_folder= "templates")

#funcion para cargar el html/pagina del cliente
@app.route("/")
def principal():
    return render_template("cliente.html")

#funcion para cargar el html/pagina del admin
@app.route("/admin")
def administrador():
    return render_template("admin.html")

#funcion para cargar el html/pagina del tienda
@app.route("/tienda")
def tienda():
    return render_template("tienda.html")

#Ejecucion del main
if __name__ == "__main__":
    app.run(debug=True)


clientes = []
tiendas = []
