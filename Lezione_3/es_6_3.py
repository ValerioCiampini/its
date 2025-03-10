glossary:dict = {"append":"Add an item to the end of the list.", "extend":"Extend the list by appending all the items from the iterable.", "insert":"Insert an item at a given position.", "remove":"Remove the first item from the list whose value is equal to x.", "pop":"Remove the item at the given position in the list, and return it."}

for key, value in glossary.items():
    print(f"{key}:\n{value}")