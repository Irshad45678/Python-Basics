#9. Sets
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")

# Operations
a = {1,2,3}
b = {3,4,5}
print(a | b)  # Union {1,2,3,4,5}
print(a & b)  # Intersection {3}
print(a - b)  # Difference {1,2}