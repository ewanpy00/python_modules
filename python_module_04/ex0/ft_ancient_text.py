def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        ds = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        text = ds.read()
        print(f"{text}")
        print("Data recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        ds.close()


if __name__ == "__main__":
    ft_ancient_text()
