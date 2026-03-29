import json
import os
import random


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "questions.json")

# How many questions to pick per difficulty for a full journey game
JOURNEY_PICK = {"easy": 5, "medium": 6, "hard": 4}


# ─────────────────────────────────────────────
#  LOAD
# ─────────────────────────────────────────────

def load_questions(difficulty=None):
    """
    Load questions from JSON, optionally filtered by difficulty.

    Args:
        difficulty (str): 'easy', 'medium', 'hard', or None for all.

    Returns:
        list: List of question dicts.
    """
    if not os.path.exists(FILE_PATH):
        print(f"Error: questions.json not found at {FILE_PATH}")
        return []

    with open(FILE_PATH, "r") as f:
        all_questions = json.load(f)

    if difficulty:
        filtered = [q for q in all_questions if q["difficulty"] == difficulty.lower()]
        if not filtered:
            print(f"No questions found for difficulty: {difficulty}")
        return filtered

    return all_questions


# ─────────────────────────────────────────────
#  RANDOM SELECTION — used by game every run
# ─────────────────────────────────────────────

def get_questions_by_difficulty():
    """
    Randomly pick questions for a full journey game:
    5 easy + 6 medium + 4 hard = 15 unique questions.
    Different questions appear every game.

    Returns:
        list: 15 randomly selected questions in KBC order.
    """
    easy   = random.sample(load_questions("easy"),   JOURNEY_PICK["easy"])
    medium = random.sample(load_questions("medium"), JOURNEY_PICK["medium"])
    hard   = random.sample(load_questions("hard"),   JOURNEY_PICK["hard"])

    # Assign correct prize ladder values in order
    prizes = [
        1000, 2000, 3000, 5000, 10000,
        20000, 40000, 80000, 160000, 320000, 640000,
        1250000, 2500000, 5000000, 10000000
    ]

    all_15 = easy + medium + hard
    for i, q in enumerate(all_15):
        q["prize"] = prizes[i]

    return all_15


def get_random_questions(count=15):
    """
    Pick `count` completely random questions from the full bank.

    Args:
        count (int): Number of questions to return.

    Returns:
        list: Randomly selected questions.
    """
    all_q = load_questions()
    if len(all_q) < count:
        print(f"Warning: Only {len(all_q)} questions available.")
        return all_q
    return random.sample(all_q, count)


def get_questions_for_mode(mode):
    """
    Return questions for a given game mode.

    Args:
        mode (str): 'journey', 'easy', 'medium', or 'hard'.

    Returns:
        list: Questions ready to play.
    """
    if mode == "journey":
        return get_questions_by_difficulty()

    pool = load_questions(mode)
    count = min(len(pool), JOURNEY_PICK.get(mode, 5))
    return random.sample(pool, count)


# ─────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────

def display_question(question):
    """Print a question with options formatted nicely."""
    print(f"\n  {question['question']}")
    print("  " + "-" * 48)
    for key, value in question["options"].items():
        print(f"  {key}) {value}")
    print("  " + "-" * 48)


def get_prize_money(question):
    """Return prize formatted as ₹10,000 string."""
    return f"₹{int(question['prize']):,}"


# ─────────────────────────────────────────────
#  QUICK TEST
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("        Testing questions.py — 90 Question Bank")
    print("=" * 55)

    # Test 1: Total count
    all_q = load_questions()
    print(f"\n✅ Total questions in bank : {len(all_q)}")

    # Test 2: Per difficulty
    easy   = load_questions("easy")
    medium = load_questions("medium")
    hard   = load_questions("hard")
    print(f"✅ Easy: {len(easy)} | Medium: {len(medium)} | Hard: {len(hard)}")

    # Test 3: Journey pick (should always be 15)
    game1 = get_questions_by_difficulty()
    game2 = get_questions_by_difficulty()
    print(f"\n✅ Game 1 — {len(game1)} questions picked")
    print(f"✅ Game 2 — {len(game2)} questions picked")

    # Test 4: Confirm different questions each game
    ids1 = {q["id"] for q in game1}
    ids2 = {q["id"] for q in game2}
    overlap = ids1 & ids2
    print(f"✅ Overlap between game 1 & 2: {len(overlap)} questions (expected ~0-5)")

    # Test 5: Prize ladder correctly applied
    print(f"\n✅ Prize ladder for game 1:")
    for q in game1:
        print(f"   {q['difficulty'].upper():<8} | {get_prize_money(q):<16} | {q['question'][:45]}...")