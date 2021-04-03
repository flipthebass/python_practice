#simple web scraping script to get up-to-date ja3 fingerprints from abuse.ch

from urllib.request import urlopen
import re

url = "https://sslbl.abuse.ch/blacklist/ja3_fingerprints.csv"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "(\w{32}\,\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}\,\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}\,[\w|\.]+)"
match_results = re.findall(pattern, html)

print("ja3,firstSeen,lastSeen,reason")
for x in match_results:
    print(x)
