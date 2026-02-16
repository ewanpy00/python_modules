import sys

def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    try:
        ID = input("Input Stream active. Enter archivist ID: ")
        report = input("Input Stream active. Enter status report:")

        sys.stdout.write(f"\n[STANDARD] Archive status from {ID}: {report}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        sys.stdout.write("\nThree-channel communication test successful.")
    except Exception as e:
        sys.stderr.write(e)


if __name__ == "__main__":
    ft_stream_management()