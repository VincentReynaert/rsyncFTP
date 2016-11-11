############
# rsyncFTP #
############

# TODO : se connecter au serveur, synchroniser le serveur
# ____________________________________________________________________________________________________
# Config

# Import
from ftplib import FTP
import os
import os.path


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Fonctions
def connectionAuServeurFTP(host, user, password):
    """
    Fonction qui initialise la connection au serveur FTP distant
    :param host: host name
    :type host: str
    :param user: user id
    :type user: str
    :param password: password
    :type password: str
    """
    ftp = FTP(host, user, password)  # on se connecte
    return ftp


def deconnexionAuServeur(connect):
    """
    Fonction qui se deconnecte du serveur
    :param connect: nom de la variable dans laquelle la connexion a ete declaree
    :type connect: ???
    """
    connect.quit()


def affichageFTP(ftp):
    """
    Fonction qui affiche ???
    :param ftp: ???
    :type ftp: ???
    """
    print(FTP.dir(ftp))


def envoyerUnFichier(fichier_chemin, fichier_nom, ftp):
    """
    Fonction qui envoie un fichier
    :param ftp: ???
    :type ftp: ???
    """
    # ouverture du fichier
    file = open(fichier_chemin, 'rb')
    # fichier a envoyer
    ftp.storbinary('STOR ' + fichier_nom, file)
    # fermeture du fichier
    file.close()


def etatConnexion(ftp):
    """
    Fonction qui ???
    :param ftp: ???
    :type ftp: ???
    """
    etat = ftp.getwelcome()  # grâce à la fonction getwelcome(), on récupère le "message de bienvenue"
    print("Etat : ", etat)


def effacerFichier(ftp, fichier):
    """
    Fonction qui ???
    :param ftp: ???
    :type ftp: ???
    :param fichier: ???
    :type fichier: ???
    """
    ftp.delete(fichier)


def creerDossier(ftp, nom_dossier, chemin_dossier):
    """
    Fonction qui cree un dossier spécifié par chemin dans le ftp
    :param ftp: ???
    :type ftp: ???
    :param dossier: ???
    :type dossier: ???
    """
    ftp.cwd(chemin_dossier)
    ftp.mkd(nom_dossier)
    ftp.cwd('..')

def supprimerDossier(ftp, dossier):
    """
    Fonction qui supprime un dossier
    :param ftp: ???
    :type ftp: ???
    :param dossier: ???
    :type dossier: ???
    """
    ftp.rmd(dossier)


def lister(ftp):
    """
    Fonction qui ???
    :param ftp: ???
    :type ftp: ???
    """
    rep = ftp.dir()  # on récupère le listing
    print(rep)  # on l'affiche dans la console

def listerFichiers(ftp):
    ret = []
    ftp.dir("", ret.append)
    ret = [x.split()[-1] for x in ret if x.startswith("d")]
    return ret

def copierContenuDossier(ftp, chemin, nom_dossier):
    """
    Fonction qui copie les fichiers d'un dossier spécifié
    :param ftp: serveur ftp
    :type ftp:
    :param chemin: chemin complet du dossier
    :type chemin: str
    :param nom_dossier: nom du dossier
    :type nom_dossier: str
    """
    liste = listerFichiers(ftp)
    print(liste)
    for i in liste:
        if (nom_dossier == i):
            return 1
    chemin_ftp = "/"
    creerDossier(ftp, nom_dossier, chemin_ftp)
    ftp.cwd(nom_dossier)
    l = os.listdir(chemin)
    print(l)
    for i in l:
        fichier = os.path.join(chemin, i)
        print(fichier)
        # dossierFTP  = os.path.join(ftp,nom_dossier)
        envoyerUnFichier(fichier, i, ftp)
    ftp.cwd('..')
    #envoyerUnFichier(fichier, i, ftp)


def pushAuServeurFTP():
    """
    Fonction qui push les donnees vers le serveur FTP distant
    """
    return 1


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Test unitaire

def monMain():
    ### Variables

    host = "localhost"  # adresse du serveur FTP
    user = "root"  # votre identifiant
    password = "tomtom"  # votre mot de passe

    directory = os.getcwd()  # "C:\Users\ISEN\Desktop\COURS\M1\Python\PycharmProjects\Projects\rsyncFTP"
    filename1 = "texte.txt"
    fichier1 = os.path.join(directory, filename1)

    nom_dossier = "test"
    chemin = os.path.join(directory, nom_dossier)

    ### Tests des Fonctions

    ftp = connectionAuServeurFTP(host, user, password)
    chemin1 = "test"
    nom_dossier1 = "test2.1"
    # affichageFTP(ftp)
    # envoyerUnFichier(fichier1, filename1, ftp)
    # etatConnexion(ftp)
    #effacerFichier(ftp, filename2)
    #creerDossier(ftp, nom_dossier1, chemin1)
    #supprimerDossier(ftp, dossier)
    #lister(ftp)
    copierContenuDossier(ftp, chemin, nom_dossier)
    print(listerFichiers(ftp))
    deconnexionAuServeur(ftp)


if __name__ == "__main__":
    monMain()
