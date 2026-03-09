from pymongo import MongoClient
from db_init import collection_heroes, collection_monsters, collection_scores

# Menu principal proposant de démarrer, afficher le classement ou quitter le jeu
def display_main_menu():
    print("=== Bienvenue dans le jeu d'expédition ! ===")
    print("=== Menu principal ===")
    print("1. Démarrer une nouvelle expédition\n 2. Afficher le classement\n 3. Quitter le jeu")

def is_valid_number(saisi, min_val, max_val):
    if not saisi.isnumeric():
        return False
    if int(saisi) < min_val :
        return False
    if int(saisi) > max_val :
        return False
    return True



def get_valid_number(saisi, min_val, max_val, message):
    # Boucle tant que saisi invalide
    while True :
        # Entrer une valeur
        user_choice = is_valid_number(saisi)
        # valeur invalide (<min ou >max) alors mess erreur
        if user_choice < min_val :
            message
        
        if user_choice > max_val :
            message
        # valeur valide (entre le min et le max) alors on renvoie
        else :
            return True