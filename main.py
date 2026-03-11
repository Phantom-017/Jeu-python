from pymongo import MongoClient
from db_init import db, collection_heroes, collection_monsters, collection_scores

# Menu principal proposant de démarrer, afficher le classement ou quitter le jeu
def show_main_menu():
    print("=== Bienvenue dans le jeu d'expédition ! ===")
    print("============= Menu principal =============")
    print(" 1. Démarrer une nouvelle expédition\n 2. Afficher le classement\n 3. Quitter le jeu")

def is_valid_number(min_val, max_val, saisie):
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


def get_valid_number(min_val, max_val, message):
    # Faire une boucle jusqu'à ce que l'utilisateur entre un nombre valide
    while True:
        # On affiche un message qui demande de saisir un nombre
        print(message)
        # On saisi une valeur
        saisie = input()
        # On vérifie si la valeur correspond aux critères
        if is_valid_number(min_val, max_val, saisie):
            # Si c'est correct, on retourne la valeur
            return int(saisie)
        else:
            # Sinon on affiche un message d'erreur
            print("Saisie incorrect.")

       
def main():

        # On affiche le menu principal du jeu
        show_main_menu()
        # On récupère la valeur valide que l'utilisateur a choisi
        user_choice = get_valid_number(1, 3, "Veuillez saisir un nombre entre 1 et 3 :")
        # Si la valeur est 1 alors le jeu commence
        if user_choice == 1 :
            start_game()
        # Si la valeur est 2 alors on affiche le tableau des scores
        if user_choice == 2 :
            show_leaderboard()
        # Si la valeur est 3 alors on arrête le programme
        if user_choice == 3 :
            quit()

def show_leaderboard():
    # Numéroté le classement des joueurs avec une variable
    p = 1
    # On trouve les scores
    score = collection_scores.find()
    # Une boucle qui s'arrête aux 3 meilleurs scores avec le username et son score
    for i in score[:3]:
        print(f"#{p} Player : {i["USERNAME"]} -> Score : {i["SCORE"]}")
        # Augmente la valeur de la variable pour numéroté le joueur suivant
        p = p + 1

def quit():
    while True:
        break

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
    # Chercher la liste des heros dispos
    heroes_avail_list = get_heroes_db()
    # Choisir 3 héros pour compléter le trio à l'aide d'une boucle
    for i in range(3):
        # Message informant la saisi du numéro d'un héros à choisir
        print("Choisissez un héros en saisissant son numéro :\n")
        # Afficher tous les héros disponibles
        show_heroes(heroes_avail_list)
        # Choisir un héros en saisissant son numéro
        choose_heroes = get_heroes_db()
        # Ajouter le héros choisi dans l'équipe
        team.append(choose_heroes)
        # Enlever le héros choisi de la liste des héros disponibles
        choose_heroes.remove()
    # Afficher l'équipe
    print(team)


def get_heroes_db():
    heroes_list = []
    # chercher les heros dans la db 
    heroes = collection_heroes.find()
    # pour chaque entree ajouter a la liste des heros
    for entree in heroes:
        heroes_list.append(entree)
    return heroes_list


def show_heroes(heroes):
    # Liste vide des héros
    # Numéroté les héros avec une variable
    n = 1
    # Trouver les héros dans la base
    # Créer une boucle qui va lister un par un tous les héros avec leurs informations
    for i in heroes :
        # Afficher les héros
        print(f"{n}. Name : {i["NAME"]}, ATK : {i["ATK"]}, DEF : {i["DEF"]}, HP : {i["HP"]}\n ")
        #print(heroes_list)
        # Augmente la valeur de la variable pour numéroté le héros suivant
        n = n + 1


#heroes_avail_list = get_heroes_db()

#show_heroes(heroes_avail_list)

create_team()

#main()