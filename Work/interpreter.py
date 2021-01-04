class Stock:

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._tmp

    @shares.setter
    def shares(self, value):
        print('call setter')
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._tmp = value
    
    @property
    def cost(self) -> float:
        return self.shares * self.price

if __name__ == "__main__":
    s = Stock('google',123,123.1)
    print(s.shares)
    print(s.cost)