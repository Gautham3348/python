#Dictionary
''' dictionaries are used to store values in key : value 
It is a collecton which is ordered, changeable and do not allow duplicates
dictionary operations are  clear, copy, fromkeys, get, keys, pop, setdefault,etc.., '''

rec = {1 : 'Hello', 5 : 'Hai', 10 : 'How are you'}
print(rec)

#accessing by key value
print(rec[5])

#accessing by index in dictionary
rec.get(1)

#combining keys and values
keys = [12,21,31]
values = ["Ram", "raju", "Ravi"]
data = dict(zip(keys,values))
print(data)

#adding values to dictionary
data[55] = "Rays"
print(data)

#deleting a value form dictionary
del data[55]
print(data)
