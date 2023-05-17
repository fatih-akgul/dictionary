# DICTIONARY
This project implements a dictionary website where the data from Wiktionary is utilized

## Running locally
Environment variables required:
- ?

Docker instructions:
--
Run the Postgres DB container:
- docker compose up -d

Command to run psql inside the postgres container:
- docker exec -it dictionary-postgres psql -U dictionary-user -W dictionary-db

