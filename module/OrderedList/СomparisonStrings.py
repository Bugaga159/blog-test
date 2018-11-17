from .OrderedList import *


class СomparisonStrings(OrderedList):


    def comparison(self, val1, val2):
        if int(val1) > int(val2):
          return True
        else:
          return False