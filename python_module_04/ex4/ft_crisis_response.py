def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r"):
            print("SUCCESS: Everything is going as planed")
            print("STATUS: 0 errors handled, system stable")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except Exception as e:
        print(f"{e}")
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r"):
            print("SUCCESS: Everything is going as planed")
            print("STATUS: 0 errors handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"{e}")
    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r"):
