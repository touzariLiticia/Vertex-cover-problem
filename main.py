#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJEDDAL HANANE 3803192
TOUZARI LITICIA 3802643
Binome 4
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import implementation as imp
import tests as test

#=============TESTS OPERATIONS DE BASE
"""
g = imp.creer_graphe('exempleinstance1.txt')
print(imp.supprimer_sommet(g,'0'))
print(g)
print(imp.supprimer_ens_sommet(g,['0','1','2','8']))
print(g)   
print(imp.get_degre(g))
print(imp.get_degre_max(g))
"""

#=============TESTS GENERATION DE GRAPHE
"""
g=imp.gen_graphe(20,0.5)
print("graphe :",g)
"""

#=============TESTS METHODES APPROCHEES
"""
print("glouton ",imp.glouton(g))
print("couplage ",imp.couplage(g))
"""
#========test_couplage
"""
x,y,xl,yl=test.test_couplage(100,0.5)
test.affichage_n_t(x,y,"Couplage")
test.affichage_n_logt(x,yl,"Couplage")
test.affichage_logn_logt(xl,yl,"Couplage")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(xl[i+1]-xl[i])
print("pente : ",p/(len(xl)-1)) 
"""
#========test_glouton
"""
x,y,xl,yl=test.test_glouton(100,0.5)
test.affichage_n_t(x,y,"Glouton")
test.affichage_n_logt(x,yl,"Glouton")
test.affichage_logn_logt(xl,yl,"Glouton")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(xl[i+1]-xl[i])
print("pente : ",p/(len(xl)-1))  
"""
#========test_couplage
"""
x,y,xl,yl=test.test_couplage_p(100)
test.affichage_p_t(x,y,"Couplage")
test.affichage_p_logt(x,yl,"Couplage")
test.affichage_logp_logt(xl,yl,"Couplage")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(xl[i+1]-xl[i])
print("pente : ",p/(len(xl)-1)) 
"""
#========test_glouton
"""
x,y,xl,yl=test.test_glouton_p(100)
test.affichage_p_t(x,y,"Glouton")
test.affichage_p_logt(x,yl,"Glouton")
test.affichage_logp_logt(xl,yl,"Glouton")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(xl[i+1]-xl[i])
print("pente : ",p/(len(xl)-1)) 

"""

#========Comparaison couplage glouton

"""
x,y1,y2=test.compare_couplage_glouton(20,0.5)
test.affichage_bar(x,y2,y1,"Comparaison Couplage-Glouton")
"""

#========Ecarts couplage glouton
"""
x,y=test.ecart_couplage_glouton(20,0.5)
test.affichage_ecart(x,y,"Ecart Couplage-Glouton")
"""
#=============TESTS OPERATIONS DE BRANCHEMENT
#====================Branchement simple
"""
x,y,xl,yl=test.test_branch(10,0.5)
test.affichage_n_t(x,y)
test.affichage_n_logt(x,yl)
test.affichage_logn_logt(xl,yl)


x,y,xl,yl=test.test_branch_p(20)
test.affichage_p_t(x,y)
test.affichage_p_logt(x,yl)
test.affichage_logp_logt(xl,yl)
"""
#==================Branchement avec bornes
"""
print(imp.branch_born(g))
print(imp.branch_born_glouton(g))
print(imp.branch_born_brut(g))
"""
#================test branch_born

"""
x,y,xl,yl=test.test_branch_born(20,0.5)
test.affichage_n_t(x,y,"Branch_born")
test.affichage_n_logt(x,yl,"Branch_born")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(x[i+1]-x[i])
print("pente : ",math.exp(p/(len(xl)-1))) # complexité O((1.6)^n)
"""
#================test branch_born_glouton
"""
x,y,xl,yl=test.test_branch_born_glouton(20,0.5)
test.affichage_n_t(x,y,"Branch_born_glouton")
test.affichage_n_logt(x,yl,"Branch_born_glouton")

p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(x[i+1]-x[i])
print("pente : ",math.exp(p/(len(xl)-1))) # complexité O((1.8)^n)
"""
#================test branch_born_brute
"""
x,y,xl,yl=test.test_branch_born_brut(20,0.5)
test.affichage_n_t(x,y,"Branch_born_brut")
test.affichage_n_logt(x,yl,"Branch_born_brut")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(x[i+1]-x[i])
print("pente : ",math.exp(p/(len(xl)-1))) # complexité O((1.7)^n)

test.Comparaison_branch_born(20,0.5)
"""
#====================Branchement avec bornes

"""
print(imp.branch_born_ameliore1(g))
print(imp.branch_born_ameliore2(g))
print(imp.branch_born_ameliore3(g))
"""

#========test_branch_born_ameliore1
"""
x,y,xl,yl=test.test_branch_born_ameliore1(30,0.5)
test.affichage_n_t(x,y,"Branchement amélioré 1")
test.affichage_n_logt(x,yl,"Branchement amélioré 1")
test.affichage_logn_logt(xl,yl,"Branchement amélioré 1")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(xl[i+1]-xl[i])
print("pente : ",p/(len(xl)-1)) # en moyenne 3
"""
#========test_branch_born_ameliore2
"""
x,y,xl,yl=test.test_branch_born_ameliore2(30,0.5)
test.affichage_n_t(x,y,"Branchement amélioré 2")
test.affichage_n_logt(x,yl,"Branchement amélioré 2")
test.affichage_logn_logt(xl,yl,"Branchement amélioré 2")

p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(xl[i+1]-xl[i])
print("pente : ",p/(len(xl)-1)) # en moyenne 2.8
"""
#========test_branch_born_ameliore3
"""
x,y,xl,yl=test.test_branch_born_ameliore3(30,0.5)
test.affichage_n_t(x,y,"Branchement amélioré 3")
test.affichage_n_logt(x,yl,"Branchement amélioré 3")
test.affichage_logn_logt(xl,yl,"Branchement amélioré 3")
p=0
for i in range(len(xl)-1):
    p+=(yl[i+1]-yl[i])/(xl[i+1]-xl[i])
print("pente : ",p/(len(xl)-1)) # en moyenne 2.8, 2.7

"""

#========Rapport d'approximation
"""
x,y,z=test.rapport_approxim(30,0.5)
test.affichage_rapport(x,y,z,'Rapport d''approximation')
"""

#========Rapport d'approximation
"""
x,y,z=test.rapport_approxim_p(30)
test.affichage_rapport_p(x,y,z,'Rapport d''approximation')

"""