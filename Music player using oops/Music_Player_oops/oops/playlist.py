
class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.tracks = []
        self.ratings = []

    def add_track(self, track):
        self.tracks.append(track)


    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)


    def add_rating(self, rating):
        self.ratings.append(rating)


    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def search_track_by_name(self, track_name):
        for track in self.tracks:
            if track.name.lower() == track_name.lower():
                return track
        return None