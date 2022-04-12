class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made - Author is {self.author} and title is {self.title}")

    def sing(self, max_lines=-1):
        print(f"{self.author} - {self.title}")
        self._print_lyrics(self.lyrics,max_lines)
        return self

    def yell(self, max_lines=-1):
        print(f"{self.author} - {self.title}")
        self._print_lyrics(self.lyrics,max_lines)
        return self

    def _print_lyrics(self, lyrics, max_lines = -1):
        if max_lines == -1:
            max_lines = len(lyrics)
        for item in lyrics[:max_lines]:
            print(item)

new_song =Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
here = new_song.sing()
here = new_song.yell()
here = new_song.sing(1).yell().sing(1)

