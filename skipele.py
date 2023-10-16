def skip_elements(elements):
    return [element for i, element in enumerate(elements)
             if i % 2 == 0]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  
print(skip_elements(['orange', 'apple', 'kiwi', 'peach','gava']))  
