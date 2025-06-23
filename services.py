import subprocess

def caddy_service():
    return subprocess.Popen(["caddy", "run", "--config", "./caddy/Caddyfile"])