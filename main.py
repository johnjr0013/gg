import hashlib
import random
import string
import threading
import ctypes
import time
from discord_webhook import DiscordWebhook

sucess = 0;genStartTime = time.time()
def TitleWorkerr():
    global sucess
    ctypes.windll.kernel32.SetConsoleTitleW(f'SUCESS+ : {sucess} |Speed : {round(sucess / ((time.time() - genStartTime) / 60))}/m |')
    

def encrypt_string():
    global sucess
    a = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(64))
    sha_signature = \
        hashlib.sha256(a.encode()).hexdigest()

    if sha_signature == "13d4ba0235df135f31e404288eccbbef8d64a7ceb904980666c4915074315810":
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1243102413414600714/xNopcoXNZKR2sX_yAFZDRvW2r85WE-fuHABwRh8ufXCVXVJd_NtMpMNH9WJXDUWy_AvW", content= a + ":" +sha_signature + ":" + "<@1225802833597694023>")
        open('sucess.txt', 'a').write(f'{a + ":" + sha_signature}\n')
        response = webhook.execute()
    else:
        print(sha_signature)
    sucess = sucess + 1 
    TitleWorkerr()
    return sha_signature


while True:
    threads = "50"   
    for i in range(int(threads)):
        threading.Thread(target=encrypt_string).start()
