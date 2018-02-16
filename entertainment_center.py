import media
import fresh_tomatoes

# Making instances of the class Movie in media
bakuman = media.Movie("Bakuman",
                      "https://ourteentrends.com/wp-content/uploads/2011/"
                      "11/Bakuman8.jpg",
                      "https://www.youtube.com/watch?v=IgdBcryhIII")

death_note = media.Movie("Death Note",
                         "https://s3.bukalapak.com/img/821614921/w-1000/"
                         "Film_Anime_Death_Note.jpg",
                         "https://www.youtube.com/watch?v=tJZtOrm-WPk")

attack_on_titan = media.Movie("Attack on titan",
                              "https://www.crunchyroll.com/i/spire3/00db49e00"
                              "cea59da36c4110602d4fb8d1491069153_full.jpg",
                              "https://www.youtube.com/watch?v=MGRm4IzK1SQ")

rainbow = media.Movie("Rainbow",
                      "https://myanimelist.cdn-dena.com/images/anime/"
                      "8/22117l.jpg",
                      "https://www.youtube.com/watch?v=mfpDLHEOdVU")

parasyte = media.Movie("Parasyte",
                       "http://www.goodanime.co/images/"
                       "kiseijuu_sei_no_kakuritsu.jpg",
                       "https://www.youtube.com/watch?v=2SOxiAP6Bo0")

boku = media.Movie("Boku No Hero Academia",
                   "http://p2.i.ntere.st/"
                   "811403a9f6b7f7ee5d569c0925b70253_480.jpg",
                   "https://www.youtube.com/watch?v=o94hQNVFw0c")

movies = [bakuman, death_note, attack_on_titan, rainbow, parasyte, boku]

# to make and open the HTML webpage
fresh_tomatoes.open_movies_page(movies)
