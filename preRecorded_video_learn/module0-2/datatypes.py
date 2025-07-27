"""
x = "Hello world" # <class 'str'>
x = 20 #<class 'int'>
x = 20.5 #<class 'float'>
x = 1j  #<class 'complex'>
x = ["apple", "banana", "cherry"] # <class 'list'>
x = ("apple", "banana", "cherry")#<class 'tuple'>
x = range(6) #range(0, 6) <class 'range'>
x = {"name" : "John", "age" : 36} # <class 'dict'>
x = {"apple","banana", "cherry"} # <class 'set'>
x = frozenset({"apple","banana", "cherry"}) # <class 'frozenset'>
x = True #<class 'bool'>
x = b"Hello" #<class 'bytes'>
x = bytearray(5) #...bytearray(b'\x00\x00\x00\x00\x00') <class 'bytearray'>...
x = memoryview(bytes(5)) # <memory at 0x000002512C736080> <class 'memoryview'>
x = None # <class 'NoneType'>

# print(x)
# print(type(x))

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
*** Setting the Specific Data Type ***
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
'''