# portfolio.py

from typing import List
from collections import Counter
from stock import Stock

class Portfolio:

    def __init__(self, holding: List[Stock]):
        self._holding = holding
    
    def __iter__(self):
        return self._holding.__iter__()

    @property
    def cost_shares(self) -> float:
        '''
        compute cost of portfolio
        '''
        return sum([s.cost for s in self._holding])

    def tabulate_shares(self) -> Counter:
        '''
        compute every shares order by name
        '''
        total_shares:Counter = Counter()
        for s in self._holding:
            total_shares[s.name] += s.shares
        return total_shares
