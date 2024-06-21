import random
from Music_Player_oops.oops.audio_track import AudioTrack as at
from Music_Player_oops.oops.playlist import Playlist as pl



class MusicPlayerApp:
    def __init__(self):
        self.playlists = []
        self.tracks = []

    def create_playlist(self, name, genre):
        playlist = pl(name, genre)
        self.playlists.append(playlist)
        return playlist

    def add_track_to_playlist(self, track, playlist_name):
        for playlist in self.playlists:
            if playlist.name.lower() == playlist_name.lower():
                playlist.add_track(track)
                return True
        return False

    def search_track_by_name(self, track_name):
        results = []
        for playlist in self.playlists:
            track = playlist.search_track_by_name(track_name)
            if track:
                results.append((playlist.name, track))
        return results

    def search_playlist_by_name(self, playlist_name):
        for playlist in self.playlists:
            if playlist.name.lower() == playlist_name.lower():
                return playlist
        return None

    def generate_random_ratings(self):
        # Simulate random ratings by 3 users
        for _ in range(3):
            random_rating = random.randint(1, 5)
            # Assuming we have some playlists and tracks already created
            playlist = random.choice(self.playlists)
            track = random.choice(playlist.tracks)
            playlist.add_rating(random_rating)
            track.add_rating(random_rating)




if __name__ == "__main__":
    # Creating instances
    app = MusicPlayerApp()
    playlist1 = app.create_playlist("Chill Mix", "Chillout")
    playlist2 = app.create_playlist("Party Playlist", "Dance")
    track1 = at("Track 1", "http://example.com/track1")
    track2 = at("Track 2", "http://example.com/track2")

    # Adding tracks to playlists
    playlist1.add_track(track1)
    playlist2.add_track(track2)

    # Generating random ratings
    app.generate_random_ratings()

    # Display average ratings
    print(f"Average rating for Playlist 1: {playlist1.average_rating()}")
    print(f"Average rating for Track 1: {track1.average_rating()}")
