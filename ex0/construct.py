import sys
import os
import site


def check_virtual_env():
    # In a virtual environment, sys.prefix points to the env, 
    # while sys.base_prefix points to the global Python installation.
    is_venv = sys.prefix != sys.base_prefix
    
    print("=" * 50)
    print("          PYTHON ENVIRONMENT DETECTOR          ")
    print("=" * 50)
    
    if is_venv:
        print("[STATUS] Inside a Virtual Environment: YES")
        print(f"Current Env Name:  {os.path.basename(sys.prefix)}")
        print(f"Env Location:      {sys.prefix}")
        print(f"Python Executable: {sys.executable}")
        
        print("\n--- Package Locations ---")
        print(f"Virtual Env Site-Packages: {site.getsitepackages()[0]}")
        # Base prefix site-packages (approximate global location)
        print(f"Global Base Location:      {sys.base_prefix}")
        
    else:
        print("[STATUS] Inside a Virtual Environment: NO (Global Environment)")
        print(f"Python Executable: {sys.executable}")
        print(f"Global Site-Packages:     {site.getsitepackages()[0]}")
        
        print("\n" + "!" * 50)
        print("INSTRUCTIONS TO CREATE & ACTIVATE A VIRTUAL ENVIRONMENT")
        print("!" * 50)
        print("1. Create a virtual environment named 'matrix_env':")
        print("   python3 -m venv matrix_env")
        print("\n2. Activate it based on your OS:")
        print("   - macOS/Linux:")
        print("     source matrix_env/bin/activate")
        print("   - Windows (Command Prompt):")
        print("     matrix_env\\Scripts\\activate.bat")
        print("   - Windows (PowerShell):")
        print("     .\\matrix_env\\Scripts\\Activate.ps1")
        print("\n3. Run this script again to see the difference:")
        print("   python3 construct.py")
    print("=" * 50)

if __name__ == "__main__":
    check_virtual_env()
