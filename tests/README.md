Module test:
  Description: Regroupe les de tests nécessaires à la 
    vérification du bon fonctionnement de l’application
  Contient les fichiers :

    Fichier : testApp.py
      Description : Contient les tests unitaires permettant de vérifier le bon
        fonctionnement des opérations arithmétiques de la calculatrice ainsi
        que les réponses HTTP de l’application Flask.
      Responsabilités :
        -Tester les additions faites avec la méthode calculate.
        -Tester les soustractions faites avec la méthode calculate.
        -Tester les multiplications faites avec la méthode calculate.
        -Tester les divisions faites avec la méthode calculate.
        -Tester les routes HTTP de Flask

    Fichier : testIndex.py
      Description : contient les tests unitaires qui vérifient le bon
        fonctionnement, le contenu et l’accessibilité de la page de la
        calculatrice Flask.
      Responsabilités :
        -Vérifier la disponibilité de la page d’accueil
        -Tester les boutons numériques en vérifiant leur présence, leurs
          fonctions JavaScript et leurs libellés visibles.
        -Tester les opérateurs mathématiques (+, -, *, /) ainsi que leurs
          symboles affichés.
        -Vérifier les boutons de calcul et d’effacement, notamment = et la
          fonction clearDisplay().

    Fichier : testOperators.py
      Description : Contient les tests unitaires des opérations arithmétiques
        (add, subtract, multiply et divide) afin de vérifier leur exactitude et
        leur comportement dans différents cas d'utilisation.
      Responsabilités :
        -Tester l'addition.
        -Tester la soustraction.
        -Tester la multiplication.
        -Tester la division.

    Fichier : testStyle.py
      Description : Contient les tests unitaires qui vérifient la présence des 
        propriétés CSS essentielles afin de vérifier la mise en page, le style 
        et les interactions visuelles de la calculatrice.
      Responsabilités :
        -Tester le chargement du CSS.
        -Tester la mise en page.
        -Tester le style de l'application.
        -Tester la disposition des boutons.