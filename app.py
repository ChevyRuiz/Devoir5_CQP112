from flask import Flask, render_template, request

import re
import base64
from io import BytesIO

import numpy as np
import sympy as sym
from matplotlib.figure import Figure

from helpers import *

"""
Fichier principal qui contient l'app web (librarie Flask)

Description: Un programme qui permet de faire differents calculs sur de polynômes, principalement
des opérations liées au calcul integral.
"""

# Application web
app = Flask(__name__)

"""
La route '/' contient index.html, une page qui montre les 3 differents formulaires de l'application
- Trouver la primitive et la déerivée
- Calculer l'aire sous la courbe
- Simplifier et décomposer en fractions partielles

"""
@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "GET":
        return render_template("index.html")

"""
La route '/data1' contient result.html, une page qui affiche l'inégrale et la dérivéé du polynôme soumis dans le form.
Si l'imput n'est pas valide, on affiche error.html
"""
@app.route("/data1", methods=["GET", "POST"])
def form_1():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        string_poly = request.form.get("polynomial")

        # Checker si le input est valide
        if not valider_entree(string_poly):
            return render_template("error.html")
        # Formatter la string correctement
        string_poly = string_conversion(string_poly)
        # Retourner la primitive
        return render_template("result.html", resultat1 = calculer_integrale(string_poly), resultat11 = calculer_derivee(string_poly))

"""
La route '/data2' contient result2.html, une page qui affiche l'aire sous la courbe et une représentation graphique
du polynôme soumis dans le form.
Si l'imput n'est pas valide, on affiche error2.html
"""
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

    # représenter graphiquement l'aire sous la courbe
    fig = Figure()
    ax = fig.subplots()

    x = sym.symbols('x')
    f = eval(string_poly)

    x_array = np.linspace(a, b, 1000)
    f_array = sym.lambdify(x, f)(x_array)

    sym.plot(f, (x, a, b),fig=fig, ax=ax, fill={'x': x_array,'y1':f_array,'color':'yellow'}, xlabel="", ylabel="", title="Aire sous la courbe")

    # Créer l'image
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    return render_template("result2.html", resultat2 = calculer_aire(a, b, string_poly), drawing=f"<img src='data:image/png;base64,{data}'/>")

"""
La route '/data3' contient result3.html, une page qui affiche la simplification de la fontion et sa décomposicion en 
fractions partielles.
Si l'imput n'est pas valide, on affiche error3.html
"""
@app.route("/data3", methods=["GET", "POST"])
def form_3():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        # Check que les 2 forms sont soumis
        if not request.form.get("numerator") or not request.form.get("denominator"):
            return render_template("error3.html")
        
        string_numerator = request.form.get("numerator")
        string_denominator = request.form.get("denominator")

        # Valider l'input
        if not valider_entree(string_numerator) or not valider_entree(string_denominator):
            return render_template("error3.html")
        
        string_numerator = "(" + string_conversion(string_numerator) + ")"
        string_denominator = "(" + string_conversion(string_denominator) + ")"
        string_rationelle = string_numerator + "/" + string_denominator
        
        return render_template("result3.html", simple=simplify_denom(string_rationelle), fractions=partial_fractions(string_rationelle))