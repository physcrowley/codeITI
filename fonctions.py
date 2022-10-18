""" Ici mes fonctions que je veux utiliser partout """

def super_cool():
    """ Sans paramètre, sans valeur de retour"""
    print("WoW!!!!!")

def returnConstant():
    """ Sans paramètre avec valeur de retour """
    return 3.141592653

def somme(a, b):
    """ Avec paramètres et valeur de retour
    int a - première valeur
    int b - deuxième valeur
    returns - la somme de a + b 
    """
    return a + b

def hello( name ):
    """ Avec paramètre sans valeur de retour """
    print("Hello", name)

# pour tester le code dans ce fichier sans qu'il se lance
# dans les autres fichiers qui importe ce module
if __name__ == "__main__" :
    super_cool()