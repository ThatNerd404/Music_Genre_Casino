import random
Genre_List = ["Crossover Music","Danger Music", "Drone Music", "Electroacoustic", "Industrial Music","Instrumental Music", "Lofi Music",
                    "Musical Improvisation", "Musique concrete", "Noise", "Outsider Music", "Progessive Music", "Psychedelic Music", "Underground music",
                    "African Blues", "Blues Rock", "British Bules", "Canadian Blues", "Chicago Blues", "Classic Female Blues", "Contempoary R&B",
                    "Country Blues", "Delta Blues", "Desert Blues", "Detroit Blues", "Electric Blues", "Gospel Blues", "Hill Country Blues",
                    "Hokum Blues", "Jump Blues", "Kansas City Blues", "Louisiana Blues", "Memphis Blues", "New Orleans Blues", "Piedmont Blues", 
                    "Punk Blues", "Rhythm and Blues", "Soul Blues", "St. Louis Blues", "Swamp Blues", "Talking Blues", "Texas Blues", "West Coast Blues",
                    "Alternative Country", "Australian Country", "Bakersfield Sound", "Bluegrass", "Blue Yodeling", "Bro-Country", "Cajun",
                    "Canadian Country", "Christian Country", "Classic Country", "Country and Irish", "Country Blues", "Country en Espanol",
                    "Country Folk", "Country Pop", "Country Rap", "Country Rock", "Cowboy Pop", "Dansband", "Gulf and Western", "Hokum", "Honky Tonk",
                    "Instrumental Country", "Lubbock Sound", "Nashville Sound", "Neotraditional Country", "Old-time", "Outlaw Country", "Pop Country",
                    "Progressive Country", "Regional Mexican", "Rockabilly", "Southern Rock", "Southern Soul", "Sertanejo", "Talking Blues",
                    "Traditional Country", "Truck-Driving Country", "Western Music", "Zydeco", "Adult Contemporary Music", "Adult Standards",
                    "Background Music", "Barococo", "Beautiful Music", "Chill-Out", "Downtempo", "Furniture Music", "Light Music", "Lounge Music",
                    "Middle of the Road", "New-Age Music", "Soft Rock", "Ambient dub", "Dark ambient" , "Ambient industrial",  "Dungeon synth",
                    "Isolationism", "Dreampunk", "Illbient", "Space music", "Footwork", "Future bass", "Kawaii future bass", "Jungle terror",
                    "Midtempo bass", "Trap", "UK bass", "Wave", "Hardwave", "Acid breaks", "Baltimore club", "Jersey club", "Philly club", "Big beat",
                    "Breakbeat hardcore", "Darkcore", "Hardcore breaks", "Broken beat", "Florida breaks", "Nu Skool Breaks", "Progressive Breaks",
                    "Psychedelic Breakbeat", "Downtempo", "Psybient", "Trip Hop", "Trip Rock", "Afro Music", "Electro-Disco", "Eurobeat",
                    "Italo Disco", "Space Disco", "Eurodisco", "Nu-Disco", "Boogie", "City Pop", "Darkstep", "Drumfunk", "Drumstep", "Hardstep",
                    "Jazzstep", "Liquid Funk", "Neurofunk", "Sambass", "Techstep", "Dub Poetry", "Dubtronica", "Dance-Rock", "Dance-Punk", "Dance-Pop",
                    "Hyperpop", "Sophisti-Pop", "Synth-Pop", "Wonky Pop", "Indietronica", "Krautrock", "New Wave", "Ethereal Wave", "Minimal Wave",
                    "New Romantic", "Post-Rock", "Space Rock", "Synth-Metal", "Electrogrind", "Synth-Punk", "Electronica", "Folktronica", "Nu Jazz", 
                    "Progressive Electronic", "Jungle", "Hardcore", "Bouncy Techno", "Breakcore", "Raggacore", "Digital Hardcore", "Frenchcore",
                    "Gabber", "Happy Hardcore", "UK Hardcore", "Industrial Hardcore", "J-Core", "Speedcore", "Vaporwave", "Electro", "Emo Rap", 
                    "Afroswing", "Instrumental Hip Hop", "Lofi Hip Hop", "Miami Bass", "Mumble Rap", "Trap", "Acid House", "Afro House", "Ambient House",
                    "Balearic Beat", "Ballroom", "Bass House", "Brazilian Bass", "Blog House", "Chicago Hard House", "Chicago House", "Deep House", 
                    "Disco House", "Diva House", "Electro-Industrial", "Aggrotech", "Electronic Body Music", "Futurepop", "New Beat", "Industrial Hip Hop", 
                    "Cyber Metal", "Industrial Rock", "Martial Industrial", "Witch House", "Drill n Bass", "R&B", "Alternative R&B", "Contemporary R&B",
                    "Neo Soul", "New Jack Swing", "Techno", "Acid Techno", "Ambient Techno", "Birmingham Sound", "Bleep Techno", "Detroit Techno",
                    "Dub Techno", "Hard Techno", "Industrial Techno", "Minimal Techno", "Schaffel", "Toytown Techno", "Acid Trance", "Balearic Trance",
                    "Dream Trance", "Eurotrance", "Goa Trance", "Hard Trance", "Progressive Trance", "Psychedelic Trance", "Tech Trance", "Video Game Music",
                    "American Folk Revival", "Americana", "Anti-Folk", "British Folk Revival", "Cajun Music", "Celtic Music", "Chalga", "Corrido",
                    "Creole Music", "Filk", "Folk Noir", "Folk Rock", "Folktronica", "Freak Folk", "Indie Folk", "Industrial Folk", "Mariachi", "Ranchera",
                    "Neofolk", "New Weird America", "Progessive Folk", "Protest Song", "Psychedelic Folk", "Singer-Songwriter", "Skiffle", "Sung Poetry",
                    "Alternative Hip Hop", "Boom Bap", "Bounce", "British Hip Hop", "Chopped and Screwed", "Christian Hip Hop", "Cloud Rap", "Comedy Hip Hop",
                    "Crunk", "Crunkcore", "East Coast Hip Hop", "Freestyle Rap", "Funk Carioca", "Frat Rap", "G-Funk", "Hardcore Hip Hop", "Gangsta Rap",
                    "Horrorcore", "Memphis Rap", "Hyphy", "Instrumental Hip Hop", "Latin Hip Hop", "Chicano Rap", "Lofi Hip Hop", "Miami Bass", "Mumble Rap",
                    "Nerdcore", "Political Hip Hop", "Progressive Rap", "Jewish Hip Hop", "Snap Music", "Southern Hip Hop", "Trap Music", "Drill Music",
                    "Latin Trap", "Phonk", "Plugg", "Rage", "Underground Hip Hop", "West Coast Hip Hop", "Country Rap", "Emo Rap", "Hip Hop Soul", 
                    "Industrial Hip Hop", "Jazz Rap", "New Jack Swing", "Pop Rap", "Punk Rap", "Ragga Hip Hop", "Rap Opera", "Rap Rock", "Rap Metal", 
                    "Rapcore", "Trip Hop",
                    ]


def Main():
    Genre_Choice = random.choice(Genre_List)
    print(Genre_Choice)


 
if __name__ == "__main__":
    Main()