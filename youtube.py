# -*- coding: utf-8 -*-
import urllib3
import urllib
import requests
import webbrowser
import re

def abre_video(nome_video):
    # http = urllib3.PoolManager()
    # Search videos on Youtube and play (e.g. Search in youtube believer)
    query_string = urllib.parse.urlencode({"search_query": nome_video})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    search_results = re.findall(
        r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
    )
    # print("http://www.youtube.com/watch?v=" + search_results[0])
    webbrowser.open(
        "http://www.youtube.com/watch?v={}".format(search_results[0])
    )

    pass


if __name__ == "__main__":
    abre_video("jaloo say goodbye")
