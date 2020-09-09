
import numpy as np


class Bandit:
    """
    A simple 1-armed bandit.
    
    Picks a random, hidden, uniform value 
    for p between 0.0 and 1.0. 
    
    The `draw(n)` method samples from the 
    binomial distribution using the hidden
    p value and the specified n (default = 1).
    
    """
    def __init__(self):
        self._p = np.random.uniform()
        
    def __repr__(self):
        return f"<One-Armed-Bandit::f{hex(id(self))}>"
        
    def __str__(self):
        return repr(self)
        
    def draw(self,n=1):
        """Draw samples from the binomial distribution
        using the bandit's hidden p-value."""
        return np.random.binomial(n,self._p)

