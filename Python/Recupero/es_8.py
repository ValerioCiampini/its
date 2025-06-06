class Movie:

    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool = False):
        self.movie_id:str = movie_id
        self.title:str = title
        self.director:str = director
        self.is_rented:bool = is_rented

    def rent(self) -> None:
        if self.is_rented == False:
            self.is_rented = True
        else:
            print(f"Il film '{self.title}' è già noleggiato.")

    def return_movie(self) -> None:
        if self.is_rented == True:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")

class Customer:

    def __init__(self, customer_id:str, name:str):
        self.customer_id:str = customer_id
        self.name:str = name
        self.rented_movie:list[Movie] = []

    def rent_movie(self, movie: Movie):
        if movie.is_rented == False:
            self.rented_movie.append(movie)
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")
    
    def return_movie(self, movie: Movie):
        if movie in self.rented_movie:
            self.rented_movie.remove(movie)
            movie.return_movie()
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):
        self.movies:dict[str, Movie] = movies
        self.customers: dict[str, Customer] = customers

    def add_movie(self, movie_id: str, title: str, director: str):
        m:Movie = Movie(movie_id, title, director)
        if movie_id not in self.movies:    
            self.movies[movie_id] = m
        else:
            print(f"Il film con ID '{movie_id}' esiste già.")

    def register_customer(self, customer_id: str, name: str): 
        c:Customer = Customer(customer_id, name)
        if customer_id not in self.customers:
            self.customers[customer_id] = c
        else:
            print(f"l cliente con ID '{customer_id}' è già registrato.")

    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id:str, movie_id:str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str): 
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movie
        else:
            print("Cliente non trovato.")
            return []
        
    def get_all_movies(self):
        film_noleggiati = []
        for customer_id, customer in self.customers.items():
            film_noleggiati += customer.rented_movie

        return film_noleggiati
    à,m