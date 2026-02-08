import sys
class NameError(Exception):
    pass

def ft_score_analytics():
    print("=== Player Score Analytics ===")
    score_list = sys.argv
    print(f"Scores procesesed: {score_list[1:]}")
    print(f"Total players: {len(score_list) - 1}")
    
    result = sum(int(value) for value in score_list[1:])
    print(f"Total score: {result}")
    print(f"Average score: {result / (len(score_list) - 1)}")
    print(f"High score: {max(int(value) for value in score_list[1:])}")
    print(f"Low score: {min(int(value) for value in score_list[1:])}")
    print(f"Score range: {max(int(value) for value in score_list[1:]) - min(int(value) for value in score_list[1:])}")

if __name__ == "__main__":
    ft_score_analytics()