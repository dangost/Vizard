class Game:

    def __init__(self, game_id, name, avatar, trailer, steam, torrent, rate, price, studio_id, genre_id):
        self.game_id = game_id
        self.name = name
        self.avatar = avatar
        self.trailer = trailer
        self.steam = steam
        self.torrent = torrent
        self.rate = rate
        self.price = price
        self.studio_id = studio_id
        self.genre_id = genre_id

    game_id: int

    name: str

    avatar: str  # picture link

    trailer: str  # yt link

    steam: str  # steam link

    torrent: str  # torrent link

    rate: str

    price: str

    studio_id: int

    genre_id: int
