import sys
import requests


def search_hotel(access_token, keyword):
    url = "https://challenge-server.tracks.run/hotel-reservation/hotels"
    headers = {"X-ACCESS-TOKEN": access_token}
    params = {}

    if keyword:
        params["keyword"] = keyword

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        hotels = response.json()
        if not hotels:
            print("該当するホテルはありません。")
            return
        for hotel in hotels:
            print(hotel["name"])
    except Exception as e:
        print(f"error: {e}")


def main(argv):
    access_token = sys.argv[1]
    keyword = sys.argv[2] if len(sys.argv) > 2 else None
    search_hotel(access_token, keyword)

    # for i, v in enumerate(argv):
    #     print("argv[{0}]: {1}".format(i, v))


if __name__ == "__main__":
    main(sys.argv)