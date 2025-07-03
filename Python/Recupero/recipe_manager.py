class RecipeManager:

    def __init__(self):
        self.d:dict = {}

    def create_recipe(self, name, ingredients:list):
        d:dict = {}
        if name in d:
            return "la ricetta esiste già"
        
        d[name] = ingredients

        self.d = d
        return self.d
    
    def add_ingredient(self, recipe_name, ingredient):
        if ingredient in self.d.values() or not recipe_name in self.d:
            return "l'ingrediente non può essere aggiunto"
        
        return self.d[recipe_name].append(ingredient)
    
    def remove_ingredient(self, recipe_name, ingredient):
        if not ingredient in self.d.values() or not recipe_name in self.d:
            return "l'ingrediente non può essere tolto"
        
        return self.d[recipe_name].remove(ingredient)
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if not old_ingredient in self.d.values() or not recipe_name in self.d:
            return "l'ingrediente non può essere aggiornato"
        
        return self.d[recipe_name].remove(old_ingredient) and self.d[recipe_name].append(new_ingredient)
    
    def list_recipes(self):
        print(self.d.keys())

    def list_ingredients(self, recipe_name):
        if not recipe_name in self.d:
            print("la ricetta non esiste")

        return self.d[recipe_name]
    
    def search_recipe_by_ingredient(self, ingredient):
        isnotin:bool
        l = []
        for key, value in self.d.items():
            if ingredient != value:
                isnotin = True
            else:
                l.append(key)


        if isnotin == True:
            print("l'ingrediente non è presente")

        return l


                
    
    