class Movie:
    def __init__(self):
        self.name = None
        self.genre = None
        self.rating = 0.0

    def set_name(self, name):
        self.name = name

    def set_genre(self, genre):
        self.genre = genre

    def set_rating(self, rating):
        self.rating = rating

    def isHit(self):
        return self.rating >= 8.0

m = Movie()
m.set_name("Inception")
m.set_genre("Sci-Fi")
m.set_rating(8.8)

print(f"Is Hit Movie? { m.isHit()}")