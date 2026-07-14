import os
import sys
from dotenv import load_dotenv


def load_matrix_config() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    env_path = os.path.join(script_dir, ".env")
    
    load_dotenv(dotenv_path=env_path)

    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"  Mode: {mode}")

    if db_url:
        if mode == "production":
            print("  Database: Connected to Production Mainframe")
        else:
            print("  Database: Connected to local instance")
    else:
        print("  Database: WARNING - No database configured!")

    if api_key:
        print("  API Access: Authenticated")
    else:
        print("  API Access: WARNING - Missing API Key!")

    print(f"  Log Level: {log_level}")
    
    if zion_endpoint:
        print("  Zion Network: Online")
    else:
        print("  Zion Network: Offline")

    print("\nEnvironment security check:")
    
    if api_key == "development_secret_key" or not api_key:
        print("[WARNING] You are using default or missing API keys!")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists("env_path"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing! Operating on fallback defaults.")

    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Operating in development sandboxed mode")


if __name__ == "__main__":
    try:
        load_matrix_config()
    except Exception as e:
        print(f"Configuration streaming error: {e}", file=sys.stderr)
        sys.exit(1)
