"""
############
# rsyncFTP #
############
# parser   #
############

@author: Julien Vermeil and Vincent Reynaert and Nicolas Sobczak
"""

# TODO : Tester la fonction logArgs, mettre a jour les commentaires et exemples
# %%__________________________________________________________________________________________________
# Config

# Import
import logger
import argparse

test = 0


# %%__________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Fonctions d'initialisation
def initVariables():
    """
    Fonction qui initialise le logger et les variables en fonction de ce que
    l'utilisateur a entre.
    La fonction genere une info recapitulant la liste des parametres entres.
    :return: ARGS
    :rtype: dict
    """
    # initialisation du argparse
    PARSER = argparse.ArgumentParser(description='Dossier miroir avec "rsyncFTP"\n')

    # obligatoire
    PARSER.add_argument("ftp", type=str, nargs=3,
                        help="(hote, identifiant, mot_de_passe) :\n" + \
                             "donnees pour le site FTP distant: hote, identifiant, mot de passe" + \
                             "ex : localhost nsobczak ISEN")
    PARSER.add_argument("dp", type=str, help="chemin vers le dossier local")
    PARSER.add_argument("ie", type=str, nargs=2,
                        help="liste des fichiers à inclure puis celle à exclure, "
                             "* pour tout selectionner, ',' pour séparer les extensions"
                             "ex : * .odt,.docx pour dire de tout inclure sauf les .odt et .docx")

    # optionnel
    PARSER.add_argument("-lp", "--logPath", default="",
                        help="chemin ou generer le fichier log")
    PARSER.add_argument("-lc", "--logConf", default="rsyncFTP.conf",
                        help="chemin vers le fichier conf du log (gestion des handler)")
    PARSER.add_argument("-p", "--profondeur", default=5,
                        help="profondeur de la supervision du dossier, default = 2")
    PARSER.add_argument("-sf", "--sizeFile", default=500,
                        help="taille maximale des fichiers transferes en Mo, default = 500 Mo")
    PARSER.add_argument("-f", "--frequence", default=1,
                        help="frequence de supervision en s, default = 1 s")
    PARSER.add_argument("-st", "--supervisionTime", default=-1,
                        help="temps de supervision en s, -1 pour infini, default = infinite")

    # affichage des arguments rentres dans le log
    ARGS = PARSER.parse_args()

    return ARGS


# %%__________________________________________________________________________________________________
# Fonctions de log
def logArgs(args, logger):
    """
    Procedure qui ecrit les parametres utilises dans le logger
    :param args: parametres entres en lignes de commandes
    :type args: dict
    """
    logger.info(
        ":\n(hote, identifiant, mot_de_passe) " + \
        "donnees pour le site FTP distant: %s \n" + \
        "chemin vers le dossier local: %s \n" + \
        "chemin pour generer le log: %s \n" + \
        "2-uple contenant :\n" +
        "-la liste de fichiers a inclure (les extensions): %s \n" + \
        "-la liste de fichiers a inclure (les extensions): %s \n" + \
        "chemin vers le fichier conf du log (gestion des handler): %s \n" + \
        "profondeur de la supervision du dossier: %d \n" + \
        "taille maximale des fichiers transferes en Mo: %d \n" + \
        "frequence de supervision en s: %d \n" + \
        "temps de supervision en s: %d \n",
        args.ftp, args.dp, args.logPath, str(args.ie[0]), str(args.ie[1]),
        args.logConf, args.profondeur, args.sizeFile, args.frequence,
        args.supervisionTime
    )


# %%__________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Tests unitaires
def monMain():
    ARGS = initVariables()
    MAIN_LOGGER = logger.initLog(ARGS.logPath, ARGS.logConf)
    print(ARGS)


if __name__ == "__main__":
    monMain()
