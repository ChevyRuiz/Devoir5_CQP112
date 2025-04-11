# Devoir5_CQP112

## Description:

Un programme qui peut: Calculer la primitive d'un polynome ax^n + bx^m + c, Calculer l'aire sur la courbe ax^n + bx^m + c
dans l'intervalle \[a,b\] et créer une répresentation graphique, Simplifier et décomposer p(x)/g(x) en fractions partielles

`app.py` contient tout le code lié à l'application web (librarie Flask).

`helpers.py` contient toutes les fonctions liées au traitement de l'user input et le calcul des intégrales (librarie re et sympy).

## Setup

1. Copiez sur voter terminal `git clone https://github.com/ChevyRuiz/Devoir5_CQP112.git` pour cloner le repo dans votre ordinateur
2. Dirigez vous à ce dossier dans votre ordinateur, ex: `cd Devoir5_CQP112`
3. Si vous êtes déjà dans un virtual environment, c'est-à-dire (.venv) est à côté de votre prompt (dans Pycharm), continuez à la prochaine étape. Sinon, activez le virtual environment avec `source venv/bin/activate` (S'il n'existe pas, créez-le avec `python -m venv venv` avant)
4. Installez les modules necessaires avec `pip install -r requirements.txt`
5. Démarrez l'app avec `flask run` et clickez sur le lien dans votre terminal
