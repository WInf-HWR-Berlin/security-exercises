from math import gcd
from matplotlib import pyplot as plt

# the class represents the multiplicative group of integers modulo n, i.e., (Z/nZ)^*
class ModNMultGroup:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.members = self.group_members()
        self.mult_table = self.multiplication_table()

    # calculates the members of (Z/nZ)^*
    def group_members(self) -> list[int]:
        pass

    # calculates either a list of lists (one row and one column per element of the group, 
    # in row x, column y the product of x and y is written)
    # or (instead of the list of lists) a dictionary with the elements of the group as keys and the list
    # of products with the other elements as values
    def multiplication_table(self) -> dict[list[int]]:
        pass

    # look up in the multiplication table to calculate the product of x and y
    def fast_mult(self, x: int, y: int) -> int:
        pass

    # calculate phi(modulus)
    def eulerphi(self) -> int:
        pass

    # calculate the inverse of x in (Z/nZ)^*
    def inverse(self, x: int) -> int:
        pass

    # calculate g^n in (Z/nZ)^*
    def power(self, g: int, n: int) -> int:
        pass

    # calculate all powers of x in (Z/nZ)^*
    def powers(self, g: int) -> list[int]:
        pass

    # calculate all powers of all elements of (Z/nZ)^*
    def all_powers(self) -> dict[list[int]]:
        pass

    def is_primitive_root(self, g: int):
        pass
    
    def all_primitive_roots(self):
        pass
    # do a scatter plot that shows all powers n^i in (Z/nZ)^* 
    def plot_powers(self, g: int):
        pass

if __name__ == '__main__':
    grp = ModNMultGroup(125)
    
    #print(grp.multiplication_table())
    #print(grp.power(3,5))
    #print(grp.eulerphi())
    prim_roots = grp.all_primitive_roots()
    print([x for x in grp.members if x not in prim_roots])
    grp.plot_powers(4)