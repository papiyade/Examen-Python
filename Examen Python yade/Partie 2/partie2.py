
# 2) On souhaite écrire une fonction récursive prenant en paramètres deux valeurs , a un réel et b un entier, et retournant la valeur réelle x.
# a) Quel(s) critère(s) d'arret proposez-vous?
# b)Ecrivez la fonction
# c)Combien y a t-il d'appels récursifs pour a=2 et b=3? Décrivez les apels récursifs dans ce cas.

#L'expression récursive 
  # a)         1+divinRec(a-b,b)


#Pour le critére d'arret il faut que a soit inferieur à  b

# b) La fonction récursive
def divinRec(a, b):
    if a < b:
        return 0
    else:
        return 1 + divinRec(a - b, b)
    

# 2)a) Critère d'arret
# b == 0
# 2)b) la fonction
def puissance(a, b):
    if b == 0:
        return 1.0
    else:
        return a * puissance(a, b - 1)
#Il doit y avoir 4 appels à savoir les puissances (2,3) , (2,2) , (2,1) ,(2,0)
#graphiquement cela doit ressembler à
# puissance(2,3) -> puissance(2,2) -> puissance(2,1) -> puissance(2,0) en descendant par puissance 





