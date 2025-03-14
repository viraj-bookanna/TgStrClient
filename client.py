import time, os
from selenium import webdriver
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

session = StringSession(input('Session: '))

with TelegramClient(session, os.getenv('API_ID'), os.getenv('API_HASH')) as ses:
    me = ses.get_me()

script = f'''document.body.innerHTML='hehe';
window.localStorage.clear();
window.localStorage.account1=JSON.stringify({{
    "dc{session.dc_id}_auth_key": "{session.auth_key.key.hex()}",
    "userId": {me.id},
    "dcId": {session.dc_id}
}});
window.location.reload();'''

driver = webdriver.Chrome()
driver.get("https://web.telegram.org/k/")
driver.execute_script(script)

while True:
    try:
        if not driver.window_handles:
            break
        time.sleep(1)
    except:
        break

driver.quit()
