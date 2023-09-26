try:
    import cPickle as cPickle
except:
    import pickle

import json

def serialize(obj, file, type):
    
    if type == 'pickle' :
        dbfile = open(file, 'wb')
        pickle.dump(obj, dbfile)
        dbfile.close()
      
    if type == 'json':
        with open(file, 'wt') as f :
            x = json.dump(obj, f)
        

def deserialize(file, type):
    
    if type == 'pickle':
        dbfile = open(file, 'rb')
        x = pickle.load(dbfile)
        dbfile.close()
        return x
    
    if type == 'json':
        with open (file) as f:
            x = json.load(f)
            return x
        
if __name__ == "__main__":
    d1 ={'a':'x','b':'y','c':'z',30 : (2,4,'a')}

    serialize(d1, 'a.dat','pickle')

    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')

    print('#' * 20)

    serialize(d1, 'a.json', 'json')

    x = deserialize('a.json', 'json')
    
    print(f'json : {x}')
