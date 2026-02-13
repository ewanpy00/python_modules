def ft_ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        with open("ancient_fragment.txt", "r") as ds:
            print("Connection established...\n")
            text = ds.read()
        print(f"{text}")
    except Exception as e:
        print(f"{e}")
    finally:
        ds.close()
        print("Data recovery complete. Storage unit disconnected.")

if __name__ == "__main__":
    ft_ancient_text()