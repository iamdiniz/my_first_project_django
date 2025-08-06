1. Arquivos estaticos (STATIC_URL, STATICFILES_DIRS e load static)

    - Pode ser css, imagem, js...

    - Vamos trabalhar com aquilo que ja vem por padrão.

    - Nos conseguimos criar uma pasta static dentro de nossas pastas app.

2. como podemos carregar os arquivos static de algum lugar em nosso template?

    - Como carregar isso em um html?

    > load

    - Use o load do django html

    > {% load static %}

    - o load carrega coisas

3. O static também pode colidir nomes

    - Para resolver isso, vamos criar uma pasta de arquivo estatico referente ao seu app

    > home > static > home > css, js, img

4. Podemos criar um static até global, na raiz

    - Se você fizer um static no seu global, é só você incluir a pasta static.

    - Inclua os arquivos estaticos referentes a ela em settings.py

    - vá em:

    > STATIC_URL = 'static/'

    - Coloque:

    > STATICFILES_DIRS = [
        BASE_DIR / 'base' / 'static'
    ]