from PIL import Image

# Abrir el archivo .webp
img = Image.open('logo.webp')

# Guardar como .ico
img.save('logo.ico')