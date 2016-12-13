"""
Data-types
"""

import collections

class Enum(object):
    def __init__(self, *enums):
        for i, val in enumerate(enums):
            if collections.Counter(enums)[val] > 1:
                raise Exception("Duplicate ENUM entry found: %s" % val)
            else:
                self.__setattr__(val, i, False)

    def __setattr__(self, name, value, locked = True):
        if (name not in self.__dict__):
            if locked == True:
                raise Exception("Unable to set attribute '%s' - instance has already been initialized with data!" % name)
            else:
                self.__dict__[name] = value
        else:
            raise Exception("Unable to assign value to %s - already assigned!" % name)

    def __getitem__(self, item):
        return self.__dict__[item]


if __name__ == "__main__":
    a = Enum("Orange", "Apple", "Pear")
