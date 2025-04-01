from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Fonctions d'aide
def valider_entree(entree):

    entree = entree.strip()
    entree = entree.replace(' ','')

    pattern1 = re.compile(r"^-?\d*x(?:\^\d+)?(?:\s*[+-]\s*\d*x?(?:\^\d+)?)*$")
    pattern2 = re.compile(r"^(-?\d*)x\^([⁰¹²³⁴⁵⁶⁷⁸⁹]|\d+)$")
    try:
        int(entree)
        return True
    except Exception:
        pass
    if pattern1.match (entree) or pattern2.match(entree):
        return True
    else:
        return False
    
def string_conversion(entree):
    entree = entree.strip()
    entree = entree.replace(' ', '')
    entree = entree.replace('x^','x**' )
    entree = list(entree)
    i = 0
    for i in range(len(entree)):
        if entree[i] == "x" and i > 0 and entree[i-1].isdigit():
            entree.insert(i,'*')

    entree = ''.join(entree)
    return entree


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
        print(string_poly)
        return render_template("result.html")
    
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