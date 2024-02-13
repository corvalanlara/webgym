from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
templates = ['index.html', 'planes.html', 'programas.html', 'espacio.html', 'terminos.html', '404.html', 'nosotros.html']

for template in templates:
    tmp = env.get_template(template)
    out = tmp.render()
    location = "./_site/{}".format(template)
    with open(location, "w", encoding="utf-8") as f:
        f.write(out)
print("Listo")
