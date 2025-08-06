1. Usando o context para enviar dados para dentro dos templates do Django.

    - As views controla para onde vai o fluxo, quais dados, qual model, etc...

    - As views pode encontrar dados quaisquer e enviar os dados para o html

2. Context

    - É qualquer coisa que tenha chave e valor, e pode ate não enviar nada.

    - Como eu faço para exibir esse texto dessa funcao da minha view na minha html?

    > def home(request):
        print('home')
        return render(
            request,
            'home/index.html',
            {
                'text': 'Estamos na home'
            }
        )
    
    - Faça assim, usando o double mustache:

    > {% extends 'global/base.html' %}

    {% block texto %} 

        {{ text }}

    {% endblock texto %}

    - Podemos pegar dados e jogar no template agora.