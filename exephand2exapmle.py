items = [1, 2, 3, 4, 5]

try:
    item = items[6]
    print(item)
except IndexError as e:
    print("An IndexError occurred:",e)
except Exception as e:
    print("An unexpected error occurred:",e)

