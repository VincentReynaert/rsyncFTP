# rsyncFTP

Programme qui synchronise un dossier local de notre machine vers un site miroir ftp distant

## parametres

|Paramètre|Type|Variable|
|---|---|---|
|donnees pour le site FTP distant: hote, identifiant, mot de passe \| ex : localhost nsobczak ISEN|obligatoire|ftp|
|chemin vers le dossier local (directory path)|obligatoire|dp|
|liste des fichiers à inclure puis celle à exclure, * pour tout selectionner, ',' pour séparer les extensions \| ex : * .odt,.docx pour dire de tout inclure sauf les .odt et .docx|obligatoire|ie|
|chemin ou generer le fichier log|optionnel|"--lp", "--logPath"|
|chemin vers le fichier conf du log (gestion des handler)|optionnel|"-lc", "--logConf"|
|profondeur de la supervision du dossier, default = 2|optionnel|"-p", "--profondeur"|
|taille maximale des fichiers transferes en Mo, default = 500 Mo|optionnel|"-sf","--sizeFile"|
|frequence de supervision en s, default = 1 s|optionnel|"-f", "--frequence"|
|temps de supervision en s, -1 pour infini, default = 60 sec|optionnel|"-st", "--supervisionTime"|


commande linux = rsync


## Note explicative

- auteurs
- Si librairie supplémentaire => installable par pip
- choix techniques
- choix d'organisation

