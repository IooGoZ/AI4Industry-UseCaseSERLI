# Ce code utilise [ Sam 2 ](https://github.com/facebookresearch/sam2?tab=readme-ov-file) pour segmenter la piste sur les images provenant d'une go-pro karting. 

## Installation :

Pour se faire il faut d'abord cloner le projet sam 2 : 
> git clone https://github.com/facebookresearch/sam2.git

Ensuite créer un environnement python avec les bibliotèques nécessaire. La liste est disponible directement sur le dépot git de Sam 2.

Avant de continuer assurez vous que Sam 2 et ses dépendances sont correctement installé. 

## Utilisation :

Pour lancer notre programme il vous faudra mettre en place votre dataset et changer le chemin des fichiers dans **our_samprog.ipynb**. Les images du dataset devront être sous le format jpeg.

Le dataset est une vidéo décrit sous la forme d'une liste d'image jpeg.
<img width="564" alt="segmentationsam" src="https://github.com/user-attachments/assets/99bdfbe0-ce6e-42c2-a48a-46b4a3ca998f" />

Dans **our_samprog.ipynb**, il faut modifier cette ligne pour placer le point qui permettra de segmenter la forme pointé sur la premiere image : 
> points = np.array([[550, 200]], dtype=np.float32)

Suite à cela, le prompt sera propager sur les prochaines images de votre 

Si ce n'est pas le cas, le notebook **modify_images.ipynb** vous permettra de convertir et renommer les images png en jpeg. 

### Empreinte carbonne 

On a utilisé la bibliotèque **codecarbon** qui nous permet de mesurer l'émission de CO~2~ lors de l'éxécution de notre script.

> pip install **codecarbon**

L'empreinte carbonne lors de l'execution de notre code sur 1440 frames est de :
```
Somme des émissions de CO₂ générées : 0.001215 kg
```
le temps d'execution est de : 
```
Somme du temps d'exécution : 295.6 secondes
```

## Convertisseur png to jpeg :

Pour convertir l'ensemble des fichiers png en jpeg dans le dossier courant, lancer la fonction **create_jpeg_images** depuis le notebook **modify_images.ipynb** 

**rename_files_to_fix_sorting** permet de renommer les fichiers afin de pouvoir les utiliser dans le notebook **our_samprog.ipynb**.

Les fonctions **compress_images** et **split_files_into_parts** sont à utilisées pour réduire le temps d'execution de SAM2. Ces dernières permettent de compresser les images en format 480*848 et de les séparer en différents sous-dossiers.




