import random
import tkinter as tk
from tkinter import ttk

Genre_Dict = {"Avant-Garde & Experimental":["Crossover Music", "Danger Music", "Drone Music", "Electroacoustic", "Industrial Music",
                                            "Instrumental Music", "Lo-fi", "Musical Improvisation", "Musique Concrete", "Noise",
                                            "Outsider Music", "Progressive Music", "Psychedelic Music", "Underground Music"
                                            ],
              "Blues":["African Blues", "Blues Rock", "British Blues", "Canadian Blues", "Chicago Blues", "Classic Female Blues",
                       "Contemporary R&B", "Country Blues", "Delta Blues", "Desert Blues", "Detroit Blues", "Electric Blues",
                       "Gospel Blues", "Hill Country Blues", "Hokum Blues", "Jump Blues", "Kansas City Blues", "Louisana Blues",
                       "Memphis Blues", "New Orleans Blues", "Piedmont Blues", "Punk Blues", "Rhythm and Blues", "Soul Blues",
                       "St. Louis Blues", "Swamp Blues", "Talking Blues", "Texas Blues", "West Coast Blues"
                       ],
              "Country":["Alternative Country", "Australian Country", "Bakersfield", "Bluegrass", "Blue Yodeling", "Bro-Country",
                         "Cajun", "Canadian Country", "Christian Country", "Classic Country", "Country and Irish", "Country Blues",
                         "Country En Espanol", "Country Folk", "Country Pop", "Country Rap", "Country Rock", "Cowboy Pop", "Dansband", 
                         "Gulf and Western", "Hokum", "Honky Tonk", "Instrumental Country", "Lubbock Sound", "Nashville Sound",
                         "Neotraditional Country", "Old-Time", "Outlaw Country", "Pop Country", "Progessive Country", "Regional Mexican",
                         "Rockabilly", "Southern Rock", "Southern Soul", "Sertanejo", "Talking Blues", "Traditional Country",
                         "Truck-Driving Country", "Western Music", "Zydeco"
                         ],
              "Easy Listening":["Adult Contemporary Music", "Adult Standards", "Background Music", "Barococo", "Beautiful Music", 
                                "Chill-Out", "Downtempo", "Furniture Music", "Light Music", "Lounge Music", "Middle of the Road", 
                                "New-Age Music", "Soft Rock"
                                ],
              "Electronic":["Ambient", "Bass Music", "Breakcore", "Breakbeat", "Chill-Out", "Disco", "Drum and Bass", "Dub", "Electronic Rock", 
                            "Electronica", "Ethnic Electronica", "Experimental Electronic", "Funk Fusion Genres", "Jungle",
                            "Hard Dance", "Hardcore", "Hauntology", "Hip Hop Fusion Genres", "House Music", "Industrial and Post-Industrial",
                            "Intelligent Dance Music", "R&B and Soul Fusion Genres", "Techno", "Trance Music", "UK Garage", "Video Game Music"
                            ],
              "Folk":["American Folk Revival", "Americana", "Anti-Folk", "British Folk Revival", "Cajun Music", "Celtic Music", "Chalga",
                      "Corrido", "Creole Music", "Filk", "Folk Noir", "Folk Rock", "Folktronica", "Freak Folk", "Indie Folk", "Industrial Folk", 
                      "Mariachi", "Ranchera", "Neofolk", "New Weird America", "Progressive Folk", "Protest Song", "Psychedelic Folk", "Skiffle", 
                      "Sung Poetry", "Tarantella", "Traditional Blues Verses"
                      ],
              "Hip Hop":["Alternative Hip Hop", "Boom Bap", "Bounce", "British Hip Hop", "Chopped and Screwed", "Chopper", "Christian Hip Hop",
                         "Cloud Rap", "Comedy Hip Hop", "Crunk", "East Coast Hip Hop", "Freestyle Rap", "Funk Carioca", "Frat Rap",
                         "G-Funk", "Hardcore Hip Hop", "Horrorcore", "Hyphy", "Instrumental Hip Hop", "Latin Hip Hop", "Lofi Hip Hop", 
                         "Miami Bass", "Mumble Rap", "Nerdcore", "Political Hip Hop", "Progessive Rap", "Religious Hip Hop",
                         "Snap Music", "Southern Hip Hop", "Trap Music", "Turntablism", "Underground Hip Hop", "West Coast Hip Hop", "Country Rap",
                         "Electro", "Emo Rap", "Hip Hop Soul", "Hip House", "Industrial Hip Hop", "Jazz Rap", "New Jack Swing", "Pop Rap",
                         "Punk Rap", "Ragga Hip Hop", "Rap Opera", "Rap Rock", "Trip Hop"
                         ],
              "Jazz":["Acid Jazz", "Afro-Cuban Jazz", "Alt-Jazz", "Avant-Garde Jazz", "Bebop", "Big Band", "Boogie-Woogie", "Bossa Nova",
                      "Brazilian Jazz", "British Dance Band", "Cape Jazz", "Chamber Jazz", "Continental Jazz", "Cool Jazz", "Crossover Jazz",
                      "Dixieland", "Ethno Jazz", "European Free Jazz", "Free Funk", "Free Improvisation", "Free Jazz", "Gypsy Jazz", "Hard Bop", 
                      "Jazz Blues", "Jazz-Funk", "Jazz Fusion", "Jazz Rap", "Jazz Rock", "Jazztronica", "Kansas City Jazz", "Latin Jazz", "Livetronica",
                      "M-Base", "Mainstream Jazz", "Modal Jazz", "Neo-Bop Jazz", "Neo-Swing", "Nu Jazz", "Orchestral Jazz", "Post-Bop", 
                      "Progessive Jazz", "Punk Jazz", "Samba-Jazz", "Shibuya-Kei", "Ska Jazz", "Smooth Jazz", "Soul Jazz", "Straight-Ahead Jazz",
                      "Stride Jazz", "Swing", "Trad Jazz", "Third Stream", "Vocal Jazz", "West Coast Jazz"
                      ],
              "Pop":["Adult Contemporary", "Adult Hits", "Alternative Pop", "Ambient Pop", "Arabic Pop Music", "Art Pop", "Avant-Pop", "Baroque Pop",
                     "Beach Music", "Bedroom Pop", "Brill Building", "Britpop", "Bubblegum Pop", "C-Pop", "Cancion", "Canzone", "Chalga",
                     "Chamber Pop", "Chanson", "Christian Pop", "Classic Hits", "Classical Crossover", "Contemporary Hit Radio", "Country Pop", 
                     "Cringe Pop", "Dance-Pop", "Dark Pop", "Disco Polo", "Electropop", "Europop", "Fado", "Folk Pop", "Hyperpop", "Indie Pop",
                     "Indian Pop", "Iranian Pop", "J-pop", "Jangle Pop", "Jazz Pop", "K-Pop", "Latin Ballad", "Latin Pop", "New Pop", "New Romantic",
                     "Oldies", "Operatic Pop", "OPM", "Pop Rap", "Pop Rock", "Pop Soul", "Progessive Pop", "Psychedelic Pop", "Rebetiko", 
                     "Rhythmic Adult Contemporary", "Rhythmic Contemporary", "Rhythmic Oldies", "Schlager", "Sophisti-Pop", "Space Age Pop",
                     "Sunshine Pop", "Swamp Pop", "Synth-Pop", "Teen Pop", "Traditional Pop", "Turbo-Folk", "Turkish Pop", "Urban Adult Contemporary",
                     "Urban Contemporary Music", "Vispop", "Wonky Pop", "Worldbeat", "Ye-Ye"
                     ],
              "R&B & Soul":["Alternative R&B", "Contemporary R&B", "Disco", "Freestyle", "Funk", "Gospel Music", "New Jack Swing", "Post-Disco","Rhythm and Blues", 
                            "Soul"
                            ],
              "Rock":["Active Rock", "Adult Album Alternative", "Adult-Oriented Rock", "Afro Rock", "Album Oriented Rock", "Alternative Rock", "Grunge",
                      "Shoegaze", "Indie Rock", "Midwest Emo", "Math Rock", "American Rock", "Anatolian Rock", "Arabic Rock", "Arena Rock", "Beat",
                      "Blues Rock", "Brazilian Rock", "British Rhythm and Blues", "British Rock Music", "Chamber Pop", "Chinese Rock", "Christian Rock", 
                      "Classic Alternative", "Classic Rock", "Comedy Rock", "Country Rock", "Dark Cabaret", "Death 'n' Roll", "Deathrock", "Desert Rock",
                      "Electronic Rock", "Emo", "Experimental Rock", "Folk Rock", "Garage Rock", "Geek Rock", "Glam Rock", "Gothic Rock", "Hard Rock", 
                      "Heartland Rock", "Heavy Metal", "Indian Rock", "Iranian Rock", "Instrumental Rock", "Japanese Rock", "Jazz Fusion", "Korean Rock",
                      "Latin Rock", "Mainstream Rock", "Mangue Bit", "Modern Rock", "New Wave of Classic Rock", "Occult Rock", "Paisley Underground", 
                      "Pop Rock", "Progressive Rock", "Psychedelic Rock", "Pub Rock", "Punk Rock", "Rap Rock", "Reggae Rock", "Rock and Roll",
                      "Rock Music in France", "Rock Opera", "Roots Rock", "Southern Rock", "Stoner Rock", "Swamp Rock", "Sufi Rock", "Surf Rock",
                      "Tropical Rock", "Viking Rock", "Visual Kei", "Wizard Rock", "Worldbeat", "World Fusion"],
              "Metal":["Alternative Metal", "Avant-Garde Metal", "Black Metal", "Christian Metal", "Death Metal", "Doom Metal", "Extreme Metal",
                       "Folk Metal", "Glam Metal", "Gothic Metal", "Industrial Metal", "Kawaii Metal", "Latin Metal", "Math Metal", "Metalcore",
                       "Neoclassical Metal", "Neue Deutsche Harte", "New Wave of American Heavy Metal", "New Wave of British Heavy Metal", "Nintendocore",
                       "Pirate Metal", "Pop Metal", "Power Metal", "Progessive Metal", "Sludge Metal", "Speed Metal", "Symphonic Metal", "Thrash Metal",
                       ],
              "Punk":["Afro-Punk", "Anarcho Punk", "Art Punk", "Avant Punk", "Christian Punk", "Crust Punk", "Deathrock", "Electropunk", "Cyberpunk",
                      "Folk Punk", "Garage Punk", "German Punk", "Glam Punk", "Gothic Punk", "Grindcore", "Hardcore Punk", "Horror Punk", "Screamo",
                      "Pop Punk", "Post-Punk", "Proto-Punk", "Psychobilly", "Punk Blues", "Punk Jazz", "Punk Pathetique", "Punk Rap", "Reggae Punk",
                      "Riot Grrrl", "Skate Punk", "Street Punk", "Surf Punk", "Trallpunk" 
                      ]
              }

