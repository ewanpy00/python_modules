import sys

class NameError(Exception):
    pass

def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    score_list = sys.argv
    if len(score_list) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    try:
        min_val = min(int(value) for value in score_list[1:]) 
        max_val = max(int(value) for value in score_list[1:])
        result = sum(int(value) for value in score_list[1:])
        print(f"Scores procesesed: {score_list[1:]}")
        print(f"Total players: {len(score_list) - 1}")
        print(f"Total score: {result}")
        print(f"Average score: {result / (len(score_list) - 1)}")
        print(f"High score: {max_val}")
        print(f"Low score: {min_val}")
        print(f"Score range: {max_val - min_val}")
    except Exception as e:
        print(f"Enter the valid arguments!!!")
    

if __name__ == "__main__":
    ft_score_analytics()