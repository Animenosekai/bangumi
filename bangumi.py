from json import loads
from time import time
from requests import get
from data.area import AREAS
from models.exceptions import FetchError
from models.program import Bangumi

HEADERS = {
    "Pragma": "no-cache",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "no-cache",
    "Accept-Language": "ja",
    "Host": "tv.yahoo.co.jp",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Connection": "keep-alive",
    "Referer": "https://tv.yahoo.co.jp/listings",
    "target-api": "programListingQuery",
    "target-path": "/TVWebService/V2/programListing"
}


def query(channel="", area=23, start_time=None, siTypeId=3, hours=24):
    if not isinstance(area, int) and not str(area) in AREAS:
        raise FetchError("Unknown area")
    elif not isinstance(area, int):
        area = AREAS[str(area)]

    # start_time
    if start_time is None:
        start_time = int(time())


    request = get("https://tv.yahoo.co.jp/api/adapter?siTypeId=" + str(siTypeId) + "&areaId=" + str(area) + "&hours=" + str(hours) + "&broadCastStartDate=" + str(start_time) + "&channelNumber=" + str(channel), headers=HEADERS)
    if request.status_code < 400:
        try:
            data = loads(request.text)
        except:
            raise FetchError("An error occured while converting the JSON response")
        return [Bangumi(program) for program in data["ResultSet"]["Result"]]
    else:
        raise FetchError("An error occured while retrieving the results from Yahoo TV Guide API (status: " + str(request.status_code))