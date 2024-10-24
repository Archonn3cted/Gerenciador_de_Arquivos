
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
