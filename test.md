# Comparaison expérimentale

## A* : 
    - 0.006 secondes de moyenne en 3x3
    - 1 seconde à plusieurs dizaine de minutes en 4x4, seule algorithme ayant déjà donné une solution

## BFS :
    - Plusieurs dizaines de minutes minimum ou mémoire saturée avant d'avoir la solution en 3x3 sans prévention de boucles
    - 0.4 secondes de moyenne en 3x3 avec prévention de boucles
    - Jamais trouvé de résultat en 4x4 (avec ou sans prévention de boucles), mémoire saturée trop tôt

## DFS :
    - Reste bloqué sans prévention de boucles
    - 0.3 secondes de moyenne en 3x3 avec prévention de boucles
    - Jamais trouvé de résultat en 4x4 (avec ou sans prévention de booucles), mémoire saturée trop tôt