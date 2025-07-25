from database import get_db_connection  # replace with the actual filename of your DB code

def test_connection():
    conn = get_db_connection()
    if conn:
        print("DB connection successful!")
        conn.close()
    else:
        print("DB connection failed!")

if __name__ == "__main__":
    test_connection()
