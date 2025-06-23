from string import Template

def setup_caddyfile(username, password, domain_name):
    with open("./templates/Caddyfile", "r") as caddy_template:
        template = caddy_template.read()
        caddyfile = Template(template)
        caddy_config = {
            "USERNAME": username,
            "PASSWORD": password,
            "DOMAIN_NAME": domain_name
        }
        caddyfile_template = caddyfile.substitute(caddy_config)
    with open("./caddy/Caddyfile", "w") as output_file:
        output_file.write(caddyfile_template)