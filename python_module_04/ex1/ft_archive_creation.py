def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        ds = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        ds.write("[ENTRY 001] New quantum algorithm discovered\n")
        print("[ENTRY 001] New quantum algorithm discovered")
        ds.write("[ENTRY 002] Efficiency increased by 347%\n")
        print("[ENTRY 002] Efficiency increased by 347%")
        ds.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception as e:
        print(f"{e}")
    finally:
        ds.close()


if __name__ == "__main__":
    ft_archive_creation()
