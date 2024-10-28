class Grandparent:
    def gpdisplay(self):
        print("GRAND PARENT METHOD...")

class Parent(Grandparent):
    def pdisplay(self):
        print("PARENT METHOD...")

class Child(Parent):
    def cdisplay(self):
        print("CHILD METHOD...")

c=Child()
p=Parent()
# c.cdisplay()
# c.pdisplay()
c.gpdisplay()
p.gpdisplay()
p.pdisplay()