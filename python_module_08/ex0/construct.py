import os
import site
import sys

def construct():
    is_env = sys.prefix != sys.base_prefix

    if is_env is True:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.version}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!\nSafe to install packages without affecting\nthe global system.")
        print(f"\nPackage installation path:\n{site.getsitepackages()[0]}")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.version}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!\nThe machines can see everything you install.\n")
        print("To enter the construct, run:\npython -m venv matrix_env\nsource matrix_env/bin/activate")
        print("\nThen run this program again.")

if __name__ == "__main__":
    construct()
