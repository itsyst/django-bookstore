from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os


class Command(BaseCommand):
    help = 'Populates the database with genres and books'

    def handle(self, *args, **options):
        print('Populating the database...')
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'seed.sql')
        sql = Path(file_path).read_text()

        # Split the SQL into individual statements
        # Execute one statement at a time happens because SQLite doesn’t support executing multiple 
        # SQL statements at once in a single cursor.execute call. 
        statements = sql.split(';')
        
        with connection.cursor() as cursor:
            for statement in statements:
                statement = statement.strip()
                if statement:  # Skip any empty statements
                    cursor.execute(statement)

        print('Database populated successfully.')
