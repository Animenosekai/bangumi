from datetime import datetime
from data import genre

class Genre():
    """
    A program genre
    """
    def __init__(self, id, minor=False) -> None:
        if str(id).replace(" ", "") == "":
            return
        self.id = int(id, 16)
        self.minor = minor
        if self.minor:
            self.name = genre.MINOR.get(self.id, None)
        else:
            self.name = genre.MAJOR.get(self.id, None)

    def __repr__(self) -> str:
        if self.name is not None:
            return self.name
        return str(self.id)

class Listing():
    """
    A listing service (地上波, BS, etc.)
    """
    def __init__(self, id, name) -> None:
        self.id = int(id)
        self.name = str(name)

    def __repr__(self) -> str:
        return self.name

class Channel():
    """
    A TV Channel
    """
    def __init__(self, number, id, name, service) -> None:
        self.number = int(number)
        self.id = int(id, 16)
        self.name = str(name)
        self.service = str(service)
    
    def __repr__(self) -> str:
        return self.name

class Title():
    """
    A program title
    """
    def __init__(self, short, long) -> None:
        self.short = str(short)
        self.long = str(long)

    def __repr__(self) -> str:
        return self.short

    def __str__(self) -> str:
        return self.long

class Bangumi():
    """
    A program
    """
    def __init__(self, data) -> None:
        self._id = int(data.get("contentsId", 0))
        self._program_id = int(data.get("programId", 0))
        self._network_id = int(data.get("networkId", "0x0"), 16)
        self._service_id = int(data.get("serviceId", "0x0"), 16)
        self._listings_flg = data.get("listingsFlg", True)
        self.listing = Listing(id=data.get("siTypeId", 0), name=data["siTypeId"])
        self.channel = Channel(number=data.get("channelNumber"), id=data.get("serviceId", "0x0"), name=data["channelName"], service=data.get("serviceName", ""))
        if "broadCastStartDateMinute" in data:
            self.broadcast_start = datetime.fromtimestamp(data["broadCastStartDateMinute"])
        else:
            self.broadcast_start = datetime.fromtimestamp(data["broadCastStartDate"])
        if "broadCastEndDateMinute" in data:
            self.broadcast_end = datetime.fromtimestamp(data["broadCastEndDateMinute"])
        else:
            self.broadcast_end = datetime.fromtimestamp(data["broadCastEndDate"])
        self.duration = float(data["duration"])
        self.title = Title(data["programTitle"], data["title"])
        self.summary = str(data["summary"])
        self.mitai_count = int(data.get("mitaiCount", 0))
        self.review_count = int(data.get("reviewCount", 0))
        self.rating_count = int(data.get("ratingCount", 0))
        self.rating = int(data.get("ratingAverage", 0))
        self.last_update = datetime.strptime(data.get("updateTime", "1970-01-01T00:00:00Z"), '%Y-%m-%dT%H:%M:%SZ')
        self.element = data.get("element", [])
        self.genres = [Genre(id) for id in data.get("majorGenreId", [])]

    def __repr__(self) -> str:
        return str(self.title)