# Agenda de compromissos

<h3> Agenda de compromissos em Django </h3>

Inicialmente, você deve executar:
```
pip install django 
```
Para instalar a framework necessária para que este projeto funcione corretamente. 

Depois disso, você deve executar:
```
cd agenda 
python manage.py makemigratios 
python manage.py migrate 
```
Para gerar um arquivo local db.sqlite3, que será usado como banco de dados não relacional para Django. <br> <br>
Logo depois, você vece executar:
```
pytohn manage.py createsuperuser 
```
E você será solicitado com as seguintes perguntas:
> Nomde de usuário (deixa em branco para usar o padrão): <br>
> Endereço de e-mail (opcional): <br>
> Senha: <br>
> Senha (novamente): <br>

Ao fim desse processo você terá um super usuário para acessar o sistema.
Em seguida, você deve executar:
```
python manage.py runserver 
```
<br> <br>
Uma vez que o servidor está rodando, algumas Urls podem ser utilizadas para a navegação na aplicação:
```
localhost:8000/admin/
```
Irá redirecionar para a área de admin, onde podera utilizar o super usuário criado anteriormente para ter acesso.
```
localhost:8000/view/
```
Irá redirecinar para a parte principal do projeto, mostrando a agenda de compromissos em forma de uma tabela.
```
localhost:8000/home/
```
Irá redirecionar para a área de cadastro de um compromisso.

