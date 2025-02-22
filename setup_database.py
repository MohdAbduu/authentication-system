from auth_system.database import DatabaseManager

def setup_database():
    db = DatabaseManager()
    db.execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.close()
    print("Database setup complete!")

if __name__ == "__main__":
    setup_database()
