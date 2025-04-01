import re
#import sympy

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

    # later evaluate wqhen using sympy


prettify("5x^3+x^2+7")
"""
sympy.init_printing()
x = sympy.Symbol('x')
function = 3*x**2 + 1
function_plot = sympy.plot(function, show=False)
#integral = sympy.integrate(function, x)
#integral_plot = sympy.plot(integral, show=False)
function_plot.show()
#print(integral)
"""

