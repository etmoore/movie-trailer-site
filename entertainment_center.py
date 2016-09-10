import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                                "Lovers try to forget their past and start over",
                                "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                                "https://www.youtube.com/watch?v=rb9a00bXf-U")

garden_state = media.Movie("Garden State",
                            "Zach Braff returns home for his mother's funeral",
                            "https://upload.wikimedia.org/wikipedia/en/3/3c/Garden_State_Poster.jpg",
                            "https://www.youtube.com/watch?v=u82n0e1mgmQ")

into_the_wild = media.Movie("Into the wild",
                            "A young man leaves society",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",
                            "https://www.youtube.com/watch?v=g7ArZ7VD-QQ")

the_godfather = media.Movie("The Godfather",
                            "A mob boss transfers the family business to his son",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

movies = [toy_story, avatar, eternal_sunshine, garden_state, into_the_wild, the_godfather]
fresh_tomatoes.open_movies_page(movies)
