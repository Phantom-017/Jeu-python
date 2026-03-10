from pymongo import MongoClient
from db_init import db, collection_heroes, collection_monsters, collection_scores

# Menu principal proposant de démarrer, afficher le classement ou quitter le jeu
def display_main_menu():
    print("=== Bienvenue dans le jeu d'expédition ! ===")
    print("============= Menu principal =============")
    print(" 1. Démarrer une nouvelle expédition\n 2. Afficher le classement\n 3. Quitter le jeu")

def is_valid_number(saisie,max_val,min_val):
    # On vérifie si la saisie n'est pas un chiffre
    if not saisie.isnumeric():
        return False
    # On vérifie si la saisie est supérieure à la valeur maximale
    if int(saisie) > max_val:
        return False
    # On vérifie si la saisie est inférieure à la valeur minimale
    if int(saisie) < min_val:
        return False
    return True 


def get_valid_number(min_val,max_val,message):
    # Faire une boucle jusqu'à ce que l'utilisateur entre un nombre valide
    while True:
        # On affiche un message qui demande de saisir un nombre
        print(message)
        # On saisi une valeur
        saisie = input()
        # On vérifie si la valeur correspond aux critères
        if is_valid_number(saisie,max_val,min_val):
            # Si c'est correct, on retourne la valeur
            return saisie        
        else:
            # Sinon on affiche un message d'erreur
            print("Saisie incorrect.")

       
def main_menu():
    # On affiche le menu principal du jeu
    display_main_menu()
    # On récupère la valeur valide que l'utilisateur a choisi
    user_choice = get_valid_number(1, 3, "Veuillez saisir un nombre entre 1 et 3 :")
    # Si la valeur est 1 alors le jeu commence
    if user_choice == 1 :
        start_game()
    # Si la valeur est 2 alors on affiche le tableau des scores
    if user_choice == 2 :
        leaderboard()
    # Si la valeur est 3 alors on arrête le programme
    if user_choice == 3 :
        quit

def leaderboard():
    # Numéroté le classement des joueurs avec une variable
    p = 1
    # On trouve les scores et les stockes
    score = collection_scores.find()
    # Une boucle qui s'arrête aux 3 meilleurs scores avec le username et son score
    for i in score[:3]:
        print(f"#{p} Player : {i["USERNAME"]} -> Score : {i["SCORE"]}")
        # Augmente la valeur de la variable pour numéroté le joueur suivant
        p = p + 1

def start_game():
    # Entrer un username
    username = input()
    print(username)
    # Créer son équipe
    create_team()
    # Lancement du combat automatisé
    launch_fight()

def create_team():
    # Créer une équipe vide
    team = []
    # Choisir 3 héros pour compléter le trio à l'aide d'une boucle
    for i in range(3):
        # Afficher tous les héros disponibles
        show_heroes()
        # Choisir les héros
        choose_heroes = get_heroes()
        # Ajouter le héros choisi dans l'équipe vide
        team.append(choose_heroes)
        # Enlever le héros choisi de la liste des héros disponibles

    # Afficher l'équipe
    print(team)


def show_heroes():
    # Liste vide des héros
    heroes_list = []
    # Numéroté les héros avec un variable
    n = 1
    # Trouver les héros dans la base
    heroes = collection_heroes.find()
    # Créer une boucle qui va lister un par un tous les héros avec leurs informations
    for i in heroes :
        # Afficher les héros
        #print(f"{n}. Name : {i["NAME"]}, ATK : {i["ATK"]}, DEF : {i["DEF"]}, HP : {i["HP"]}\n ")
        # Stocker les héros
        heroes_list.append(heroes)
        print(heroes_list)
        # Augmente la valeur de la variable pour numéroté le héros suivant
        n = n + 1

#def get_heroes():

#def launch_fight():

show_heroes()