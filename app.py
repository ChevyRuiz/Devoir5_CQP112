from flask import Flask, render_template, request
import re
import sympy as sym
from helpers import valider_entree, string_conversion, calculer_integrale, calculer_derivee, calculer_aire
import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np

app = Flask(__name__)

# Application web
@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "GET":
        return render_template("index.html")
    
@app.route("/data1", methods=["GET", "POST"])
def form_1():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        string_poly = request.form.get("polynomial")
        # Checker si le input est valide
        if not valider_entree(string_poly):
            return render_template("error.html")
        string_poly = string_conversion(string_poly)
        # Retourner la primitive
        return render_template("result.html", resultat1 = calculer_integrale(string_poly), resultat11 = calculer_derivee(string_poly))
    
@app.route("/data2", methods=["GET", "POST"])
def form_2():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        #Checker que les 3 forms soient soumis
        if not request.form.get("polynomial2") or not request.form.get("polynomiala") or not request.form.get("polynomialb"):
            return render_template("error2.html")
        
        string_poly = request.form.get("polynomial2")
        a_string = request.form.get("polynomiala")
        b_string = request.form.get("polynomialb")
        #Checker si a et b sont des entiers
        try: 
            a = int(a_string)
            b = int(b_string)
        except Exception:
            return render_template("error2.html")
        
        # Checker si le input est valide
        if not valider_entree(string_poly):
            return render_template("error2.html")
        string_poly = string_conversion(string_poly)
        # Retourner la primitive
        print(string_poly)

    # graphing the area under the curve
    try:
        fig = Figure()
        ax = fig.subplots()

        x = sym.symbols('x')
        f = eval(string_poly)

        x_array = np.linspace(a, b, 1000)
        f_array = sym.lambdify(x, f)(x_array)

        sym.plot(f, (x, a, b),fig=fig, ax=ax, fill={'x': x_array,'y1':f_array,'color':'yellow'}, xlabel="", ylabel="", title="Aire sous la courbe")

        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template("result2.html", resultat2 = calculer_aire(a, b, string_poly), drawing=f"<img src='data:image/png;base64,{data}'/>")
    except Exception:
        img = ""
        return render_template("result2.html", resultat2 = calculer_aire(a, b, string_poly), drawing="")