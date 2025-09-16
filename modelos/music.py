class Music:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f'''
    Music name: {self.name};
    Artist: {self.artist};
    Duration: {self.duration}.
    '''
    

    

music1 = Music('Bohemia Rhaposy', 'Queen', 355)

print(music1)
