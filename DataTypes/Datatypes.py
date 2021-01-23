'''A demostration of data types in Python 3'''


# Text
a = 'FrivolousCoding'
print(a, "is", type(a))
print()
# Numeric types

#  integer
n1 = 12
print(n1, "is", type(n1))
print()

#  float
n2 = 12.1
print(n2, "is", type(n2))
print()

#  complex
n3 = 1 + 2*1j
print(n3, "is", type(n3))
print()

# Sequences
#  list

l1 = [1, 2, 3]
print(l1, "is a list. All elements in the list are integers.")
print()

l2 = [1, 2.1, 1 + 2*1j, "ABCD", l1]
print(l2, "is another list. It has different data types as its elements.")
print()

#  tuple
l1 = (1, 2, 3)
print(l1, "is a tuple. All elements in the tuple are integers.")
print()

l2 = (1, 2.1, 1 + 2*1j, "ABCD", l1)
print(l2, "is another tuple.\n It has different data types as its elements.\n You cannot change the elements of a tuple. it is immutable.")
print()

#  range
a = range(0, 7, 2)
print(a, "is ", type(a))
print()

# Mapping
#  dict - key value mapping

a1 = {'A': 1, 1.2:'B'}
print("a1 = ",a1, "is a dictionary. It maps key-value pairs. ")
print("  You can access its elements using the keys.")
print("  a1['A'] = ", a1['A'])
print("  a1[1.2] = ", a1[1.2])
