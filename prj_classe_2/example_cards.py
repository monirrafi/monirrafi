"""Ce module contient un exemple de code lié à

Pensez Python, 2e édition
par Allen Downey
http://thinkpython2.com

Droit d'auteur 2015 Allen Downey

Licence : http://creativecommons.org/licenses/by/4.0/
"""

de __future__ import print_function, division

importer au hasard


Carte de classe :
    """Représente une carte à jouer standard.
    
    Les attributs:
      costume : entier 0-3
      rang : entier 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [Aucun, "As", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Valet", "Reine", "Roi"]

    def __init__(self, suit=0, rank=2):
        self.suit = costume
        self.rank = rang

    def __str__(soi) :
        """Renvoie une représentation sous forme de chaîne lisible par l'homme."""
        renvoie '%s de %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(soi, autre):
        """Compare cette carte à une autre, d'abord par couleur, puis par rang.

        renvoie : booléen
        """
        t1 = self.suit, self.rank
        t2 = autre.suite, autre.rang
        retourner t1 < t2


pont de classe :
    """Représente un jeu de cartes.

    Les attributs:
      cartes : liste des objets Carte.
    """
    
    def __init__(self):
        """ Initialise le Deck avec 52 cartes.
        """
        self.cards = []
        pour costume dans la gamme (4):
            pour le rang dans la plage (1, 14):
                card = Card (couleur, rang)
                self.cards.append(carte)

    def __str__(soi) :
        """ Renvoie une représentation sous forme de chaîne du jeu.
        """
        res = []
        pour la carte dans self.cards :
            res.append(chaîne(carte))
        retourne '\n'.join(res)

    def add_card(soi, carte):
        """Ajoute une carte au paquet.

        carte : carte
        """
        self.cards.append(carte)

    def remove_card(soi, carte):
        """Retire une carte du jeu ou déclenche une exception si elle n'y est pas.
        
        carte : carte
        """
        self.cards.remove(carte)

    def pop_card(self, i=-1):
        """Retire et renvoie une carte du paquet.

        i : index de la carte à éclater ; par défaut, éclate la dernière carte.
        """
        retourner self.cards.pop(i)

    def shuffle (soi):
        """Mélange les cartes de ce paquet."""
        random.shuffle(self.cards)

    def tri(auto):
        """Trie les cartes par ordre croissant."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """ Déplace le nombre donné de cartes du paquet vers la Main.

        hand : destination de l'objet Hand
        num : nombre entier de cartes à déplacer
        """
        pour je dans la plage (num):
            hand.add_card(self.pop_card())


main de classe (Pont):
    """Représente une main de cartes à jouer."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = étiquette


def find_defining_class(obj, method_name):
    """Recherche et renvoie l'objet de classe qui fournira
    la définition de nom_méthode (sous forme de chaîne) s'il est
    invoqué sur obj.

    obj : tout objet python
    nom_méthode : nom de la méthode de chaîne
    """
    pour ty dans type(obj).mro() :
        si nom_méthode dans ty.__dict__ :
            retour ty
    retour Aucun


si __nom__ == '__main__' :
    pont = pont()
    deck.shuffle()

    main = Main()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(main, 5)
    main.sort()
    impression (main)