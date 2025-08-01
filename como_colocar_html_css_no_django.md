1. Como eu posso colocar o html e css no django?

    - Vamos usar o 'render' para renderizar o html

       def home(request):
            print('home')
            return render(
                request,
                'home.html'
            )
    
    - Vamos supor que o segundo argumento você esteja chamando um arquivo em algum lugar.

    - Você pode configurar em settings.py onde ele vai buscar os diretorios de templates:

        > 'DIRS': []
    
    - Se você não mudar, o padrão normal ele indica que dentro do seu app você pode criar uma pasta chamada de templates, e nessa pasta de templates você pode criar esses arquivos...

    - E você não precisa em 'home.html' especificar que você quer que ele busque de templates, porque ele ja faz isso automaticamente.

    - Não esqueça de algumas premissas, como por exemplo o nome do seu app, que quando você cria ele está em apps.py, e use aquele nome que está na classe:

        > name = 'home'
    
    - Coloque ele também em INSTALLED_APPS = [ 'home' ]

    - cuidado, que se você tiver 2 arquivos com o mesmo nome, você não terá nenhuma proteção.

    - Se a gente não criar um name space, ele vai fazer uma busca em todos os apps. E pode ter 2 arquivos de mesmo nome em apps diferentes, o primeiro que ele achar é o que ele vai usar.

    - Para evitar isso vamos usar o padrão do django.

    - vamos colocar de novo uma pasta com o nome do meu app. e ai os arquivos de template vão para dentro de blog.

    - e agora nas views você vai precisar informar o nome do app.

        > 'blog/home.html'

    - Isso é namespace e evita colisão de nome de arquivo.