class fonctions:
    def __init__(self,j1,j2):
        self.tab = [[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7]
        self.joueur1 = j1
        self.joueur2 = j2
        i = 0
        parcours = 1
        while i <= 5:
            j = 0
            while j <= 6:
                self.tab[i][j] = parcours
                j += 1
                parcours += 1
            i += 1
        
    def afficheTableau(self):
        i = 0
        parcours = 1
        while i <= 5:
            j = 0
            while j <= 6:
                print("|",self.tab[i][j],"|",end="\t")
                j += 1 
                parcours += 1
            print("\n")
            i += 1


    def verificateurVerticale(self,i,j):
        if self.tab[i][j] == self.tab[i+1][j]  and  self.tab[i][j] == self.tab[i+2][j]  and  self.tab[i][j] == self.tab[i+3][j] :
            return 1
        else:
            return 0 
    
    def verificateurHorizontale(self,i,j):
        if self.tab[i][j] == self.tab[i][j+1]  and  self.tab[i][j] == self.tab[i][j+2]  and  self.tab[i][j] == self.tab[i][j+3] :
            return 1
        else:
            return 0

    def verificateurbObliqueNormale(self,i,j):
        if self.tab[i][j] == self.tab[i+1][j+1]  and  self.tab[i][j] == self.tab[i+2][j+2]  and  self.tab[i][j] == self.tab[i+3][j+3] :
            return 1
        else:
            return 0
            
    def verificateurbObliqueAnormale(self,i,j):
        if self.tab[i][j] == self.tab[i+1][j-1]  and  self.tab[i][j] == self.tab[i+2][j-2]  and  self.tab[i][j] == self.tab[i+3][j-3] :
            return 1
        else:
            return 0

    def gagner(self):
        g = 0
        i = 0
        while i <= 2:
            j = 0
            while j <= 6:
                if(self.verificateurVerticale(i,j) == 1):
                    g = 1
                j += 1
            i += 1

        i = 0
        while i <= 5:
            j = 0
            while j <= 3:
                if(self.verificateurHorizontale(i,j) == 1):
                    g = 1
                j += 1
            i += 1

        i = 0
        while i <= 2:
            j = 0
            while j <= 3:
                if(self.verificateurbObliqueNormale(i,j) == 1):
                    g = 1
                j += 1
            i += 1

        i = 0
        while i <= 2:
            j = 3
            while j <= 6:
                if(self.verificateurbObliqueAnormale(i,j) == 1):
                    g = 1
                j += 1
            i += 1
                    
        return g

    def finJeu(self):
        f = 1
        i = 0
        while i <= 5 :
            j = 0
            while j <= 6 :
                if self.tab[i][j] != self.joueur1.symbole and self.tab[i][j] != self.joueur2.symbole :
                    f = 0
                    break
                j += 1
            i += 1
        return f

    
