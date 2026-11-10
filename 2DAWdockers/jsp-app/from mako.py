from mako.template import Template

plantilla = Template(filename="productos.mako")

html = plantilla.render()

print(html)