from vars import username, password, domain_name
from setup import setup_caddyfile

if __name__ == "__main__":
    setup_caddyfile(username, password, domain_name)
    print("Caddyfile has been set up successfully.")