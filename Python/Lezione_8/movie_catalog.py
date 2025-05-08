class MovieCatalog:

    def __init__(self):
        self.catalog:dict[str, list[str]] = {}

    def add_movie(self, director_name:str, movies:list[str]):
        if director_name not in self.catalog:
            self.catalog[director_name] = movies
        else:  
            for i in movies:    
                if i not in self.catalog:
                    self.catalog[director_name].append(i)    

    def remove_movies(self, director_name:str, movie_name:str):
        if movie_name in self.catalog[director_name] and director_name in self.catalog:
            self.catalog[director_name].remove(movie_name)
        if not self.catalog[director_name]:
            self.catalog.pop(director_name)

    def list_directors(self):
        return self.catalog.keys()
    
    def movie_by_director(self, director_name:str):
        if director_name in self.catalog:
            return self.catalog[director_name]

    def search_movies_by_title(self, title:str):
        result:dict[str, list[str]] = {}
        for key, value in self.catalog.items():
            movies:list[str] = []
            for i in value:
                if i.lower() == title.lower():
                    movies.append(i)
                
                if movies:
                    result[key] = movies
        
        if result:
            return result 
        else:
            return "nessun film trovato"
        
catalog1:MovieCatalog = MovieCatalog()
