#5. Strings
text = "Python"

# Indexing & Slicing
print(text[0])   # 'P'
print(text[-1])  # 'n'
print(text[0:4]) # 'Pyth'

# Methods
print(text.upper())   # 'PYTHON'
print(text.lower())   # 'python'
print(text.replace("P","J")) # 'Jython'
print(len(text))      # 6
print(text.split("y")) # ['P', 'thon']