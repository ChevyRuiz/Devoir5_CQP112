from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Fonctions
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
        string_poly = request.form.get("polynomial", "abc")
        # Checker si le input est valide
        if not valider_entree(string_poly):
            return render_template("error.html")
        
        # Retourner la primitive
        print(string_poly)
        return render_template("result.html")
    
@app.route("/data2", methods=["GET", "POST"])
def form_2():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        string_poly = request.form.get("polynomial2", "abc")
        # Checker si le input est valide
        if not valider_entree(string_poly):
            return render_template("error2.html")
        
        # Retourner la primitive
        print(string_poly)
        return render_template("result2.html")