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

3. HTTP

    - HTTP é stateless (sem estado) quer dizer que o protocolo HTTP não guarda nenhuma informação sobre requisições anteriores.

    - Stateless nos lembra API Rest, pois, ser Stateless é um dos princípios definidos por Roy Fielding que criou REST.

    - É sempre bom lembrar do que é uma API REST

4. API REST (Representationtal State Transfer)

    - API É um conjunto de regras que permite que dois sistemas se comuniquem (exemplo: front e back)

    - REST (Representational State Transfer): É um estilo de arquitetura criado por Roy Fielding em 2000, usado para construir APIs simples, escaláveis e baseadas no protocolo HTTP.

    - API REST é uma API que segue os princípios REST, usando o HTTP como meio de comunicação.

    - Os 6 Princípios do REST

        1. Uniform Interface - Obrigatório

        2. Stateless (Sem estado) - Obrigatório

        3. Cacheable (Cacheável) - Obrigatório

        4. Client-Server (Cliente e Servidor separados) - Obrigatório

        5. Layered System (Sistemas em Camadas) - Obrigatório

        6. Code on Demand (Código sob Demanda) - Opcional