from random import randint, choice, uniform

WORDS = [
    "notion",
    "vote",
    "python",
    "ctypes",
    "c",
    "curl",
    "linen",
    "goal",
    "fox",
    "theorist",
    "fuel",
    "productive",
    "delay",
    "topple",
    "settle",
    "throw",
    "support",
    "charge",
    "folk",
    "apparatus",
    "publisher",
    "executive",
    "plug",
    "complain",
    "quarrel",
    "rocket",
    "pray",
    "warm",
    "exempt",
    "precision",
    "spray",
    "message",
    "model",
    "dealer",
    "color",
    "trick",
    "bench",
    "hospital",
    "fan",
    "contact",
    "cousin",
    "greeting",
    "top",
    "rise",
    "waterfall",
    "minute",
    "courtesy",
    "coalition",
    "vote",
    "abc",
    "efg",
    "u",
    "hello",
    "hi",
    "hey",
    "hola",
    "guitar",
    "code",
    "foo",
    "bar",
    "susan",
    "annie",
    "john",
    "josh",
    "jake",
    "kale",
    "hash",
    "array",
    "class",
    "function",
    "annie",
    "bart",
    "glee",
    "jump",
]

# UTILITY FUNCTIONS


def get_random_words(n: int, max_length: int):
    """
    n: number of words to generate
    max_length: maximum length of each word
    """
    if max_length == 1:
        return [word[:max_length] for word in WORDS[:n]]
    if max_length == 0:
        raise ValueError("Max length must be greater than 0")

    word_list = set()  # unique words
    seen = set()
    while len(word_list) < n:
        if len(seen) >= len(WORDS) // 2:
            break
        word = choice(WORDS)
        seen.add(word)
        if len(word) <= max_length:
            word_list.add(word)

    if len(word_list) != n:
        print(f"Warning: {len(word_list)} words generated, {n} words expected.")
    return list(word_list)


def set_upper(upper_bound: int | float | None, type: str):
    if upper_bound == None:
        if type == "int":
            return randint(47, 99)
        if type == "uint":
            return randint(80, 128)
        if type == "double":
            return uniform(47, 102)
    return upper_bound


def set_lower(lower_bound: int | float | None, type: str):
    if lower_bound == None:
        if type == "int":
            return randint(-99, -47)
        if type == "uint":
            return randint(0, 13)
        if type == "double":
            return uniform(-102, -47)
    return lower_bound
