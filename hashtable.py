#
# This is a hashtable meant to handle a 100 element data sets and preform the following:
# insert(), hashFunction(), remove(), iterator(), returnValue()
# Constructor includes
#
class Hashtable:
    def __init__(self):
        self.list = [''] * 100 #set size to 100

    # Make sure to run this class with PYTHONHASHSEED=1 python hashtable.py
    def hashfunction(self, key="ABCDEFGHI"):
        code = hash(key) % 100
        return code

    def insert(self, value):
        newkey = self.hashfunction(value)
        i = 0
        while i < 101: #open addressing
            if self.list[newkey] == '':
                self.list.insert(newkey, value)
                return True
            else:
                if newkey == 100:
                    newkey -= 100
                else:
                    newkey += 1
                i += 1

    def tostring(self):
        print(self)


testList = ['hi', 'hello', 'sam']
jerry = Hashtable()
jerry.insert("Samuel")
print(jerry.hashfunction())
