1. Configurando templates globais com DIRS + extends para herança de templates

    - Em settings.py, vá em 'DIRS' e crie sua BASE_DIR

    - Crie uma pasta chamada 'base' na raiz do seu projeto

    - Vamos criar namespaces para evitar colisao de nomes

    - Criamos uma basta chamada 'global' dentro da pasta base que vai ser o nome dos templates globais.

    - Baixe a extensao 'Django'

2. Na nossa no nosso global, criamos um base.html que iremos usar nos demais.

    - Nele, estaremos usando o conceito de block e endblock

    - E no seu app, você quer que seu template html extenda dessa sua base.html

    - Fizemos um super template acima de todos, e deixamos um block de texto para que a gente possa fazer com quem herde use e substituia o conteudo como desejar.

    - para usar, extenda dele

    - é tipo você ter um tema que vai ser usado por muitos, um template, mas você pode substituir os textos, o conteudo por outras coisas.

    - Ou seja, é melhor criar as coisas globais e usar dentro dos apps.