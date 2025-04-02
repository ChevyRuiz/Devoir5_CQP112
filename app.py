from flask import Flask, render_template, request
import re
import sympy as sym
from helpers import valider_entree, string_conversion, calculer_integrale

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
        return render_template("result.html", resultat1 = calculer_integrale(string_poly))
    
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
            int(a_string)
            int(b_string)
        except Exception:
            return render_template("error2.html")
        
        # Checker si le input est valide
        if not valider_entree(string_poly):
            return render_template("error2.html")
        string_poly = string_conversion(string_poly)
        # Retourner la primitive
        print(string_poly)
        return render_template("result2.html")