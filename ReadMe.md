#### AI4INDUSTRY - SERLI 

### Groupe Rouge : Boireau Tom, Rambolatahiana Tsinjoaribenja Mario, Mathieu Théo, Caby Bruno, Proust Léna

## Approche Segmentation : 

# Approche : 
Détecter les objets dans l’image et reconnaitre dans que virage/endroit de la piste on est à partir des positions des bâtiments (open street view) 
Outils : OpenCV ou Meta SAM 2

# Travail réalisé : 

- Jour 1 : 

    Approche avec Meta SAM 2 : 
    Grosses difficultés pour l’installer et il faut un GPU pour l’utiliser donc approche qui sera probablement abandonnée. 

    Approche avec OpenCV : 
    Lien : https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html

    Résultat obtenu : segmented_image.png

- Jour 2 : 

    Approche avec Meta SAM 2 : 
    Installation de SAM2 finalisée, test de base avant de voir comment l’utiliser pour le sujet
    On pense se focaliser sur la route via la vidéo pour essayer de savoir où se trouve le kart, voir comment mettre les points pour être sûr de ne détecter que le route et rien de plus (surement 2/3 points vers le centre de l’écran)
    Résultat obtenu avec SAM2 sur une image en appliquant des masques automatiquements.

    Résultat obtenu : sam2_result.png

    Approche avec OpenCV : 
    Test avec GrabCut (plus interactif et adapté à la segmentation spécifique à un objet qu’open cv). Le résultat est mieux que l’algorithme de watershed mais c’est très très long donc abandon de cet algorithme. 

- Jour 3 : 

    Abandon de l’algorithme de watershed pour la segmentation car on obtient de meilleurs résultats avec SAM 2. 

    Conversion du dataset de png à jpeg. 

    Segmentation effectuée avec SAM 2 qui sort des masques de la route sur l’ensemble de la vidéo. On applique en plus un masque afin de cacher le kart et le ciel, pour minimiser les risques d’erreurs. Resize des images pour réduire le temps d’execution
    Maintenant, conception du modèle de convolution permettant de déterminer la position de la caméra par rapport à la courbure de la route. 

    Ensuite, nous avons créé un modèle de convolution CNN léger que nous devons tester et entrainer avec les données (images) récupérées grâce à SAM 2. 

- Jour 4 :
    Conversion de tableaux en images exploitables pour l’entrainement
    Fonction d’erreur utilisée : MSE (mean square error) 
    Entrainement du modèle 
    Ajout des fonctions d,ne tracking Code Carbon 
    Récupération du dataset complet 
    -> ça ne marche pas sur ce dataset, on ne sait pas vraiment pourquoi. Les images sont bien compressées en 480x848 mais celles en sortie sont en 1080x1920 et la segmentation ne fonctionne pas sur la route, les points semblent être décalés lors de la segmentation
    Après avoir modifié les hypers paramètres plusieurs fois et fait plusieurs entrainements de modèle, notre meilleur résultat est de 31%. Il semblerait donc que notre méthode de segmentation ne soit pas la meilleure pour résoudre ce problème. 

- Jour 5 :
      Présentation : comment l’utilisateur va s’en servir et pourquoi : utile pour pilote/ingénieur de course pour voir où sont ses erreurs et ainsi les corriger 
