import re
import sympy as sym

"""
Fichier qui contient des fonctions pour traiter l'user input et faire les calculs
"""
def valider_entree(entree):
    """
    Cette fonction prend comme entree l'input user des formulaires, et checke
    s'il est un polynome valide ou un entier en utilisant regex
    """
    valide = False
    # Enlever les espaces
    entree = entree.strip()
    entree = entree.replace(' ','')

    # Checker si c'est un entier
    try:
        int(entree)
        return True
    except Exception:
        pass

    # Pattern regex
    pattern1 = re.compile(r"^[+-]?\d*x(?:\^\d+)?(?:\s*[+-]\s*\d*x?(?:\^\d+)?)*$")
    pattern2 = re.compile(r"^([+-]?\d*)x\^(\d+)$")

    # Checker si ca match
    if pattern1.match (entree) or pattern2.match(entree):
        valide = True
    else:
        valide = False

    entree = string_conversion(entree)
    
    # Checker si la fonction marche avec sympy
    try:
        x = sym.Symbol("x")
        function = eval(entree)
        derivee = sym.diff(function, x)
        valide = True
    except Exception:
        valide = False

    return valide
    
def string_conversion(entree):
    """
    Cette fonction prend comme entree l'user input (polynome) et le transforme en une string qui peut etre evalué
    avec sympy.
    Exemple:
    '3x + 1  ' -> '3*x + 1'
    '-x ^ 2 + 5x + 6  ' -> '-x**2 + 5*x + 6'
    """
    entree = entree.strip()
    entree = entree.replace(' ', '')
    entree = entree.replace('x^','x**' )
    entree = list(entree)

    # Ajouter une * si un caractere x a un coefficient ex: '3x' -> '3*x'
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


def simplify_denom(entree):
    x = sym.Symbol("x")
    function = eval(entree)
    num = sym.numer(entree)
    denom = sym.denom(entree)

    # Factoriser
    try:
        denom = sym.factor(denom)
        num = sym.factor(num)
    except (sym.SympifyError, TypeError, ValueError):
        pass
    
    return sym.latex(sym.sympify(num/denom))

def partial_fractions(entree):
    x = sym.symbols("x")
    return sym.latex(sym.apart(eval(entree)))