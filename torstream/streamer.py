import argparse
from torstream import knaben , peerflix_test


def torrent(query):
    """
    The function that calls and sorts the torrent handler
    :param query: The name of the torrent you want to stream
    :return: VLC stream
    """
    knaben.main(query)


def argParser():
    """
    The main CLI function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("media", help="The name of the media you want to stream",
                        type=str)
    args = parser.parse_args()
    try:
        # print(args)
        peerflix_test.test_system()
        torrent(args.media)
    except ValueError:
        print("Failed to connect to server: Please try again!")