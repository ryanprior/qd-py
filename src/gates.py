"Quantum gates."

from .qtypes import ket, Gate
from numpy import array
from math import sqrt

Not = Gate(transform=array(
    [(0, 1),
     (1, 0)]
))

Hadamard = Gate(transform=1/sqrt(2) * array(
    [(1,  1),
     (1, -1)]
))

print(Not)
print(ket(1,0))
print("NOT==")
print(Not.apply(ket(1, 0)))
print("HADAMARD==")
print(Hadamard.apply(ket(1, 0)))
