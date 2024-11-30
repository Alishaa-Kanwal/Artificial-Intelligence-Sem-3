class Movie:
    def __init__(self, name, budget):
        self.name= name
        self.budget= budget

class MoviesData:
    def __init__(self):
        self.movies= [
            Movie("Eternal Sunshine of the Spotless Mind", 20000000),
            Movie("Memento", 9000000),
            Movie("Requiem for a Dream", 4500000),
            Movie("Pirates of the Caribbean: On Stranger Tides", 379000000),
            Movie("Avengers: Age of Ultron", 365000000),
            Movie("Avengers: Endgame", 356000000),
            Movie("Incredibles 2", 200000000)
        ]
    def add(self, name, budget):
        self.movies.append(Movie(name, budget))
    def average(self):
        t_budget= sum(movie.budget for movie in self.movies)
        return t_budget/len(self.movies)
    def high_budget(self):
        avg_budget=self.average()
        print(f"\nAverage budget: $ {avg_budget}")
        count=0
        for movie in self.movies:
            if movie.budget > avg_budget:
                print(f"\n{movie.name} exceeded avg Budget By $ {movie.budget- avg_budget}")
                count+=1
        print(f"\n {count} movies have higher budget then average.")
    
obj=MoviesData()

try:
    no_of_movies= int(input("How many movies you wanna enter? "))
    for _ in range(no_of_movies):
        name= input("Enter movie name: ")
        budget= int(input("Enter movie budget: "))
        obj.add(name,budget)
except:
    print('Invalid input, Enter valid number.')

obj.high_budget()  
