# Objetivo Geral
introduzir conceitos fundamentais de desenvolvimento web, compreendendo a estrutura básica da web
arquitetura cliente servidor, e as principais tecnologias front e back-end.

# Dev Web:
processo de criação de websites e aplicações para internet. Variedades de tarefas, incluindo web design, programação web, gestão de banco de dados e engenharia dos servidores.

# Componentes principais 
1. Frontend:
    A parte do website que o usuario interage diretamente. Envolve criação de interfaces de usuário e experiencias usando tecnologias como HTML, CSS e JavaScript.

2. Backend:
    O 'bastidor' de website, onde ocorrem o processamento de dados, gerenciamento de banco de dados e controle do servidor.
    envolve linguagens como Python, Java, Go, Php, Ruby etc..

    Banco de dados: PostgreSQL, MySQL, MongoDB, Oracle, etc..

    Framework: Django(Python), Express(javascript), Boot(java)

Frontend > API > backend

# Como WEB funciona
# Protocolo HTTP: cliente - servidor
--> é o protocolo fundamental usado na web para transferencia de dados. Quando um usuário acessa um site, o navegador envia uma solicitação HTTP para o servidor do site, que responde com os dados site.

# Funcionamento de um Website
1. Solicitação do usuário:
    começa quando o usuário inserindo um URL no navegador ou clicando em um link. 

2. Resolução de DNS:
    o URL é traduzido em um endereço de IP através de um sisema chamado DNS(Domain Name System)

3. Conexão com o Servidor:
    o navegador utiliza o endereço IP para estabelecer uma conexão com o servidor que hospeda o site.

4. Resposta do servidor:
    O servidor processa a solicitação HTTP e envia de volta os arquivos geralmente em HTML, CSS ou Js.

5. Renderização no navegador:
    O navegador interpreta esses arquivos e exibe os sites ao usuário.

# Tecnologias envolvidas
Além de HTML, CSS e JavaScript, tecnologias como SSL/TLS para segurança, APIs para interatividade e banco de dados para armazenamento de dados também desempenham um papel vital no funcionamento da web.


# APIs e conceitos Fundamentais:
conjunto de regras e definições que permite que diferentes aplicações de software ou componentes se comuniquem entr si.
Funciona como um intermediário, permitindo que pedidossejam feitos e respostas sejam recebidas entre diferentes sistemas de software. 

# API no contexto web
usadas para permitir a interaçãoentre diferentes serviços e aplicações, como enviar dados de um usuário de um aplicativo para um servidor ou solicitar dados de um serviço externo(por ex, redes sociais, mapas, previsão do tempo)

# API de pagamento:
facilita transações de comercio eletronico atraves de diferentes plataformas de pagamentos.
https://vindi.github.io/api-docs/dist/#/

# API RESTful
refere-se a APIs que seguem os principios do REST. São baseadas em padrões HTTP e utilizadas para interações web

1. uso dos métodos HTTP (GET, POST, PUT, DELETE) para operações CRUD

# Escolhendo API
RESTful é popular pela simplicidade
SOAP é preferido para segurança e transações complexas
GraphQL é ideal para aplicações que requerem dados dinamicos personalizados