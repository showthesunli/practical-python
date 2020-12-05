#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# exercise 4.3

class Stock:
    """
    stock class
    """
    def __init__(self, name, shares, price):
        """
        docstring
        """
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        """
        docstring
        """
        return self.shares*self.price
    
    def sell(self, num:int):
        if num > self.shares:
            raise Exception
        self.shares = self.shares - num