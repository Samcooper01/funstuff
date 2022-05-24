import time
#
# This is a hashtable meant to handle a 100 element data sets and preform the following:
# insert(), hashFunction(), remove(), iterator(), find()
# Load Factor of 75% - uses open addressing to handle collisions
#
class Hashtable:
    def __init__(self):
        self.list = [''] * 100 #set size to 100
        self.size = 100

    # Make sure to run this class with PYTHONHASHSEED=1 python hashtable.py
    def hashfunction(self, key="ABCDEFGHI"):
        code = hash(key) % len(self.list)
        return code

    def insert(self, value):
        newkey = self.hashfunction(value)
        i = 0
        while i < self.size: #open addressing
            if self.list[newkey] == '':
                self.list[newkey] = value
                if self.getnumofvalues() > (len(self.list) * 0.75):
                    addme = [''] * (len(self.list) * 2)
                    self.list = self.rehash(addme)
                    self.size = len(self.list)
                return True
            else:
                if newkey == self.size - 1:
                    newkey -= (self.size - 1)
                else:
                    newkey += 1
                i += 1
        print("Didn't insert")

    def tostring(self):
        for x in self.list:
            if x != '':
                print('[' + x + '] ', end ='')
            else:
                print('[] ', end='')
        print()

    def iterator(self):
        return self.list

    def getnumofvalues(self):
        total = 0
        for i in range(self.size):
            if self.list[i] != '':
                total += 1
        return total

    def find(self, value):
        key = self.hashfunction(value)
        i = 0
        while i < self.size:
            print('Search iteration #: ' + str(i))
            if self.list[key] == value:
                return value
            else:
                if key == (self.size - 1):
                    key -= (self.size - 1)
                else:
                    key += 1
                i += 1
        print("Didn't find")

    #plist is a list of the new length with all [''] values
    #returns a list of the new length with the values hashed into it
    def rehash(self, plist):
        output = plist
        for i in range(len(self.list)):
            key = self.hashfunction(self.list[i])
            output[key] = self.list[i]
        return output



#test it out (When you run it use terminal and type:  PYTHONHASHSEED=1 python hashtable.py
#this is so the hash table won't use a random hash seed everytime
jerry = Hashtable()
#insert 40 values (No resizing/reshashing
for x in range(40):
    jerry.insert("Sam" + str(x))
print(jerry.iterator())
print('Find Sam24: ', end ='')
print(jerry.find('Sam24') + ' (pretty fast huh')
print('Now lets do a reshash and resize')
#insert 50 new values
for x in range(50):
    jerry.insert("John" + str(x))
print(jerry.iterator())
print('New length: ' + str(len(jerry.list)) + ' (old length was 100)')
print('Thanks that is it!')
time.sleep(2)
print('Hey thanks for waiting around, now click this link')
print('https://www.youtube.com/watch?v=a3Z7zEc7AXQ')