
import numpy as np


class Bandit:
    def __init__(self):
        self._p = np.random.uniform()
        
    def __repr__(self):
        return f"<One-Armed-Bandit::f{hex(id(self))}>"
        
    def __str__(self):
        return repr(self)
        
    def draw(self,n=1):
        return np.random.binomial(n,self._p)

