# RemoveFundo
Como remover fundo de imagens com apenas duas linhas de codigo python.

### Primeiro passo teremos que instalar 2 bibliotecas via terminal:

### Biblioteca Rembg.

```
pip install rembg
```

### Biblioteca Pillow.

```
pip install -U Pillow
```

Assim que instalado importar no codigo.
```py
from rembg import remove
from PIL import Image
```
Criamos uma variável(nesse caso dei o nome de "entrada") e usamos o método open para abrir a imagem , nesse exemplo usei uma imagem da internet de um cachorrinho de óculos, e dei o nome para imagem de cao.
Obs:  imagem tem que estar no mesmo diretorio do projeto.

```py
entrada = Image.open("cao.jpg")
```

Agora criamos uma variavel saida que recebe a imagem na variavek entrada, usando o metodo remove e salvavando com um novo nome, no caso salvei como "caofinal.png".
```py
saida = remove(entrada).save("caofinal.png")
```
A Imagem com o fundo removido irá aparecer no mesmo diretorio.
