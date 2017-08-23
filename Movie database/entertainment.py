import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story","A boy whose toys comes to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

transformers=media.Movie("Transformers","Alien Robots invading earth",
                      "http://cdn.collider.com/wp-content/uploads/2016/12/transformers-the-last-knight-poster-1.jpeg",
                      "https://www.youtube.com/watch?v=yCOvcyfRPRk")

lordof_the_rings=media.Movie("The Lord of the Rings","One ring to rule them all one ring to bind them",
                      "https://images-na.ssl-images-amazon.com/images/I/51%2BDyPydG4L._SX355_.jpg",
                      "https://www.youtube.com/watch?v=V75dMMIW2B4")


#print(toy_story.title)
#media.Movie.show_trailer(toy_story.trailer_youtube_url)

movies=[toy_story,transformers,lordof_the_rings]
fresh_tomatoes.open_movies_page(movies)
