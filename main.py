import atexit, signal, sys
from vars import username, password, domain_name
from setup import setup_caddyfile
from os.path import exists
from services import caddy_service

config_files = {
    "./caddy/Caddyfile"
}

def start_caddy_service():
    global caddy_process
    caddy_process = caddy_service()

def exit_function():
    def on_exit():
        caddy_process.terminate()
    def handle_exit(signum, frame):
        sys.exit(0)
    atexit.register(on_exit)
    signal.signal(signal.SIGTERM, handle_exit)
    signal.signal(signal.SIGINT, handle_exit)
    signal.pause()

if __name__ == "__main__":
    if all(not exists(file) for file in config_files):
        setup_caddyfile(username, password, domain_name)
    start_caddy_service()
    exit_function()