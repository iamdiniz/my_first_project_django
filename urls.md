1. Você consegue criar urls em urls.py na pasta do seu projeto

    - Existem um urls.py na pasta do seu projeto que possui os padrões de suas urls:

    > urlpatterns = [
    >    path('admin/', admin.site.urls),
    > ]

    - O path nunca começa com '/' ele termina com '/'

    - Então quando você for fazer caminho, você deve criar a rota e o que você vai devolver para ele.

2. O Django trabalha com MVT - Model View Template (MVC)

    - Model: Base de dados, dados

    - View: Recebe a request e decide o que faz.