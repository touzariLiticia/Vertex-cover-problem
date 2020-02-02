#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJEDDAL HANANE 3803192
TOUZARI LITICIA 3802643
Binome 4
""" 
import implementation as imp
import numpy as np

import math
import time
import matplotlib.pyplot as plt

    #Tests
def test_couplage(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                start_time = time.time()
                C=imp.couplage(g)
                end_time = time.time()
                t=(end_time- start_time)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
def test_couplage_p(n):
    x=[]
    y=[]
    xl=[]
    yl=[]
    if(n>1):
        for i in np.arange(0.1,1,0.01):
            x.append(i)
            xl.append(math.log(i))
            g=imp.gen_graphe2(n,i)
            start_time = time.time()
            c=imp.couplage(g)
            end_time = time.time()
            t=(end_time- start_time)
            y.append(t)
            yl.append(math.log(t))
        return x,y,xl,yl
    else:
        print('n doit etre supérieur à 1')
        return None 
    
def test_glouton(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                start_time = time.time()
                c=imp.glouton(g)
                end_time = time.time()
                t=(end_time- start_time)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
def test_glouton_p(n):
    x=[]
    y=[]
    xl=[]
    yl=[]
    if(n>1):
        for i in np.arange(0.1,1,0.01):
            x.append(i)
            xl.append(math.log(i))
            g=imp.gen_graphe2(n,i)
            start_time = time.time()
            c=imp.glouton(g)
            end_time = time.time()
            t=(end_time- start_time)
            y.append(t)
            yl.append(math.log(t))
        return x,y,xl,yl
    else:
        print('n doit etre supérieur à 1')
        return None 
    
def compare_couplage_glouton(nmax,p):
    x=[]
    y1=[]
    y2=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            i=int(i)+1
            x.append(i)
            cumul1=0
            cumul2=0
            for j in range(20):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                c2=len(imp.glouton(g))
                c1=len(imp.couplage(g))
                if (c1<c2):
                    cumul1+=1
                else :
                    if (c2<c1):
                        cumul2+=1
                    else:
                        cumul2+=1
                        cumul1+=1
            y1.append(cumul1)
            y2.append(cumul2)
        return x,y1,y2
    else:
        print('nmax doit etre supérieur à 1')
        return None
def ecart_couplage_glouton(nmax,p):
    x=[]
    y=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            i=int(i)+1
            x.append(i)
            ecumul=0
            for j in range(20):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                c2=len(imp.glouton(g))
                c1=len(imp.couplage(g))
                ecumul+=abs(c2-c1)
            y.append(ecumul/20)
        return x,y
    else:
        print('nmax doit etre supérieur à 1')
        return None

#=====TEST
def test_branch1(nmax,nmin,pas,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    if(nmin>1):
        for i in range (nmin,nmax,pas):
            print(i)+1
            x.append(i)
            xl.append(math.log(i))
            g=imp.gen_graphe2(i,p)
            print(i)
            t,b,nb_n=imp.branch(g)
            y.append(t)
            yl.append(math.log(t))
        return x,y,xl,yl
    else:
        print('nmin doit etre supérieur à 1')
        return None
def test_branch(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch(g)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
def test_branch_p(n):
    x=[]
    y=[]
    xl=[]
    yl=[]
    if(n>1):
        for i in np.arange(0.1,1,0.01):
            print(i)+1
            x.append(i)
            xl.append(math.log(i))
            g=imp.gen_graphe2(n,i)
            print(i)
            t,b,nb_n=imp.branch(g)
            y.append(t)
            yl.append(math.log(t))
        return x,y,xl,yl
    else:
        print('n doit etre supérieur à 1')
        return None 


#===========================Test branch_born_ameliore 1
def test_branch_born_ameliore1(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born_ameliore1(g)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
  

#=============================Test branch_born_ameliore 2
def test_branch_born_ameliore2(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born_ameliore2(g)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None

#=================== Branch_born_ameliore3   
def test_branch_born_ameliore3(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born_ameliore3(g)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
    
    
#5 ==============================Tests des méthodes approchées
def rapport_approxim(nmax,p):
    x=[]
    y1=[]
    y2=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            rcumul1=0
            rcumul2=0
            for j in range(10):
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,C,nb_n=imp.branch_born_ameliore1(g)
                c1=len(C)
                c2=len(imp.couplage(g))
                c3=len(imp.glouton(g))
                rcumul1+=c2/c1
                rcumul2+=c3/c1
            y1.append(rcumul1/10)
            y2.append(rcumul2/10)
        return x,y1,y2
    else:
        print('nmax doit etre supérieur à 1')
        return None
def rapport_approxim_p(n):
    x=[]
    y1=[]
    y2=[]
    if(n>1):
        for i in np.arange(0.1,1,0.01):
            print(i)
            i=int(i)+1
            x.append(i)
            g=imp.gen_graphe2(n,i)
            t,C,nb_n=imp.branch_born_ameliore1(g)
            c1=len(C)
            c2=len(imp.couplage(g))
            c3=len(imp.glouton(g))
            y1.append(c2/c1)
            y2.append(c3/c1)
        return x,y1,y2
    else:
        print('n doit etre supérieur à 1')
        return None        
def test_branch_born(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born(g)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
def test_branch_born_glouton(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born_glouton(g)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
def test_branch_born_brut(nmax,p):
    x=[]
    y=[]
    xl=[]
    yl=[]
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born_brut(g)
                tcumul+=t
            y.append(tcumul/10)
            yl.append(math.log(tcumul/10))
        return x,y,xl,yl
    else:
        print('nmax doit etre supérieur à 1')
        return None
def Comparaison_branch_born_ameliore(nmax,p):
    x=[]
    xl=[]
    yl1=[]
    y1=[]
    yl2=[]
    y2=[]
    yl3=[]   
    y3=[]
    
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul1=0
            tcumul2=0
            tcumul3=0
            nbSommet1=0
            nbSommet2=0
            nbSommet3=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born_ameliore1(g)
                tcumul1+=t
                nbSommet1+=nb_n
                t,b,nb_n=imp.branch_born_ameliore2(g)
                tcumul2+=t
                nbSommet2+=nb_n
                t,b,nb_n=imp.branch_born_ameliore3(g)
                tcumul3+=t
                nbSommet3+=nb_n
                
            y1.append(nbSommet1/10)
            y2.append(nbSommet2/10)
            y3.append(nbSommet3/10)
            yl1.append(math.log(tcumul1/10))
            yl2.append(math.log(tcumul2/10))
            yl3.append(math.log(tcumul3/10))
    #comparaison du log (temps) 
    plt.xlabel('Log de la taille d''instance: N')
    plt.ylabel('Log du temps de calcul')
    plt.title("comparaison du log (temps)")
    plt.plot(xl,yl1,label="branch-born_ameliore1")
    plt.plot(xl,yl2,label="branch-born_ameliore2")
    plt.plot(xl,yl3,label="branch-born_ameliore3")
    plt.legend()
    plt.show()
    #comparaison du nombre de noeuds créé
    plt.xlabel('Taille d''instance: N')
    plt.ylabel('Nombre de noeuds')
    plt.title("comparaison du nombre de noeuds créés")
    plt.plot(x,y1,label="branch-born_ameliore1")
    plt.plot(x,y2,label="branch-born_ameliore2")
    plt.plot(x,y3,label="branch-born_ameliore3")
    plt.legend()
    plt.show()  
def Comparaison_branch_born(nmax,p):
    x=[]
    xl=[]
    yl1=[]
    y1=[]
    yl2=[]
    y2=[]
    yl3=[]   
    y3=[]
    
    N=nmax*(np.arange(10)+1)/10
    if(nmax>1):
        for i in (N):
            print(i)
            i=int(i)+1
            x.append(i)
            xl.append(math.log(i))
            tcumul1=0
            tcumul2=0
            tcumul3=0
            nbSommet1=0
            nbSommet2=0
            nbSommet3=0
            for j in range(10):   
                g=imp.gen_graphe(i,p)
                while(imp.is_empty(g)):
                    g=imp.gen_graphe(i,p)
                t,b,nb_n=imp.branch_born(g)
                tcumul1+=t
                nbSommet1+=nb_n
                t,b,nb_n=imp.branch_born_glouton(g)
                tcumul2+=t
                nbSommet2+=nb_n
                t,b,nb_n=imp.branch_born_brut(g)
                tcumul3+=t
                nbSommet3+=nb_n
                
            y1.append(nbSommet1/10)
            y2.append(nbSommet2/10)
            y3.append(nbSommet3/10)
            yl1.append(math.log(tcumul1/10))
            yl2.append(math.log(tcumul2/10))
            yl3.append(math.log(tcumul3/10))
    #comparaison du log (temps) 
    plt.xlabel('Log de la taille d''instance: N')
    plt.ylabel('Log du temps de calcul')
    plt.title("comparaison du log (temps)")
    plt.plot(xl,yl1,label="branch-born")
    plt.plot(xl,yl2,label="branch-born_glouton")
    plt.plot(xl,yl3,label="branch-born_brut")
    plt.legend()
    plt.show()
    #comparaison du nombre de noeuds créé
    plt.xlabel('Taille d''instance: N')
    plt.ylabel('Nombre de noeuds')
    plt.title("comparaison du nombre de noeuds créés")
    plt.plot(x,y1,label="branch-born")
    plt.plot(x,y2,label="branch-born_glouton")
    plt.plot(x,y3,label="branch-born_brut")
    plt.legend()
    plt.show()  
    
    
def affichage_n_t(x,y,titre=''):
    plt.xlabel('Taille de l''instance: N')
    plt.ylabel('Temps de calcul')
    plt.plot(x,y)
    plt.title(titre)
    plt.show()
def affichage_n_logt(x,y,titre=''):
    plt.xlabel('Taille de l''instance: N')
    plt.ylabel('Log du temps de calcul')
    plt.title(titre)
    plt.plot(x,y)
    plt.show()
def affichage_logn_logt(x,y,titre=''):
    plt.xlabel('Log de la taille d''instance: N')
    plt.ylabel('Log du temps de calcul')
    plt.title(titre)
    plt.plot(x,y)
    plt.show()
    
def affichage_p_t(x,y,titre=''):
    plt.xlabel('Probabilité: p')
    plt.ylabel('Temps de calcul')
    plt.title(titre)
    plt.plot(x,y)
    plt.show()
def affichage_p_logt(x,y,titre=''):
    plt.xlabel('Probabilité: p')
    plt.ylabel('Log du temps de calcul')
    plt.title(titre)
    plt.plot(x,y)
    plt.show()
def affichage_logp_logt(x,y,titre=''):
    plt.xlabel('Log de la probabilité: p')
    plt.ylabel('Log du temps de calcul')
    plt.title(titre)
    plt.plot(x,y)
    plt.show()
    
def affichage_bar(x,y,z,titre=''):
    plt.xlabel('Taille de l''instance : N')
    plt.ylabel('Comptage de la meilleure valeur')
    plt.title(titre)
    plt.bar(x,y)
    plt.bar(x,z)
    plt.show()
def affichage_ecart(x,y,titre=''):
    plt.xlabel('Taille de l''instance : N')
    plt.ylabel('Ecart')
    plt.title(titre)
    plt.plot(x,y)
    plt.show()
def affichage_rapport(x,y,z,titre=''):
    plt.xlabel('Taille de l''instance : N')
    plt.ylabel('Rapport d''approximation')
    plt.title(titre)
    plt.plot(x,y,"r")
    plt.plot(x,z,"b")
    plt.show()

def affichage_rapport_p(x,y,z,titre=''):
    plt.xlabel('Probabilité: p')
    plt.ylabel('Rapport d''approximation')
    plt.title(titre)
    plt.plot(x,y,"r")
    plt.plot(x,z,"b")
    plt.show()





