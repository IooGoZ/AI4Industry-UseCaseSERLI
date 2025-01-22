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


- Jour 4 (à faire) :
  Entrainer le modèle conçu au j3 avec les données récupérées au j3.
  Réfléchir présentation + rapport.