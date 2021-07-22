import mysql.connector

from mysql.connector import Error
from cryptography.fernet import Fernet

CIPHERED_BIN_LOCATION = r"C:\Users\ikhwan\ecp_2\hash_files\user1_ciphered.bin"

# cryptography: Retrieve key and bin file for decryption
key = b'Qs8IYF0DHhQ8hfyABcHOGVG585YePQpX5unmLaJ5ZaQ='
cipher_suite = Fernet(key)

with open(CIPHERED_BIN_LOCATION, 'rb') as f:
    for line in f:
        encrypted_pwd = line

uncipher_text = (cipher_suite.decrypt(encrypted_pwd))
plain_text_encrypted_password = bytes(uncipher_text).decode('utf-8')


def check_database_playlist_aggregator_connection():
    database_list = list_databases("localhost", "root", plain_text_encrypted_password)

    if "playlist_aggregator" in database_list:
        print("playlist_aggregator exists")
    else:
        print("playlist_aggregator does not exist.")
        connection = create_connection("localhost", "root", plain_text_encrypted_password)
        # Create database
        create_playlist_aggregator_query = "CREATE DATABASE playlist_aggregator"
        create_database(connection, create_playlist_aggregator_query)
        print("Created 'playlist_aggregator' database.")
        # Create tables
        create_table_users()
        print("Created 'users' table.")
        create_table_services()
        print("Created 'services' table.")

    connection = create_connection("localhost", "root", plain_text_encrypted_password, "playlist_aggregator")
    tables = list_tables(connection)
    return tables


def list_databases(host_name, user_name, user_password):
    database_list = []
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             password=user_password,
                                             buffered=True)
        cursor = connection.cursor()
        databases = "SHOW DATABASES"
        cursor.execute(databases)

        for (databases) in cursor:
            database_list.append(databases[0])
    except Error as e:
        print(f"The error '{e}' occurred.")
    return database_list


def list_tables(connection):
    tables_list = []
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    results = cursor.fetchall()
    for table in results:
        tables_list.append(table[0])
    return tables_list


def create_connection(host_name, user_name, user_password, db_name=None):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,
                                             database=db_name,
                                             user=user_name,
                                             password=user_password)

    except Error as e:
        print("Error while connecting to MySQL", e)
    return connection


def disconnect_mysql_db():
    connection = mysql.connector.connect(host='localhost',
                                         database='playlist_aggregator',
                                         user='root',
                                         password=plain_text_encrypted_password)
    cursor = connection.cursor()
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e} occurred")


def create_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query, values=None):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred.")


def create_table_users():
    """
    This function requires that the playlist_aggregator database already exists
    """

    connection = create_connection("localhost", "root", plain_text_encrypted_password, "playlist_aggregator")
    create_table_users_query = """
            CREATE TABLE IF NOT EXISTS users (
              id INT AUTO_INCREMENT NOT NULL,
              first_name VARCHAR(45) NOT NULL,
              last_name VARCHAR(45) NOT NULL,
              email VARCHAR(45),
              address VARCHAR(50),
              phone   VARCHAR(45),
              dob     VARCHAR(45),
              PRIMARY KEY (id)
              )ENGINE=INNODB;
            """
    execute_query(connection, create_table_users_query)
    print("Created 'users' table.")


def create_table_services():
    """
    This function requires that the playlist_aggregator database already exists
    """

    connection = create_connection("localhost", "root", plain_text_encrypted_password, "playlist_aggregator")
    create_table_services_query = """
            CREATE TABLE IF NOT EXISTS services (
              id INT NOT NULL,
              service_name VARCHAR(45) NOT NULL,
              user_id INT,
              INDEX use_ind (user_id),
              FOREIGN KEY (user_id)
                REFERENCES users(id)
                ON DELETE CASCADE
              )ENGINE=INNODB;
            """
    execute_query(connection, create_table_services_query)


def create_table_playlists():
    """
    The create_table_playlists function creates the table to store playlist data for each user
    """

    connection = create_connection("localhost", "root", plain_text_encrypted_password, "playlist_aggregator")
    create_table_playlists_query = """
        CREATE TABLE IF NOT EXISTS playlists (
            playlist_id INT NOT NULL,
            user_id INT,
            playlist_name VARCHAR(45),
            INDEX use_ind (user_id),
            FOREIGN KEY (user_id)
                REFERENCES users(id)
                ON DELETE CASCADE
            )ENGINE=INNODB;
        """
    execute_query(connection, create_table_playlists_query)