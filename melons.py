"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = 5.0
        if self.imported == True:
           total = total * 1.5
        if self.species == "Casaba" or self.species == "Ogen":
             total = total + 1
        if self.shape != "natural":
            total = total * 2
        total = total * qty

        return total
