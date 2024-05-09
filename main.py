from rembg import remove
from PIL import Image

entrada = Image.open("cao.jpg")
saida = remove(entrada).save("caofinal.png")