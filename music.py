import urllib.request
import re
import webbrowser

song = input("What's your favourite song? ")
song = "".join(song.split(" "))
html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+song)
video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())

webbrowser.open("http://youtube.com/watch?v="+video_ids[0])                 