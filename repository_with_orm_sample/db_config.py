from pathlib import Path

root_path = Path(__file__).parent
sqlite3_file_path = root_path / 'repository_with_orm_sample.sqlite3'

DB_CONFIG = {
    'development': {
        'driver': 'sqlite',
        'database': sqlite3_file_path,
    }
}
