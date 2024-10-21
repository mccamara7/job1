#début job1
fruits=['pomme', 'cerise', 'orange']
print(fruits)
#fin job1

#début job2
fruits=['pomme', 'cerise', 'orange']
print(fruits[1])
#fin job2

#début job3
fruits=['pomme','cerise','orange']
fruits.append('melon')
print(fruits)
#fin job3

#début job4
fruits=['pomme','cerise','orange','melon']
fruits.insert(2,'mangue') 
print(fruits)
#fin job5

#début job5
l=[1,2,3,4,5]
print(l) 
print(l[1])

l[3]= l[2] + l[4]

new_value = l[2] + l[4]
l[3] = new_value
print(l)
print(l[-1])
#fin job5

#début job6
l=[1,2,3,4,5]
print(l)

l[0], l[-1] = l[-1], l[0]
print(l)
#fin job6

#début job7 (multiple de 3)
l=[8,24,48,2,12]
print(l)
n=0
for nombre in l:
    if (nombre%3==0):
        n+=n
        print("l:", nombre)
#fin job7

#début job8 (la somme des valeurs paires)
l=[8,24,27,48,2,16,9,84,91]
print(l)
n= 0
for nombre in l:
    if nombre % 2 == 0:
        n += nombre  
        print("l :", n)
#fin job8

#début job9
l=[8,24,27,48,2,16,9,102,7,84,91]
valeur_max=('valeur max()')
valeur_min=('valeur min()')
print('valeur max() est: 102')
print('valeur min() est :2')
#fin de job9

#début job 10
l=[8,24,27,48,2,16,9,102,7,84,91]
produit= len(l)
#produit des valeurs de [25, 90]
p=1
for i in range(0, produit):
    if 25<= l[i] <=90:
        p=p*l[i]
        print("produit des valeurs comprise entre 25 et 90 :", p)
#fin job 10

#début job 11
l=[7,11,42,39,2]
p=len(l)
#ajout de 1 à chaque valeur de l
for i in range (0, p ):
    l[i]=l[i]+1
    print("l modifiée par ajout de 1:", l)
#fin job 11

#début job 12
def tri_bulle(liste):
    n = len(liste)
  # Traverse tous les éléments de la liste
    for i in range(n):
     for j in range(0, n-i-1):
      # Compare les éléments adjacents
      if liste[j] > liste[j+1] :
        # Échange les éléments
        liste[j], liste[j+1] = liste[j+1], liste[j]

ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri_bulle(ma_liste)
print("Liste triée:", ma_liste)
#fin job 12

#début job 13
l=[10,20,30,20,10,50,60,40,80,50,40]
def supprimer_doublons(l):
     resultat = [10,20,30,50,60,40,80]
     for element in l:
      if element not in resultat:
       resultat.append(element)
     return resultat
 
liste_sans_doublons = supprimer_doublons(l)
print("Liste sans doublons :", liste_sans_doublons)
    
    
    
    

    
        

    


