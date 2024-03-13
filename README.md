Kami Bot
O Kami Bot é um chatbot simples desenvolvido em Python que utiliza o processamento de linguagem natural (NLP) para interagir com o usuário e fornecer respostas com base em um banco de dados de conhecimento. Ele permite ao usuário conversar com o bot, fazer perguntas e receber respostas relevantes.

Funcionalidades Principais
Interatividade: O bot permite que o usuário faça perguntas e interaja com ele em tempo real.
Aprendizado: Se o bot não souber a resposta para uma pergunta, ele solicita ao usuário que forneça uma resposta, contribuindo para a expansão do banco de dados de conhecimento.
Processamento de Linguagem Natural: Utilizando a biblioteca Spacy, o bot analisa a semelhança entre a pergunta do usuário e as perguntas armazenadas no banco de dados para encontrar a melhor correspondência.
Como Usar
Instalação das Dependências:

Certifique-se de ter o Python instalado em seu sistema.
Instale as dependências do projeto executando pip install -r requirements.txt.
Execução do Bot:

Execute o arquivo kami_bot.py em um ambiente Python.
Digite suas perguntas quando solicitado. Você pode encerrar a conversa digitando "quit".
Contribuindo com Novo Conhecimento:

Se o bot não souber responder a uma pergunta, ele solicitará ao usuário uma resposta. Basta fornecer uma resposta para ajudar a expandir o banco de dados de conhecimento.
Estrutura do Projeto
kami_bot.py: O arquivo principal contendo a lógica do bot e a interação com o usuário.
knowledge_database.json: Um arquivo JSON que armazena o banco de dados de perguntas e respostas.
README.md: Este arquivo, fornecendo uma visão geral da aplicação, instruções de uso e outras informações relevantes.
requirements.txt: Lista de dependências do projeto para instalação fácil.
Contribuindo
Contribuições são bem-vindas! Se você encontrar um bug ou tiver sugestões para melhorar o bot, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
