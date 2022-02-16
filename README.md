# OC Projet 12 / CRM / BODIN

Ce CRM est une API développée avec le framework django REST, permet de recevoir des requêtes CRUD (create, read, update, delete).

## Installation

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone https://github.com/Dyna-Soar/oc_p12_crm.git`
2. Créer une base de donnée PostgreSQL   
3. Rendez-vous depuis un terminal à la racine du répertoire oc_p10_api avec la commande `$ cd oc_12_crm`
4. Installez les dépendances de à l'aide de la commande `pip install -r requirements.txt`
5. Configurez les liens entre l'application et la base de donnée Postgres dans settings.py


## Exécution

1. Créer les tables postgreSQL en effectuant la migration des modèles `python manage.py migrate`
2. Lancez le serveur avec la commande `$ python3 manage.py runserver`
3. Rendez-vous sur le serveur local (http://127.0.0.1:8000/) pour consulter les points d'entrées de l'API `http://127.0.0.1:8000/`