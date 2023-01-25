class SqfgUtilities():
    
    def calcul_volume_substrat():
        """Calcule le volume d'engrais/substrat idéal afin de remplir
        votre potager en carré
        """
        lng = float(input("\nLongueur de la base solide (en cm)?"))
        lrg = float(input("Largeur de la base du solide (en cm)?"))
        h = float(input("Hauteur du solide (en cm)?")) 
        v = (lng * lrg * h)/1000
        
        return print("Vous avez besoins d'approximativement",v,"litres de substrat.")