1. Arquivos parciais e include para separar trechos dos templates (partials)

    - Com o {{  }} é como 

    - 'extends' executa a extensão do template entre aspas. (herança)

    - 'block' pode criar quantos blocos quiser.

    - o que esta dentro do block voce consegue trocar.

    - mude tudo para simplificar tudo.

2. Partials (partes da pagina)

    - É bom para reutilizar, e fazer com que outras paginas incluam aquele bloco de codigo nela.

    - e na pagina que voce vai utilizar, voce pede para ele fazer um include

    > {% include '' %}

    - ele inclui um partial ali.

    - use para trechos de sua pagina, head, foto, etc...