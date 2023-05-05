'''

Lyrics generator: Display the names of 5 songs, ask the user choose one song. 
After user chosen a song, display the lyrics of that song.

'''

print(" 1:Ride it \n 2:Wannable \n 3:Bad Habit \n 4:Shivers \n 5:Old Town Road")

dic_lyric={
    "1":"ride it all night long",
    "2":"Can I tell you what I really want",
    "3":"Every time the sun goes down",
    "4":"Oh heah I want it all",
    "5":"I'm gonna take my horse to the old town road"
}
print("==============================")
num=input("Chose a song by entering number(1~5):")
if num == "1"or "2"or"3"or"4"or"5":
    lyric=dic_lyric.get(num)
    print(lyric)
else:
    print("no such song")  