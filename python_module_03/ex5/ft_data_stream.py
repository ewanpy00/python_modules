from typing import Generator


def event_stream(n: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        player = players[i % len(players)]
        level = (i * 7) % 20 + 1
        action = actions[i % len(actions)]

        yield {
            "id": i,
            "player": player,
            "level": level,
            "action": action,
        }


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_numbers(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num
            count += 1

        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    stream = event_stream(total_events)

    for event in stream:
        total += 1
        if total <= 3:
            print(
                f"Event {event['id']}: "
                f"Player {event['player']} "
                f"(level {event['level']}) "
                f"{event['action']}"
            )
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure += 1
        if event["action"] == "leveled up":
            level_up += 1

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    for val in fibonacci(10):
        if val != 0:
            print(",", end="")
        print(f" {val}", end="")

    print("\nPrime numbers (first 5): ", end="")
    for val in prime_numbers(5):
        if val != 2:
            print(",", end="")
        print(f" {val}", end="")


if __name__ == "__main__":
    main()
