#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# exercise 4.3

class Stock:
    """
    stock class
    """
    __slots__ = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        """
        docstring
        """
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

    @property
    def cost(self) -> float:
        """
        computa the value of property with name cost
        """
        return self.shares*self.price
    
    def sell(self, num:int):
        if num > self.shares:
            raise Exception
        self.shares = self.shares - num