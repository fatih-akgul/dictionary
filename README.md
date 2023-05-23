# DICTIONARY
This project implements a dictionary website where the data from Wiktionary is utilized

## Running locally
Environment variables required:
- values in **postgres.template.env** need to be in **postgres.env**
- values in **.templete.env** need to be in **.env**

Django-Postgres connection:
We need pg_config for Django to work with Postgres. Install it with:
```bash
sudo apt update
sudo apt -y upgrade
sudo apt install postgresql postgresql-contrib
```
We also need some header files for psycopg2:
```bash
sudo apt install libpq-dev
```
Then, install psycopg2:
```bash
pip install psycopg2
```

Install requirements:
```bash
pip install -r requirements.txt
```

Add a newly installed requirement to requirements.txt (Django in this example):
```bash
pip freeze | grep Django >> requirements.txt
```

Docker instructions:
--
Run the Postgres DB container:
```bash
docker compose up -d
```

Command to run psql inside the postgres container:
```bash
docker exec -it dictionary-postgres psql -U <dictionary-user> -W <dictionary-db>
```

