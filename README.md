Descrição
O objetivo principal é oferecer uma calculadora que realiza as quatro operações matemáticas básicas (Soma, Subtração, Multiplicação e Divisão). Cada usuário precisa se registrar e fazer login para acessar a calculadora. Todas as operações realizadas são salvas e associadas ao perfil do usuário, que pode visualizar seu histórico de cálculos na página principal.

Funcionalidades Principais
Autenticação de Usuários: Sistema completo com páginas de registro, login e funcionalidade de logout.

Calculadora Funcional: Interface para realizar cálculos matemáticos básicos.

Histórico de Cálculos: As operações (ex: "5 + 5") e seus resultados (ex: "10") são salvos no banco de dados.

Exibição do Histórico: O usuário logado pode ver uma lista de seus últimos cálculos realizados.

Banco de Dados Relacional: Utiliza SQLite para persistir os dados de usuários e suas operações, seguindo o modelo relacional definido.

Tecnologias Utilizadas
Backend: Python

Framework: Django

Banco de Dados: SQLite

Frontend: HTML, CSS e JavaScript

Como Configurar e Rodar o Projeto
Pré-requisitos
Antes de começar, certifique-se de que você tem o Python e o pip instalados em sua máquina.

1. Clonar o Repositório
Primeiro, clone o projeto para sua máquina local (se estiver no GitHub) ou simplesmente navegue até a pasta do projeto.

# Se o projeto está no Git, clone-o:
git clone <URL_DO_SEU_REPOSITORIO>
# Navegue para a pasta do projeto
cd <NOME_DA_PASTA_DO_PROJETO>

2. Criar um Ambiente Virtual
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

3. Instalar as Dependências
Com o ambiente virtual ativado, instale o Django.


# pip install -r requirements.txt

4. Aplicar as Migrações do Banco de Dados
As migrações criam as tabelas (Usuario, Operacao, etc.) no banco de dados SQLite.

python manage.py migrate


5. Rodar o Servidor de Desenvolvimento
Agora, inicie o servidor local.

python manage.py runserver

A aplicação estará disponível em http://127.0.0.1:8000/.

Endpoints (URLs) da Aplicação
Acesse as seguintes URLs no seu navegador para interagir com a aplicação:

http://127.0.0.1:8000/registrar/ - Página para registrar um novo usuário.

http://127.0.0.1:8000/login/ - Página para fazer login.

http://127.0.0.1:8000/logout/ - Rota para deslogar o usuário atual.

http://127.0.0.1:8000/home/ - Página principal com a calculadora e o histórico de operações (requer login).

http://127.0.0.1:8000/admin/ - Área administrativa do Django (requer login de superusuário).