import time
import random
import threading

BEST_SCORE_FILE = "best_score.txt"

def load_best_score():
    try:
        with open(BEST_SCORE_FILE, "r") as f:
            return float(f.read().strip())
    except (FileNotFoundError, ValueError):
        return None

def save_best_score(score):
    with open(BEST_SCORE_FILE, "w") as f:
        f.write(str(score))

def wait_for_enter(flag):
    input()
    flag["pressed"] = True

def reaction_test():
    print("Get ready...")

    flag = {"pressed": False}
    t = threading.Thread(target=wait_for_enter, args=(flag,))
    t.start()

    wait_time = random.uniform(2, 5)
    start_wait = time.perf_counter()

    while time.perf_counter() - start_wait < wait_time:
        if flag["pressed"]:
            print("Too soon!")
            return None
        time.sleep(0.01)

    print("NOW! Press Enter as fast as you can.")
    start_time = time.perf_counter()
    input()
    end_time = time.perf_counter()

    reaction_time = (end_time - start_time) * 1000
    print(f"Your reaction time: {reaction_time:.2f} milliseconds.")
    return reaction_time

if __name__ == "__main__":
    best_score = load_best_score()

    for _ in range(5):
        score = reaction_test()

        if score is not None:
            if best_score is None or score < best_score:
                best_score = score
                save_best_score(best_score)
                print(f"New best score: {best_score:.2f} milliseconds!")

        print()

    if best_score is not None:
        print(f"Best score saved: {best_score:.2f} milliseconds")