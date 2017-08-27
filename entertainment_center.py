import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet" ,"https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg" ,"https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "An rat that wants to be a chef", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris","Mais um filme merda do Woody Allen","https://upload.wikimedia.org/wikipedia/pt/thumb/b/be/Meia-noite-em-paris-poster1.jpg/200px-Meia-noite-em-paris-poster1.jpg", "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games", "A Girl Has to Fight in a jungle", "https://upload.wikimedia.org/wikipedia/pt/thumb/4/42/HungerGamesPoster.jpg/200px-HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)