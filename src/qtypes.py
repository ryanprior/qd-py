from numpy import cdouble, array, dtype, matmul
from dataclasses import dataclass

# example:
# k = ket(1,0)

Ket = dtype([("zero", cdouble), ("one", cdouble)])
# Transform = dtype((
#     [("a", cdouble), ("b", cdouble)],
#     [("c", cdouble), ("d", cdouble)]
# ))

def ket(zero: cdouble, one: cdouble) -> Ket:
    return array(([zero], [one]), dtype=cdouble)

@dataclass
class Gate:
    transform: array

    def apply(self, k: Ket):
        return matmul(self.transform, k)

