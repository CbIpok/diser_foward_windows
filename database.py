import sqlite3
import mysql.connector

db_config_ = {
    'user': 'admin',
    'password': 'root',  # Замените на ваш реальный пароль
    'host': '172.22.128.55',
    'database': 'data',  # Замените на имя вашей базы данных
    'port': 3306
}

class FileDatabase:
    def __init__(self, db_config=None):
        """db_config - словарь с параметрами подключения к базе данных MySQL."""
        if db_config is None:
            db_config = db_config_
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Создает таблицу для хранения файлов, если она еще не существует"""
        query = """
        CREATE TABLE IF NOT EXISTS files (
            bath VARCHAR(255),
            wave VARCHAR(255),
            txt_file LONGBLOB,
            nc_file LONGBLOB,
            PRIMARY KEY (bath, wave)
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def save_files(self, bath, wave, txt_file_path, nc_file_path):
        """Сохраняет файлы по ключам bath и wave"""
        with open(txt_file_path, 'rb') as txt_file, open(nc_file_path, 'rb') as nc_file:
            txt_data = txt_file.read()
            nc_data = nc_file.read()

        query = """
        INSERT INTO files (bath, wave, txt_file, nc_file)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE txt_file = VALUES(txt_file), nc_file = VALUES(nc_file)
        """
        self.cursor.execute(query, (bath, wave, txt_data, nc_data))
        self.conn.commit()

    def load_files(self, bath, wave, txt_output_path, nc_output_path):
        """Загружает файлы по ключам bath и wave и сохраняет их на диск"""
        query = """
        SELECT txt_file, nc_file FROM files WHERE bath = %s AND wave = %s
        """
        self.cursor.execute(query, (bath, wave))
        result = self.cursor.fetchone()

        if result:
            txt_data, nc_data = result
            with open(txt_output_path, 'wb') as txt_output, open(nc_output_path, 'wb') as nc_output:
                txt_output.write(txt_data)
                nc_output.write(nc_data)
            print(f"Files saved to {txt_output_path} and {nc_output_path}")
        else:
            print(f"No files found for bath={bath} and wave={wave}")

    def delete_files(self, bath, wave):
        """Удаляет файлы по ключам bath и wave"""
        query = "DELETE FROM files WHERE bath = %s AND wave = %s"
        self.cursor.execute(query, (bath, wave))
        self.conn.commit()

    def close(self):
        """Закрывает соединение с базой данных"""
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    db = FileDatabase("/mnt/hgfs/shared/set_1.db")
    # db.save_files("1000","0","dat_1000.txt","out_1000.nc")
    db.load_files("1000", "0", "/mnt/hgfs/shared/dat_1000.txt", "/mnt/hgfs/shared/out_1000.nc")