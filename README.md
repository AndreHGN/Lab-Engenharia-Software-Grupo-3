# Lab-Engenharia-Software-Grupo-3

## Trello: https://trello.com/b/6L1Xj0mt/planejamento-do-projeto

## COMO EXECUTAR O APP

### 1. Instalar e criar ambiente virtual

Instalação do ambiente virtual:
`pip3 install virtualenv`

Criação de um ambiente virtual:
`virtualenv -p python3 venv`

Ativação do ambiente virtual:
- Em Windows: `venv/Scripts/activate`
- Em Linux: `source venv/bin/activate`

### 2. Instalação do Django e do Cliente MySQL

Django:
`pip install django`

Cliente MySQL:
`pip install pymysql`

### 3. Instalação do banco de dados MySQL

- Instalação do BD para Linux:
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-pt 

- Instalação do BD para Windows:
https://www.mysqltutorial.org/install-mysql/ 

Além disso, deve ser instalado o MySQL Workbench para realizar o gerenciamento.

OBS: É recomendado que ao se instalar o banco de dados, seja configurado com as seguintes credenciais e nomes:
```
'NAME': 'Lote',
'USER': 'admin',
'PASSWORD': 'pass',
'HOST': 'localhost',
'PORT': '3306',
```

### 4. Ajustar as variáveis do banco de dados

- Caso o banco de dados não estiver configurado com as credenciais originais, ir para `Projeto/apps/apps/settings.py` e alterar a variável de ambiente DATABASES.
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'nomeDoBanco',
    'USER': 'usuarioRootDoBanco',
    'PASSWORD': 'senhaDoUsuario',
    'HOST': 'localhost',
    'PORT': 'portaSendoUtilizada',
    }
}
 ```

### 5. Criação do Banco de Dados no MySQL Workbench

Utilizar o comando abaixo para criar o banco (seguindo as credenciais definidas no código do repositório):
`CREATE DATABASE Lote;`

Criar usuário e senha para acessar o banco com:
```
CREATE USER admin@localhost IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON Lote.* TO admin@localhost;
FLUSH PRIVILEGES;
```

### 6. Migração das tabelas ao banco

Desta seção em diante é necessário que os comandos sejam rodados no diretório `Projeto/apps/`. Se não tiver feito ainda, faça:
`cd Projeto/apps`
 
Em seguida, rode os comandos na seguinte sequência:

`python manage.py makemigrations`

`python manage.py migrate`

### 7. Criação de superusuário no sistema

O arquivo manage.py também contém um script para criação de superusuário do sistema, basta rodar `python manage.py createsuperuser` e cadastrar as credenciais. (Para coincidir com os testes, o usuário deve se chamar `admin` e ter a senha `1234qwer!`)

### 8. Rodar o servidor

Após todas as configurações, o servidor pode ser iniciado rodando o script `runserver` em manage.py (`python manage.py runserver` na pasta `Projeto/apps`)