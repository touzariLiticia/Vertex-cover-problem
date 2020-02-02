#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJEDDAL HANANE 3803192
TOUZARI LITICIA 3802643
Binome 4
"""
import numpy as np
import copy
import math
import time
import matplotlib.pyplot as plt
#1==============================OPERATIONS DE BASE

def creer_graphe (Nfichier):
    fichier=open(Nfichier,'r+')
    Tgraphe=dict() #Tableau de listes d'adjacence
    line=fichier.readline()# " Nombre de Sommets"
    nb_sommet=int(fichier.readline())
    line=fichier.readline() # "Sommets"
    for i in range(nb_sommet):
        Tgraphe[fichier.readline()[0]]=[]
    line=fichier.readline()#nb_arretes
    nb_arretes=int(fichier.readline())
    line=fichier.readline()#Arretes
    for i in range(nb_arretes):
        a=fichier.readline()
        Tgraphe[a[0]].append(a[2])
        Tgraphe[a[2]].append(a[0])
    return Tgraphe

def supprimer_sommet(Graphe,s):
    G=copy.deepcopy(Graphe)
    if(s in list(G.keys())):
        voisin=G[s]
        for i in voisin :
            del G[i][G[i].index(s)]
        del G[s]
    return G

def supprimer_ens_sommet(G,sommets):
    gnouv=copy.deepcopy(G)
    for s in sommets :
        gnouv=supprimer_sommet(gnouv,s)
    return gnouv

def get_degre(G):
    degres=dict()
    for s in list(G.keys()):
        degres[s]=len(G[s])
    return degres
def get_degre_max(G):
    d=(get_degre(G))
    s=max(d.values())
    l=[c for c,v in d.items() if v==s]
    return s,l
def get_nbre_aretes(G):
    n=0
    for s in list(G.keys()) :
        n+=len(G[s])
    return (n/2)
    

#2==============================GENERATIONS D'INSTANCES

def gen_graphe(n,p):
    g={} #graphe
    tirages= np.empty([n,n])
    if(n>0 and p<1 and p>0):
        a=int(n*(n-1)/2) #nombre des aretes possibles dans un graphe (complet)
        for i in range (n):
            for j in range (n) :
                tirages[i][j]=np.random.binomial(1, p, 10)[0]
                tirages[j][i]=tirages[i][j]
        #construction d'un graphe complet
        for i in range (n) :
            l=[]
            for s in range (n):
                if(i != s and (tirages[i][s]==1)):
                    l.append(s)
            g[i]=l           
    return g
def gen_graphe2(n,p):
    g={} #graphe
    if(n>0 and p<1 and p>0):
        #construction d'un graphe complet
        for i in range (n) :
            if(i not in g.keys()):
                g[i]=[]
            for s in range (n):
                if( s>i and np.random.binomial(1, p, 10)[0]==1):
                    g[i].append(s)
                    if(s not in g.keys()):
                        g[s]=[]
                    g[s].append(i)
                
    return g

#3==============================METHODES APPROCHEES
    #Algorithmes
def couplage(g):
    C=[]
    for key,val in g.items() :
        for v in val :
            if (not (key in C ) and not (v in C ) ):
                C.append(key)
                C.append(v)
    return C

def is_empty (g):
    for s in list(g.keys()):
        if g[s] != []:
            return False
    return True
def glouton (g):
    C=[]
    g_copie= copy.deepcopy(g)
    while (not is_empty(g_copie)):
        d,s=get_degre_max(g_copie)
        C.append(s[0])
        g_copie= supprimer_sommet(g_copie,s[0])
    return C
    

#3============================== Séparation et évaluation
    #===========================Branchement
class Noeud:
    def __init__(self, g,c):
        self.graphe=g
        self.couv=c


class Pile:
    def __init__(self):
        self.pile=[]
        self.taille=0
    def empiler (self,n):
        self.pile.append(n)
        self.taille +=1
    def depiler (self):
        if (self.taille > 0):
            self.taille-=1
            p=self.pile[self.taille]
            del self.pile[self.taille]
            return p
        return None
    def vide (self):
        return (self.taille <=0)
def get_arete(g):
    i=0
    cont=True
    while (cont == True and i <len(g)):
        s=list(g.keys())[i]
        if g[s] != [] :
            cont=False
        else :
            i+=1
    if (cont!=False):
        return (None, None)
    return (s, g[s][0])
    
def branch (Tg):
    # Debut du decompte du temps
    start_time = time.time()
    
    nbre_it=0
    g=copy.deepcopy(Tg)
    best=list(np.arange(len(g)))
    pile = Pile ()
    n= Noeud (g,[])
    e=get_arete(g)
    g1=supprimer_sommet(g,e[0])
    g2=supprimer_sommet(g,e[1])
    n1 = Noeud(g1, [e[0]])
    n2 = Noeud(g2, [e[1]])
    pile.empiler(n1)
    pile.empiler(n2)
    nb_noeud=3
    while (not pile.vide()):
        nbre_it+=1
        n= pile.depiler() 
        if (not is_empty(n.graphe) ):
            e=get_arete(n.graphe)
            g1=supprimer_sommet(n.graphe,e[0])
            g2=supprimer_sommet(n.graphe,e[1])
            c1=copy.deepcopy(n.couv)
            c2=copy.deepcopy(n.couv)
            c1.append(e[0])
            c2.append(e[1])
            n1 = Noeud(g1,c1) 
            n2 = Noeud(g2, c2)
            pile.empiler(n1)
            pile.empiler(n2)
            nb_noeud+=2
        else:
            if (len (n.couv) < len (best)) :
                best=n.couv
    # Affichage du temps d execution
    end_time=(time.time() - start_time)
    #print("Temps d execution : %s secondes ---" % (time.time() - start_time))
    #print("====================================Iteration :", nbre_it)
    return end_time,best,nb_noeud

            
#4 ============================== Evaluation
    
def borne_inf(g,M):
    n=len(g)
    m=get_nbre_aretes(g)
    degMax=get_degre_max(g)[0]
    b1=0
    if(degMax>0):
        b1=int (m/degMax)
    b2=len(M)/2
    b3=(2*n-1-math.sqrt((2*n-1)**2-8*m))/2
    return max(b1,b2,b3)

def borne_sup(g):
    C=couplage(g)
    return len(C)

def branch_born (Tg):
    # Debut du decompte du temps
    start_time = time.time()
    nbre_it=0
    g=copy.deepcopy(Tg)
    pile = Pile ()
    n= Noeud (g,[])
    nb_noeud=1
    M=couplage(g)
    best=M
    binf=borne_inf(g,M)
    bbest=len(M)
    if(binf<=bbest):
        e=get_arete(g)
        g1=supprimer_sommet(g,e[0])
        g2=supprimer_sommet(g,e[1])
        n1 = Noeud(g1, [e[0]])
        n2 = Noeud(g2, [e[1]])
        pile.empiler(n1)
        pile.empiler(n2)  
        nb_noeud+=2
        while (not pile.vide()):
            nbre_it+=1
            n= pile.depiler() 
            if (not is_empty(n.graphe) ):
                binf=borne_inf(n.graphe,M) + len (n.couv)  
                if((binf<=bbest)):
                    M=couplage(n.graphe)
                    if(bbest>len(M)+len(n.couv)):  
                        bbest=len(M)+len(n.couv)
                        best=M+n.couv
                    e=get_arete(n.graphe)
                    g1=supprimer_sommet(n.graphe,e[0])
                    g2=supprimer_sommet(n.graphe,e[1])
                    c1=copy.deepcopy(n.couv)
                    c2=copy.deepcopy(n.couv)
                    c1.append(e[0])
                    c2.append(e[1])
                    n1 = Noeud(g1,c1) 
                    n2 = Noeud(g2, c2)
                    pile.empiler(n1)
                    pile.empiler(n2)
                    nb_noeud+=2
            else:
                if (len (n.couv) < len (best)) :
                    best=n.couv
                    bbest=min(len(best),bbest)
    end_time=(time.time() - start_time)
    return end_time,best, nb_noeud

def branch_born_glouton(Tg):
    # Debut du decompte du temps
    start_time = time.time()
    nbre_it=0
    g=copy.deepcopy(Tg)
    pile = Pile ()
    n= Noeud (g,[])
    nb_noeud=1
    M=glouton(g)
    best=M
    binf=borne_inf(g,M)
    bbest=len(M)
    if(binf<=bbest):
        e=get_arete(g)
        g1=supprimer_sommet(g,e[0])
        g2=supprimer_sommet(g,e[1])
        n1 = Noeud(g1, [e[0]])
        n2 = Noeud(g2, [e[1]])
        pile.empiler(n1)
        pile.empiler(n2) 
        nb_noeud+=2
        while (not pile.vide()):
            nbre_it+=1
            n= pile.depiler() 
            if (not is_empty(n.graphe) ):
                binf=borne_inf(n.graphe,M) + len (n.couv)  
                if((binf<=bbest)):
                    M=glouton(n.graphe)
                    if(bbest>len(M)+len(n.couv)):  
                        bbest=len(M)+len(n.couv)
                        best=M+n.couv
                    e=get_arete(n.graphe)
                    g1=supprimer_sommet(n.graphe,e[0])
                    g2=supprimer_sommet(n.graphe,e[1])
                    c1=copy.deepcopy(n.couv)
                    c2=copy.deepcopy(n.couv)
                    c1.append(e[0])
                    c2.append(e[1])
                    n1 = Noeud(g1,c1) 
                    n2 = Noeud(g2, c2)
                    pile.empiler(n1)
                    pile.empiler(n2)
                    nb_noeud+=2
            else:
                if (len (n.couv) < len (best)) :
                    best=n.couv
                    bbest=min(len(best),bbest)
     
    end_time=(time.time() - start_time)
    return end_time,best, nb_noeud

def borne_inf_brute(g):
    n=len(g)
    m=get_nbre_aretes(g)
    degMax=get_degre_max(g)[0]
    b1=0
    if(degMax>0):
        b1=int (m/degMax)
    b3=(2*n-1-math.sqrt((2*n-1)**2-8*m))/2
    return max(b1,b3)

def branch_born_brut (Tg):
    # Debut du decompte du temps
    start_time = time.time()
    nbre_it=0
    g=copy.deepcopy(Tg)
    pile = Pile ()
    n= Noeud (g,[])
    nb_noeud=1
    binf=borne_inf_brute(g)
    best=list(np.arange(len(g)))
    bbest=len(best)
    if(binf<=bbest):
        e=get_arete(g)
        g1=supprimer_sommet(g,e[0])
        g2=supprimer_sommet(g,e[1])
        n1 = Noeud(g1, [e[0]])
        n2 = Noeud(g2, [e[1]])
        pile.empiler(n1)
        pile.empiler(n2)  
        nb_noeud+=2
        while (not pile.vide()):
            nbre_it+=1
            n= pile.depiler() 
            if (not is_empty(n.graphe) ):
                binf=borne_inf_brute(n.graphe) + len (n.couv)  
                if((binf<=bbest)):
                    e=get_arete(n.graphe)
                    g1=supprimer_sommet(n.graphe,e[0])
                    g2=supprimer_sommet(n.graphe,e[1])
                    c1=copy.deepcopy(n.couv)
                    c2=copy.deepcopy(n.couv)
                    c1.append(e[0])
                    c2.append(e[1])
                    n1 = Noeud(g1,c1) 
                    n2 = Noeud(g2, c2)
                    pile.empiler(n1)
                    pile.empiler(n2)
                    nb_noeud+=2
            else:
                if (len (n.couv) < len (best)) :
                    best=n.couv
                    bbest=min(len(best),bbest)
     
    end_time=(time.time() - start_time)
    return end_time,best, nb_noeud

#4 ============================== Amelioration du branchement

def get_arete_max(g):
    d,s=get_degre_max(g)
    if (s !=[]):
        return (s[0], g[s[0]][0])
    return (None, None)
    
def branch_born_ameliore1(Tg):
    start_time = time.time()
    
    nbre_it=0
    g=copy.deepcopy(Tg)
    pile = Pile ()
    n= Noeud (g,[])
    nb_noeud=1
    M=couplage(g)
    best=M
    binf=borne_inf(g,M)
    bbest=len(M)
    if(binf<=bbest):
        e=get_arete(g)
        g1=supprimer_sommet(g,e[0])
        g2=supprimer_sommet(g,e[1])
        n1 = Noeud(g1, [e[0]])
        c= [e[1]]+g2[e[0]]
        g2=supprimer_ens_sommet(g2,(g2[e[0]]+[e[0]]))
        n2 = Noeud(g2, c)
        nb_noeud+=2
        pile.empiler(n2)
        pile.empiler(n1)  
        while (not pile.vide()):
            nbre_it+=1
            n= pile.depiler() 
            if (not is_empty(n.graphe) ):
                binf=borne_inf(n.graphe,M) + len (n.couv)  
                if((binf<=bbest)):
                    M=couplage(n.graphe)                
                    if(bbest>len(M)+len(n.couv)):  
                        bbest=len(M)+len(n.couv)
                        best=M+n.couv
                    e=get_arete(n.graphe)
                    g1=supprimer_sommet(n.graphe,e[0])
                    g2=supprimer_sommet(n.graphe,e[1])
                    c1=copy.deepcopy(n.couv)
                    c2=copy.deepcopy(n.couv)
                    c= [e[1]]+g2[e[0]]
                    c1.append(e[0])
                    c2=c2+c
                    n1 = Noeud(g1,c1)
                    g2=supprimer_ens_sommet(g2,(g2[e[0]]+[e[0]]))
                    n2 = Noeud(g2, c2)
                    nb_noeud+=2
                    pile.empiler(n2)
                    pile.empiler(n1)
            else:
                if (len (n.couv) < len (best)) :
                    best=n.couv
                    bbest=min(len(best),bbest)
                    
        # Affichage du temps d execution
        end_time=(time.time() - start_time)
    return end_time,best,nb_noeud

#========================================================
def branch_born_ameliore2(Tg):
    start_time = time.time()
    nbre_it=0
    g=copy.deepcopy(Tg)
    pile = Pile ()
    n= Noeud (g,[])
    nb_noeud=1
    M=couplage(g)
    best=M
    binf=borne_inf(g,M)
    bbest=len(M)
    if(binf<=bbest):
        e=get_arete_max(g)
        g1=supprimer_sommet(g,e[0])
        g2=supprimer_sommet(g,e[1])
        n1 = Noeud(g1, [e[0]])
        c= [e[1]]+g2[e[0]]
        g2=supprimer_ens_sommet(g2,(g2[e[0]]+[e[0]]))
        n2 = Noeud(g2, c)
        pile.empiler(n2)
        pile.empiler(n1) 
        nb_noeud+=2
        while (not pile.vide()):
            nbre_it+=1
            n= pile.depiler() 
            if (not is_empty(n.graphe) ):
                binf=borne_inf(n.graphe,M) + len (n.couv)  
                if((binf<=bbest)):
                    M=couplage(n.graphe)
                    if(bbest>len(M)+len(n.couv)):  
                        bbest=len(M)+len(n.couv)
                        best=M+n.couv
                    e=get_arete_max(n.graphe)
                    g1=supprimer_sommet(n.graphe,e[0])
                    g2=supprimer_sommet(n.graphe,e[1])
                    c1=copy.deepcopy(n.couv)
                    c2=copy.deepcopy(n.couv)
                    c= [e[1]]+g2[e[0]]
                    c1.append(e[0])
                    c2=c2+c
                    n1 = Noeud(g1,c1) 
                    g2=supprimer_ens_sommet(g2,(g2[e[0]]+[e[0]]))
                    n2 = Noeud(g2, c2)
                    pile.empiler(n2)
                    pile.empiler(n1)
                    nb_noeud+=2
            else:
                if (len (n.couv) < len (best)) :
                    best=n.couv
                    bbest=min(len(best),bbest)
                   
    end_time=(time.time() - start_time)
        
    return end_time,best, nb_noeud  

#=================================================
        
def branch_born_ameliore3(Tg):
    start_time = time.time()
    nbre_it=0
    g=copy.deepcopy(Tg)
    pile = Pile ()
    n= Noeud (g,[])
    nb_noeud=1
    M=couplage(g)
    best=M
    binf=borne_inf(g,M)
    bbest=len(M)
    if(binf<=bbest):
        e=get_arete_max(g)
        g1=supprimer_sommet(g,e[0])
        g2=supprimer_sommet(g,e[1])
        n1 = Noeud(g1, [e[0]])
        nb_noeud+=1
        if(len(g[e[1]])>1):
            c= [e[1]]+g2[e[0]]
            g2=supprimer_ens_sommet(g2,(g2[e[0]]+[e[0]]))
            n2 = Noeud(g2, c)
            pile.empiler(n2)
            nb_noeud+=1
        pile.empiler(n1)  
        while (not pile.vide()):
            nbre_it+=1
            n= pile.depiler() 
            if (not is_empty(n.graphe) ):
                binf=borne_inf(n.graphe,M) + len (n.couv)  
                if((binf<=bbest)):
                    M=couplage(n.graphe)
                    if(bbest>len(M)+len(n.couv)):  
                        bbest=len(M)+len(n.couv)
                        best=M+n.couv
                    e=get_arete_max(n.graphe)
                    g1=supprimer_sommet(n.graphe,e[0])
                    g2=supprimer_sommet(n.graphe,e[1])
                    c1=copy.deepcopy(n.couv)
                    c2=copy.deepcopy(n.couv)
                    if(len(g[e[1]])>1):
                         c= [e[1]]+g2[e[0]]
                         c2=c2+c
                         g2=supprimer_ens_sommet(g2,(g2[e[0]]+[e[0]]))
                         n2 = Noeud(g2, c2)
                         nb_noeud+=1
                         pile.empiler(n2)
                    c1.append(e[0])
                    n1 = Noeud(g1,c1) 
                    nb_noeud+=1
                    pile.empiler(n1)
            else:
                if (len (n.couv) < len (best)) :
                    best=n.couv
                    bbest=min(len(best),bbest)
    end_time=(time.time() - start_time)
        
    return end_time, best,nb_noeud 


    
    






