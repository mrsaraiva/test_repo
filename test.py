from application import application
import requests
import os
import signal
import subprocess
import sys
import threading
import time


app_url = 'http://127.0.0.1:5000'
test_filename = os.path.basename(__file__)
test_string = 'version'
test_tries = 5
test_delay = 5
test_pid_list = []


# Sorry about the hacky way guys! With enough time, i could probably come up with a better test and wrap the webapp
# into a class.
def test_application(tries, delay):
    current_try = 0
    response = requests.get(app_url)
    html = str(response.content)
    while (current_try < test_tries):
        if test_string in html:
            print('Found string in the webpage')
            exit_code = 0
            break
        else:
            print('Did not find string in the webpage')
            exit_code = 1
        current_try += 1
        time.sleep(test_delay)
    kill_flask()
    sys.exit(exit_code)


# Ugly hack!
def kill_flask():
    supported_platforms = ['linux1' , 'linux2', 'darwin']
    if sys.platform in supported_platforms:
        pgrep = 'pgrep -f {}'.format(test_filename)
        for line in os.popen(pgrep):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)


kill_flask() # cleanup any leftover processes from previous test
t = threading.Timer(5, test_application, args=[test_tries, test_delay])
t.start()
application.run()