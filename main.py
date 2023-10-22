class LB:
    def lb_system(self, new_mass):
        print(f"M: {new_mass} lb")

class KG:
    def kg_system(self, mass):
        print(f"M: {mass} lb")

class KGAdapter(LB):
    def __init__(self, oldsystem):
        self.oldsystem = oldsystem

    def lb_system(self, new_mass):
        self.oldsystem.kg_system(new_mass*2.205)


if __name__ == "__main__":
    masslb = LB()
    masskg = KG()
    kgadapter = KGAdapter(masskg)

    masslb.lb_system(15)
    kgadapter.lb_system(20)