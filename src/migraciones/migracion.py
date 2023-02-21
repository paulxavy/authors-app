from flask import Flask
from yoyo import read_migrations, get_backend
from decouple import config
import time
import os



host = config('PGSQL_HOST')
user = config('PGSQL_USER')
password = config('PGSQL_PASSWORD')
database = config('PGSQL_DATABASE')
port = config('PGSQL_PORT')
time.sleep(5)
backend = get_backend(f"postgresql://{user}:{password}@{host}:{port}/{database}")
migrations_folder = "src/migraciones/migrations"
migrations = read_migrations(migrations_folder)
print(f'migrations: {migrations}')
if migrations:
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
        print("Migraciones aplicadas correctamente.")