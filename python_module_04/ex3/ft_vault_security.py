def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    try:
        print("Initiating secure vault access...")
        with open("ancient_fragment.txt", "r") as ds:
            print("Vault connection established with failsafe protocols")
            text = ds.read()
        print("SECURE EXTRACTION:")
        print(text)
    except Exception as e:
        print(f"{e}")
    try:
        with open("ancient_fragment.txt", "r") as ds:
            print("SECURE PRESERVATION:")
            ds.write("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
    except Exception as e:
        print(f"{e}")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
