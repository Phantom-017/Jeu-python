from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["python_game_db"]

# stockage des 10 héros jouables
collection_heroes = db["Heroes"]

# stockage des 10 monstres à combattre
collection_monsters = db["Monsters"]

# historique des 3 meilleurs scores avec le nom d'utilisateur des joueurs
collection_scores = db["Scores"]