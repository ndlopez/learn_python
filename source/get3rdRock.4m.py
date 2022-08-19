#!/usr/bin/python3
# ignore verify peer
# curl -k https://stream.consultoradas.com/cp/get_info.php?p=8042
# <xbar.title>NowPlaying on ThirdRock</xbar.title>
# <xbar.version>0.2</xbar.version>
# <xbar.author>Diego Lopez</xbar.author>
# <xbar.author.github>ndlopez</xbar.author.github>
# <xbar.desc>Fetch current song playing on thirdRock from tune.in</xbar.desc>
# <xbar.image></xbar.image>
# <xbar.dependencies>python3,json,urllib</xbar.dependencies>

from urllib.request import urlopen
from urllib.error import URLError
import json

this_url = "https://stream.consultoradas.com/cp/get_info.php?p=8042"
that_url = "https://feed.tunein.com/profiles/s151799/nowPlaying?token=eyJwIjpmYWxzZSwidCI6IjIwMjEtMDktMDFUMDM6MDg6MTUuNjI4NzEzNFoifQ&itemToken=BgUFAAEAAQABAAEAb28B91ACAAEFAAA&formats=mp3,aac,ogg,flash,html,hls,wma&serial=5e05491c-6709-47a1-a3c2-433ed9ec5344&partnerId=RadioTime&version=4.74&itemUrlScheme=secure&reqAttempt=1"

def get_info(param):
    try:
        currData = json.load(urlopen(that_url,context=None))
    except URLError:
        return False

    return currData[param]

jsonHead = get_info('Header')
currSong = jsonHead['Subtitle']
print("♫",currSong)
print("---\nNow playing on Third Rock.")
