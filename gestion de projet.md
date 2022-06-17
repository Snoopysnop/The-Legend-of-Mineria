# Gestion de projet

## Mathis Fouillen

### *Site et base de donnée (2 semaines)*
**Partie dynamique du site (langages PHP et MySQL) :**
   * Se connecter via Discord sur la page d'accueil
   * Ajouter un serveur à la base de donnée sur la page d'installation
   * Barre de recherche des serveurs (par id et nom) de la base de donée
   * Voir/Modier/Supprimer un serveur de la base de donnée
   * Voir les serveurs de la base de donnée sur lesquels l'utilisateur est présent
   * Communication PHP / Python pour lancer l'application

### *Application (4 semaines)*
**Communication Python / Discord** (1 semaine)
   * Utilisation de l'API de discord pour envoyer des messages via Python
   * L'application réagit aux interractions des utilisateurs (supression message, ajout de réaction...)

**Jeu** (3 semaines)
   * Création d'un fichier pour écrire les évenenements
      * Evenements de base (texte)
      * Evenements spéciaux (combats, mort, ...)
      * Conditions (si un évenement est déjà fait alors, prérequis d'or, ..)
      * Récompenses (or, expérience, objets, ...)
      

   * Création du fichier Python pour lire et interpréter les évenements
      * En cas d'évenement spécial, genère un texte particulier (affichage des points de vie pour un combat, ...)
      * Sélécteur d'ennemis pour les combats contre plusieurs adversaires
      * Gestion de la mort (retour en arrière)
      * Gestion des récompenses

### *Documentation (3 jours)*
   * Pages README.md, manuel d'utilisation.md, histoire.md, INSTALL.md et participation à la vidéo de présentation.



## Gwenaël Gombert

### *Site internet (2 semaines)*

**Partie statique du site (langages HTML et CSS) :**
   
* Creation de la page d'acceuil ainsi que des pages : installation, bestiaire, leaderboard. 
* Utilisation du css afin d'embélir toutes les pages du site.

### *Application (4 semaines)*

**Partie jeu (langage python)**

* Creation de plusieurs classes afin d'avoir un jeu structuré.
    * Une classe "combat" permettant d'effectuer un tour de jeu contre un ou plusieurs monstres.
    * Une classe "character" permettant de créer un personnage et d'effectuer diverses actions sur lui.
    * Une classe "classes" definissant des classes que peut prendre un personnage.
    * Une classe "item" regroupant et definissant tous les items de notre jeu qui ont des effets.
    * Une classe "attack" permettant au personnage d'attaquer avec différentes attaques.
    * Une classe "level" permettant au personnage et aux monstres d'avoir des niveaux différents.
    


* Creation de diverses fonctionnalitées majoritairement dans les classes "combat" et "character"
    * Character :
        * Creation d'un inventaire.
        * Creation d'un systeme de point de défense.
        * Creation d'un systeme d'esquive.
        * Creation d'un systeme d'argent dans le jeu.
        * ...
    * Combat :
        * Creation d'un combat tour par tour
        * Creation d'un mécanisme d'attaque sur plusieurs cibles
        * Creation d'un ordre de jeu
        * ...

### *Documentation (3 jours)*

   * Document DESIGN.md
   * Participation et montage de la vidéo de présentation





## Florian David

### *Jeu (6 semaines)*
**Personnages et Items** (2 semaine)
   * Création des classes des personnages/mobs et items
   
      * Getters et Setters, gestion d'heritage de classe
      * Caractéristiques de bases (HP,Attaque, ...)
      * Fonctions de base (heal, ajout d'or, ...)
      * Ajout d'un système pour l'utilisation de consomable
      


**Système de combat** (4 semaines)
   * Reflexion sur la logique de combat et création de la classe
    
      * Choix des paramètres de la classe en fonction des besoin pour la création des quêtes
      * Mise en place des fonctions de base (joueurMort, degat des mobs, ...)
      * Gestion de l'ordre de combat avec un trie des participants en fonction de leurs initiatives
      * Gestion de la boucle de combat






## Florian Rasemont

### *Lore (2 semaines)*
   * Etablissement de l'histoire du jeu (création de l'environnement, personnages, monstres...)
   * Créations des quêtes (Enchaînement, déroulement de l'histoire)
   * Recherche d'idée pour les mécaniques du jeu

### *Quêtes (3 semaines)*
   * Chronologie et echaînement des quêtes:
      Rentrer les quêtes dans le json afin d'avoir un jeu fonctionnel. Coopération avec Mathis afin de coder les mécaniques 
         de jeux et les rendre applicables dans le json.
   * Equilibrage des combats (gestion de l'xp/gold gagné, niveaux des monstres..)

### *Finitions (1 semaine)*
   * Compte-rendu du travail apporté
   * Finitions jeux (quêtes...)
