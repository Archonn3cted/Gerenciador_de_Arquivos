
# Sistema de Arquivos

Este projeto simula um sistema de arquivos simples utilizando o framework Django. Ele permite criar, listar, ler e deletar arquivos, com um gerenciamento de blocos de memória. Os arquivos são armazenados em blocos, e o sistema simula a alocação e liberação de blocos de memória quando os arquivos são criados ou deletados.


## Funcionalidades

- **Criação de Arquivos**: Armazena o conteúdo de um arquivo em blocos de memória simulados.
- **Listagem de Arquivos e Blocos**: Exibe o status de cada bloco de memória (livre ou ocupado) e mostra qual arquivo está ocupando um bloco específico.
- **Leitura de Arquivos**: Exibe o conteúdo de um arquivo armazenado.
- **Deleção de Arquivos**: Deleta um arquivo específico e libera os blocos ocupados.
- **Deleção de Todos os Arquivos**: Remove todos os arquivos criados e libera todos os blocos ocupados.


## Instalação

1. **Instale Gerenciador_de_Arquivos com npm**:

```bash
  npm install my-project
  cd my-project
```
2. **Ou clone este repositório**: 

 ```bash
   git clone https://github.com/Archonn3cted/Gerenciador_de_Arquivos.git
   cd projeto_arquivos
 ```
3. **Instale as dependências**:
 ```bash
   pip install -r requirements.txt
 ```
4. **Configure o banco de dados**:
 ```bash
   python manage.py migrate
 ```
5. **Crie um superusuário (opcional, para acessar a interface administrativa)**:
 ```bash
   python manage.py createsuperuser
 ```
6. **Inicie o servidor de desenvolvimento**:
 ```bash
   python manage.py runserver
 ```
7. **Acesse a aplicação**: Abra o navegador e vá até http://127.0.0.1:8000/blocos/ para visualizar a lista de blocos e arquivos.
## Detalhes Técnicos

**Modelos (Models)**:

O projeto usa dois modelos principais:

-***Bloco***: Representa um bloco de memória. Cada bloco contém:

-*conteudo*: O caractere armazenado no bloco.

-*ponteiro*: O ponteiro que indica o próximo bloco (ou None se for o último bloco).

-***Arquivo***: Representa um arquivo. Cada arquivo contém:

-*nome*: O nome do arquivo.

-*tamanho*: O número de caracteres no arquivo.

-*endereco_inicial*: O primeiro bloco alocado para este arquivo.

**Views**:

-*criar_arquivo*: Cria um novo arquivo, particionando seu conteúdo em blocos.

-*ler_arquivo*: Lê o conteúdo de um arquivo existente.

-*criar_blocos_iniciais*: Quando inicializar a view, a representação da memória será criada com 32 blocos livres.

-*deletar_arquivo*: Deleta um arquivo específico e libera os blocos.

-*lista_arquivos*: Exibe todos os blocos e arquivos associados.

**Templates**:

-*criar_arquivo.html*: Formulário para criar um arquivo.

-*ler_arquivo.html*: Exibe o conteúdo de um arquivo.

-*lista_blocos.html*: Exibe os blocos e arquivos com opções para deletar.
## Como Funciona o Gerenciamento de Memória
-Ao criar um arquivo, o sistema verifica quantos blocos são necessários e aloca blocos livres. Se não houver blocos livres suficientes, uma mensagem de "Memória insuficiente" será exibida.

-Quando um arquivo é deletado, os blocos que estavam alocados para ele são liberados.

-A funcionalidade "Deletar Todos" remove todos os arquivos e redefine todos os blocos.
