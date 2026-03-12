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
            exit()

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
        # Afficher tous les héros disponibles
        show_heroes(heroes_avail_list)       
        # Choisir un héros en saisissant son numéro
        choose_heroes = heroes_avail_list[get_valid_number(0, 9, "Veuillez saisir le numéro du héros que vous souhaitez :")]
        # Enlever le héros choisi de la liste des héros disponibles
        heroes_avail_list.remove(choose_heroes)
        # Ajouter le héros choisi dans l'équipe
        team.append(choose_heroes)
        # Afficher l'équipe pour vérifier que le héros a bien été ajouté dans l'équipe
        print("Voici votre équipe :", team)


def get_heroes_db():
    # Liste vide des héros
    heroes_list = []
    # Chercher les héros dans la db 
    heroes = collection_heroes.find({}, {"NAME":1, "ATK":1, "DEF":1, "HP":1, "_id":0})
    # pour chaque entree ajouter à la liste des heros
    for entree in heroes:
        heroes_list.append(entree)
    # Retourner la liste des héros
    return heroes_list


def show_heroes(heroes):
    # Numéroté les héros avec une variable
    n = 0
    # Créer une boucle qui va lister un par un tous les héros avec leurs informations
    for i in heroes :
        # Afficher les héros
        print(f"{n}. Name : {i["NAME"]}, ATK : {i["ATK"]}, DEF : {i["DEF"]}, HP : {i["HP"]}\n ")
        # Augmente la valeur de la variable pour numéroté le héros suivant
        n = n + 1


def launch_fight():
    # Afficher que l'expédition commence
    print("======== L'expédition commence ! ========")
    # Générer aléatoirement depuis la db un monstre à affronter avec ses stats affichées
    generate_random_monster = get_monsters
    # Fonctionnement du jeu en tour par tour
    # Le jeu commence vague 0
    # Tant que la valeur des PV des 3 héros ou du monstre n'est pas 0 alors le jeu continue
    # Tour des héros: les héros attaque le monstre
    # Réduction des PV du monstre en fonction de l'ATK des héros et de la DEF du monstre
    # Tour du monstre : le monstre attaque aléatoirement unn héros
    # Réduction des PV du héros attaqué en fonction de l'ATK du monstre et de la DEF du monstre
    # Si les PV du monstre atteignent 0 alors les héros ont gagné
    # Incrémentation de 1 des vague
    # Nouveau monstre généré aléatoirement
    # Les héros gardent les PV de la partie précédente il n'y a donc pas de récupération
    # Dans le cas contraire si les PV de tous les héros atteignent 0
    # Arrêt du jeu et sauvegarde des vagues


def get_monsters_db():
    # Liste vide des monstres
    monsters_list = []
    # Chercher les monstres dans la db 
    monsters = collection_monsters.find({}, {"NAME":1, "ATK":1, "DEF":1, "HP":1, "_id":0})
    # pour chaque entree ajouter à la liste des monstres
    for entree in monsters:
        monsters_list.append(entree)
    # Retourner la liste des monstres
    return monsters_list


def random_monster(monsters):
    # Choisir un monstre aléatoirement avec ses informations


#main()