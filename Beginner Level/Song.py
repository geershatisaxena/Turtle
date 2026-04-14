import time
import sys

def print_lyrics():
    lyrics = [
        "Dil jala ke muskurane ki jo aadat hui hai mujhe",
        " Lag raha hai qayde se ab mohabbat hui hai mujhe",
        " Dil jala ke muskurane ki jo aadat hui hai mujhe",
        " Lag raha hai qayde se ab mohabbat hui hai mujhe",
        " Meri tumhi se hai jawabdari, naraazgi bhi dher saari",
        " Tumhein harane ki zid mein, ye zindagi tumhee se haari",
        " Agar kabhi tumhein rulaya, kaha mujhe bhi chain aaya",
        " Asal men dil nahi tumhara, khud hee ka dukhaya"
    ]

    delays = [
        0.3, 0.5, 0.4, 0.3, 0.3, 0.8, 0.8,0.6
    ]

    print("Pal Pal \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            if len(delays) > i:
                time.sleep(delays[i])
            else:
                time.sleep(0.8)

print_lyrics()
