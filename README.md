
<<<<<<< HEAD
# CALCULADORA KOGUI 
=======
# CALCULADORA KOGUI 🧮
>>>>>>> afa0ad8136d18b471d854ac7f050b6761baefca9


#### O objetivo principal é oferecer uma calculadora que realiza as quatro operações matemáticas básicas (Soma, Subtração, Multiplicação e Divisão). Cada usuário precisa se registrar e fazer login para acessar a calculadora. Todas as operações realizadas são salvas e associadas ao perfil do usuário, que pode visualizar seu histórico de cálculos na página principal.

Funcionalidades Principais
- Autenticação de Usuários: Sistema completo com páginas de registro, login e funcionalidade de logout.

 - Calculadora Funcional: Interface para realizar cálculos matemáticos básicos.

 - Histórico de Cálculos: As operações (ex: "5 + 5") e seus resultados (ex: "10") são salvos no banco de dados.


## Tecnologias Utilizadas
Backend: Python

Framework: Django

Banco de Dados: SQLite

Frontend: HTML, CSS e JavaScript

## Como Configurar e Rodar o Projeto
Pré-requisitos
Antes de começar, certifique-se de que você tem o Python e o pip instalados em sua máquina.

### 1. Clonar o Repositório
Primeiro, clone o projeto para sua máquina local 

    git clone https://github.com/zeguil/CALCULATOR-KOGUI.git
### Navegue para a pasta do projeto
    cd CALCULATOR-KOGUI

### 2. Criar um Ambiente Virtual
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

    python -m venv venv

### Ativar o ambiente virtual
### No Windows:

    venv\Scripts\activate

### No macOS/Linux:

    source venv/bin/activate

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale as dependências do arquivo 'requirements.txt'.


     pip install -r requirements.txt

### 4. Aplicar as Migrações do Banco de Dados

    python manage.py migrate


### 5. Rodar o Servidor de Desenvolvimento
Agora, inicie o servidor local.

    python manage.py runserver


A aplicação estará disponível em http://127.0.0.1:8000/.

### Endpoints (URLs) da Aplicação
Acesse as seguintes URLs no seu navegador para interagir com a aplicação:

- http://127.0.0.1:8000/registrar/ - Página para registrar um novo usuário.

- http://127.0.0.1:8000/login/ - Página para fazer login.

- http://127.0.0.1:8000/logout/ - Rota para deslogar o usuário atual.

- http://127.0.0.1:8000/home/ - Página principal com a calculadora e o histórico de operações (requer login).

