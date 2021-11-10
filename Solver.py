#coding utf-8
import copy


class Noeud:
    def __init__(self,c_etat):
        self.etat = c_etat

    def afficher_noeud(self):
        print(self.etat)

    def est_etat_final(self):
        etat_final = [
            [1, 6, 2],
            [8, 0, 3],
            [7, 5, 4]
        ]
        return self.etat == etat_final



    def pos_case_vide(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.etat[i][j] == 0:
                    return (i,j)

    def numero(self,i,j):
        return self.etat[i][j]

    def permuter(self,c1,c2):
        i1 = c1[0]
        j1 = c1[1]
        i2 = c2[0]
        j2 = c2[1]
        n = copy.deepcopy(self)
        aux = n.etat[i1][j1]
        n.etat[i1][j1] = n.etat[i2][j2]
        n.etat[i2][j2] = aux
        return n

    def voisins(self):
        if self.pos_case_vide() == (0,0):
            n1 = self.permuter((0,0),(0,1))
            n2 = self.permuter((0,0),(1,0))
            return [n1,n2]
        elif self.pos_case_vide() == (0,1):
            n1 = self.permuter((0,1),(1,1))
            n2 = self.permuter((0,1),(0,0))
            n3 = self.permuter((0,1),(0,2))
            return [n1,n2,n3]
        elif self.pos_case_vide() == (0,2):
            n1 = self.permuter((0,2),(0,1))
            n2 = self.permuter((0,2),(1,2))
            return [n1,n2]
        elif self.pos_case_vide() == (1,0):
            n1 = self.permuter((1,0),(0,0))
            n2 = self.permuter((1,0),(1,1))
            n3 = self.permuter((1,0),(2,0))
            return [n1,n2,n3]
        elif self.pos_case_vide() == (1,1):
            n1 = self.permuter((1,1),(0,1))
            n2 = self.permuter((1,1),(2,1))
            n3 = self.permuter((1,1),(1,0))
            n4 = self.permuter((1,1),(1,2))
            return [n1,n2,n3,n4]
        elif self.pos_case_vide() == (1,2):
            n1 = self.permuter((1,2),(0,2))
            n2 = self.permuter((1,2),(2,2))
            n3 = self.permuter((1,2),(1,1))
            return [n1,n2,n3]
        elif self.pos_case_vide() == (2,0):
            n1 = self.permuter((2,0),(1,0))
            n2 = self.permuter((2,0),(2,1))
            return [n1,n2]
        elif self.pos_case_vide() == (2,1):
            n1 = self.permuter((2,1),(1,1))
            n2 = self.permuter((2,1),(2,0))
            n3 = self.permuter((2,1),(2,2))
            return [n1,n2,n3]
        else:
            n1 = self.permuter((2,2),(1,2))
            n2 = self.permuter((2,2),(2,1))
            return [n1,n2]

    def recherche(self, a, l):
        i = 0
        ok = False
        while (i < len(l) - 1) and (ok == False):
            ok = l[i].etat == a.etat
            i = i + 1
        return ok

    def recherche_en_largeur(self):
        freeNodes = [self]
        closedNodes = []
        goalNode = []
        generatedStates = []
        success = False
        while freeNodes != [] and success == False:
            """ajouter le premier de freenodes a closednodes et le supprimer de freenodes"""
            closedNodes.append(freeNodes[0])
            firstNode = copy.deepcopy(freeNodes[0])
            del freeNodes[0]

            """generer ses voisins dans generatedStates"""
            tab = firstNode.voisins()
            for a in tab:
                if not self.recherche(a,closedNodes) and not self.recherche(a,freeNodes):
                    generatedStates.append(a)
            for noeud in generatedStates:
                if noeud.est_etat_final():
                    success = True
                    goalNode.append(noeud)

            """ajouter les voisins generés à FreeNodes (en cas de succés ajouter seulement le noeud final)"""
            if success:
                freeNodes = freeNodes + goalNode
                generatedStates = []
            else:
                freeNodes = freeNodes + generatedStates
                generatedStates = []

        return closedNodes + freeNodes


    def recherche_en_profondeur(self):
        freeNodes = [self]
        closedNodes = []
        generatedStates = []
        success = False
        while freeNodes != [] and success == False:
            closedNodes.append(freeNodes[len(freeNodes)-1])

            fistNode = copy.deepcopy(freeNodes[len(freeNodes)-1])
            del freeNodes[len(freeNodes)-1]

            tab = fistNode.voisins()
            for a in tab:
                if not self.recherche(a,closedNodes) and not self.recherche(a,freeNodes) :
                    generatedStates.append(a)

            generatedStates.reverse()
            freeNodes = freeNodes + generatedStates
            generatedStates = []

            if closedNodes[len(closedNodes)-1].est_etat_final():
                return closedNodes





"""

    def recherche_en_profondeur(self):
        freeNodes = [self]
        closedNodes = []
        success = False

        while (freeNodes != [] and success == False):
            if (freeNodes[0] not in closedNodes):
                closedNodes.append(freeNodes[0])

            for noeud in closedNodes:
                if noeud.est_etat_final():
                    return closedNodes

            fistNode = freeNodes[0]
            generatedStates = fistNode.voisins()

            nodes_a_supprimmer = []
            for val in generatedStates:
                if (val in freeNodes) or (val in closedNodes):
                    nodes_a_supprimmer.append(val)
            for nodes in nodes_a_supprimmer:
                generatedStates.remove(nodes)

            if generatedStates == []:
                freeNodes.remove(freeNodes[0])
            else:
                while generatedStates[0] in closedNodes:
                    generatedStates.remove(generatedStates[0])
                if generatedStates != []:
                    freeNodes.insert(0,generatedStates[0])
                generatedStates = []
"""