def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        with open("new_discovery.txt", "w") as ds:
            print("Storage unit created successfully...\n")
            ds.write("[ENTRY 001] New quantum algorithm discovered")
            ds.write("[ENTRY 002] Efficiency increased by 347%")
            ds.write("[ENTRY 003] Archived by Data Archivist trainee")
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    ft_archive_creation()