class myApp:
        
        def __init__(self, root):
             self.root = root
             self.root.title("Music Genre Casino")
             self.root.iconbitmap('assests\icons8-slot-machine-48.ico')
             # window size 
             
             self.casino_img = tk.PhotoImage(file="assests\Casino_BG_tiny.png")
             self.window_width = self.casino_img.width()
             self.window_height =self.casino_img.height()
             # get the screen dimension
             self.screen_width = root.winfo_screenwidth()
             self.screen_height = root.winfo_screenheight()
             self.root.resizable(False, False)

             # find the center point
             self.center_x_screen = int(self.screen_width/2 - self.window_width / 2)
             self.center_y_screen = int(self.screen_height/2 - self.window_height / 2)

             # set the position of the window to the center of the screen
             self.root.geometry(f'{self.window_width}x{self.window_height}+{self.center_x_screen}+{self.center_y_screen}')
            
            
             self.bg_image = tk.Label(self.root, image=self.casino_img, anchor=tk.CENTER)
             self.bg_image.place(x=0,y=0)
             
              # Label to display the genre and subgenre
             self.result_label = ttk.Label(self.root, text="Press the button to get a genre!", font=("Helvetica", 14), anchor=tk.CENTER)
             self.result_label.pack(ipadx=0,ipady=0)

        # Button to trigger Crank_That_Bitch
             self.generate_button = ttk.Button(self.root, text="Generate Genre", command=self.Crank_That_Bitch)
             self.generate_button.pack(ipadx=0,ipady=0)
        
        def Random_Genre(self):
             Random_Genre = random.choice(list(Genre_Dict.keys()))
             Random_Sub_Genre = random.choice(Genre_Dict[Random_Genre])
             return f"{Random_Genre}: {Random_Sub_Genre}"
        
        def Crank_That_Bitch(self):
        # Call Random_Genre and update the label with its result
             result_text = self.Random_Genre()
             self.result_label.config(text=result_text)
             self.generate_button.config(state=tk.DISABLED) 
             self.spin_count = 0 
             self.spin_speed = 0
             self.Spinning()
        
        def Spinning(self):
        # Flash 18 times starting at 25ms and ending at 450ms
                if self.spin_count < 18:
                        result_text = self.Random_Genre()
                        self.result_label.config(text=result_text)
                        self.spin_count += 1
                        self.spin_speed += 25
                        self.root.after(self.spin_speed,self.Spinning)
                else:
                        self.Stop_Spin()
                        
        def Stop_Spin(self):
                final_result_text = self.Random_Genre()
                self.generate_button.config(state=tk.NORMAL)
                self.result_label.config(text=final_result_text)
                

                      

        
     
def Main():

    root = tk.Tk() # initialize the main window
    app = myApp(root)
    root.mainloop() # run the application
    
   
    
    


 
if __name__ == "__main__":
    Main()