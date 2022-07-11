poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author_fixed)

line_one = "The sky has given over"

line_one_words = line_one.split()

print(line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Carmen Boullosa,Kamala Suraiyya"

author_names = authors.split(",")

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""


spring_storm_lines = spring_storm_text.split("\n")

print(spring_storm_lines)

repears_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

repears_line_one = ' '.join(repears_line_one_words)

print(repears_line_one)

featuring = "       rob thomas       "

print(featuring.strip())

with_spaces = "you got the kind of love that i want"

with_underscores = with_spaces.replace(" ", "_")

print(with_underscores)

print("smooth".find("t"))

print("smooth".find("oo"))


def favorite_song_statement(song, artist):
    return "My favorite song is {} by {}".format(song, artist)

print(favorite_song_statement("Supercut", "Lorde"))

def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}".format(song=song, artist=artist)