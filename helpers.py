import re
import sympy as sym

# Fonctions d'aide
def valider_entree(entree):
    """
    Cette fonction prend comme entree l'input user des formulaires, et checke
    s'il est un polynome valide ou un entier en utilisant regex
    """

    # Enlever les espaces
    entree = entree.strip()
    entree = entree.replace(' ','')

    # Pattern regex
    pattern1 = re.compile(r"^[+-]?\d*x(?:\^\d+)?(?:\s*[+-]\s*\d*x?(?:\^\d+)?)*$")
    pattern2 = re.compile(r"^([+-]?\d*)x\^([⁰¹²³⁴⁵⁶⁷⁸⁹]|\d+)$")

    # Checker si c'est un entier
    try:
        int(entree)
        return True
    except Exception:
        pass

    # Si ca match, on retourne vraie, else on retourve faux
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

def calculer_integrale(entree):
    try:
        x = sym.Symbol("x")
        function = eval(entree)
        integral = sym.integrate(function, x)
        return sym.latex(integral)
    except Exception:
        return ""
    
def calculer_derivee(entree):
    try:
        x = sym.Symbol("x")
        function = eval(entree)
        derivee = sym.diff(function, x)
        return sym.latex(derivee)
    except Exception:
        return ""
    
def calculer_aire(a, b, entree):
    try:
        x = sym.Symbol("x")
        function = eval(entree)
        aire = sym.integrate(function, (x, a, b))
        return sym.latex(abs(aire))
    except Exception:
        return ""


