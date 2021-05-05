"Quantum gates."

from .qtypes import ket, Gate
from numpy import array

Not = Gate(transform=array(
    [(0, 1),
     (1, 0)]
))

print(Not)
print(ket(1,0))
print(Not.apply(ket(1, 0)))
