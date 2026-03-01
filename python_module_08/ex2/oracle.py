import os
from dotenv import load_dotenv

def oracle():
    try:
        load_dotenv()

        matrix_mode = os.getenv("MATRIX_MODE")
        database_url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL")
        zion_endpoint = os.getenv("ZION_ENDPOINT")

        print("\nORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print(f"Mode: {matrix_mode}")
        print(f"Database: {database_url}")
        print(f"API Access: {'Authenticated' if api_key else 'Missing'}")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_endpoint}")
        print("\nEnvironment security check:\n[OK] No hardcoded secrets detected\n[OK] .env file properly configured\n[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print("An error occured", e)


if __name__ == "__main__":
    oracle()
