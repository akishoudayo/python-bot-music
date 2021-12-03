from os import getenv, system
from urllib.request import urlretrieve
from re import sub

print("[INFO] Changing the port ...")
try:
    temp = open('application.yml', 'r').read()
    temp = sub('REPLACEPORT', getenv('PORT'), temp)
    temp = sub('REPLACEPASSWORD', getenv('PASSWORD'), temp)
    open('application.yml', 'w').write(temp)
except BaseException as exc:
    print(f"[ERROR] Error changing port ... Info: {exc}")
else:
    print("[INFO] Successfully changed Port and Password...")

print("[INFO] Downloading Latest Lavalink ...")
try:
    urlretrieve("https://github.com/freyacodes/Lavalink/releases/download/3.4/Lavalink.jar", filename='Lavalink.jar')
except BaseException as exc:
    print(f"[ERROR] Error downloading Lavalink... Info: {exc}")
else:
    print("[INFO] Success in downloading Lavalink...")
    
try:
    system('java -jar Lavalink.jar {}'.format(getenv('ADDITIONAL_JAVA_OPTIONS')))
except:
    print(f"[ERROR] Failed to start Lavalink server... Info: {exc}")
