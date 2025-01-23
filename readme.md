# Ce code utilise [ Sam 2 ](https://github.com/facebookresearch/sam2?tab=readme-ov-file) pour segmenter la piste sur les images provenant d'une go-pro karting. 

## Installation :

Pour se faire il faut d'abord cloner le projet sam 2 : 
> git clone https://github.com/facebookresearch/sam2.git

Ensuite créer un environnement python avec les bibliotèques nécessaire. La liste est disponible directement sur le dépot git de Sam 2.

Avant de continuer assurez vous que Sam 2 et ses dépendances sont correctement installé. 

## Utilisation :

Pour lancer notre programme il vous faudra mettre en place votre dataset et changer le chemin des fichiers dans **our_samprog.ipynb**. Les images du dataset devront être sous le format jpeg.

Le dataset est une vidéo décrit sous la forme d'une liste d'image jpeg.

Dans **our_samprog.ipynb**, il faut modifier cette ligne pour placer le point qui permettra de segmenter la forme pointé sur la premiere image : 
> points = np.array([[550, 200]], dtype=np.float32)

Suite à cela, le prompt sera propager sur les prochaines images de votre 

Si ce n'est pas le cas, le notebook **modify_images.ipynb** vous permettra de convertir et renommer les images png en jpeg. 

### Empreinte carbonne 

On a utilisé la bibliotèque **codecarbon** qui nous permet de mesurer l'émission de CO~2~ lors de l'éxécution de notre script.

> pip install **codecarbon**

L'empreinte carbonne lors de l'execution de notre code est disponible dans le fichier 

## Convertisseur png to jpeg :






