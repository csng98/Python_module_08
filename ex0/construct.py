import os
import site
import sys


def check_virtual_env() -> None:
    """Detects and displays Python environment
    status matching Matrix parameters."""
    is_venv: bool = sys.prefix != sys.base_prefix

    if not is_venv:
        print("\nMATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("  python3 -m venv matrix_env")
        print("  source matrix_env/bin/activate  # On Unix")
        print("  matrix_env\\Scripts\\activate     # On Windows\n")
        print("Then run this program again.")
    else:
        env_name: str = os.path.basename(sys.prefix)
        site_pkgs: str = site.getsitepackages()[0]

        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(f"  {site_pkgs}")


if __name__ == "__main__":
    check_virtual_env()
