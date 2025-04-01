import re

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

def prettify(entree):
    entree = entree.strip()
    entree = entree.replace(' ','')