doker 
docker-compose up -d
docker-compose logs -f db_oracle 
docker exec -it oracle-xe sqlplus myuser/mypass123@localhost/XE
docker exec -it oracle-xe sqlplus sys/oracle123@localhost/XE as sysdba


venv
venv\Scripts\Activate.ps1

alembic 
alembic upgrade head
alembic revision --autogenerate -m "comment"

pip freeze > requirements.txt