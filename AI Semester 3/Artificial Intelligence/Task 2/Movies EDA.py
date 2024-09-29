class Movie:
    def __init__(self,name,budgut):
        self.name=name
        self.budgut=budgut

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
    def add(self,name,budgut):
        self.movies.append(Movie(name,budgut))
    def average(self):
        t_budgut= sum(movie.budgut for movie in self.movies)
        return t_budgut/len(self.movies)
    def high_budgut(self):
        avg_budgut=self.average()
        print(f"\nAverage budgut: $ {avg_budgut}")
        count=0
        for movie in self.movies:
            if movie.budgut > avg_budgut:
                print(f"\n{movie.name} exceeded avg Budget By $ {movie.budget- avg_budgut}")
                count=count+ 1
        print(f"\n {count} movies have higher budget then average.")
obj=MoviesData()
try:
    movies_num= int(input("How many movies you wanna enter? "))
    for _ in range(movies_num):
        name= input("Enter movie name: ")
        budgut= int(input("Enter movie budget: "))
        obj.add(name,budgut)
except:
    print('Invalid input, Enter valid number.')
obj.high_budgut()  
