class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def axial_subtract(self, autre):
        return Point(self.x - autre.x, self.y - autre.y)

    def distance(self, autre):
        vec = self.axial_subtract(autre)
        return (abs(vec.x) + abs(vec.x + vec.y) + abs(vec.y)) / 2


class Dodo:
    def __init__(self):
        self.taille_x = 6
        self.taille_y = 6
        self.checkers = []

        self.init_checkers()

    def init_checkers(self, result=False):
        """
        Initialisation des checkers des deux joueur.

        Parameters:
        result: bool (afficher ou non les coordonnées résultantes)
        """


        for player in [-1, 1]:

            # -------------------Première colonne (6, ...) ou (-6, ...)-------------------
            for y in range(0, self.taille_y*player + player, player):
                self.checkers.append(Point(self.taille_x*player, y))


            # -------------------Les autres colonnes -------------------
            y_init = 0
            for x in range(player*self.taille_x - player, -player, -player):
                # x varie de 5 à 0 ou -5 à 0 (donc un pas de -1 ou +1)

                # À partir de la troisième colonne colonne, on décale la première ligne de 1 vers le bas (P-1)
                # ou 1 vers le haut (P1) à chaque nouvelle colonne
                if player == 1 and x  < self.taille_x - 1:
                    y_init += player
                elif player == -1 and x > -self.taille_x + 1:
                    y_init += player

                for y in range(y_init, self.taille_y*player + player, player):
                    self.checkers.append(Point(x, y))
   
        # Affichage du résultat:
        if not result:return
        for i in range(len(self.checkers)):
            c = self.checkers[i]
            if i == len(self.checkers)//2:
                print("Next player")
            print(c.x, c.y)


def main():
    dodo = Dodo()


if __name__ == "__main__":
    main = main()
                        

    
        
    

