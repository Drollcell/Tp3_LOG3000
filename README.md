# Tp3_LOG3000

Numéros d'équipe: 32

But et portée du projet: Cette application permette d'effectuer les opérations
    arythmétiques (addition, soustraction, multiplication et divison) à l'aide des chiffres de 0 à 9.

Guide d'installation: 
  1. Installer Python 3.9 ou plus.
  2. Créer un environnement virtuel 
  3. Installer flask en utilisant la commande pip: 'python -m pip install flask'.

Guide d'utilisation:
  1. Lancer l'application en utilisant la commande: 'python app.py'. (Si une fenêtre du navigateur ne s'ouvre pas
     automatiquement, ouvrir l'adresse (fournie dans le terminal) dans le navigateur)
  2. Sélectionner le premier nombre.
  3. Sélectionner l'opérateur.
  4. Sélectionner le second nombre. 
  5. Soumettre l'opération (=) pour optenir le résultat.
  6. Effacer le résultat (C).
  7. Reprendre à partir de l'étape 2.

Guide de test: 

Fichier: app.py
  Description: Ce ficher permet de vérifier le respect des nomres d'écriture 
    d'un opération arithmétique et, dans le cas du respect de ces dernières, 
    d'obtenir le résultat d'opération et de l'afficher sur un navigateur. 
  Responsabilités: 
    - Vérifier la structure de l'opération fournie
    - Sélectionner le bon opération arithmétique à effectuer.
    - Afficher le résultat de l'opération lors de la soumission de l'opération

Fichier: operators.py
  Description: Ce fichier contient la logique des quatres opérations arithmétiques, soit l'addition, la soustraction, la
    multiplication et la division. 
  Responsabilités: 
    - Fournir le résultat d'opérations arithmétiques.