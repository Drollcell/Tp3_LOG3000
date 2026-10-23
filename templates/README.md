Module templates :
  Description : Regroupe les gabarits HTML utilisés par Flask pour afficher l'interface de l'application. 
  Contient les fichiers :

    Fichier : index.html
      Description : Page unique de la calculatrice. Elle affiche l'écran
        et le clavier, puis envoie l'expression saisie au serveur Flask
        lorsque l'utilisateur clique sur «=».
      Responsabilités :
        - Afficher le résultat transmis par Flask (variable `result`).
        - Fournir les boutons de chiffres, d'opérateurs et d'effacement.
        - Construire l'expression à l'écran avec JavaScript.
        - Envoyer l'expression au serveur par une requête POST (champ `display`).
        - Charger la feuille de style `static/style.css`.
