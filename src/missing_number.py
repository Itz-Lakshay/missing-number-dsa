"""
The Missing Number (DSA)
-------------------------
Given a list containing numbers from 1 to n, but one number missing,
find and print the missing number.

Build plan:
    1. Project setup                     (done)
    2. Input handling                    (this commit)
    3. Mathematical approach
    4. Data-structure-based approach
    5. Complexity comparison
    6. Output formatting
    7. Edge case handling
    8. Final polish
"""


def get_input():
    """
    Ask the user for n and the list of numbers.
    Returns a tuple: (n, numbers) where n is an int and numbers is a list of ints.

    Basic validation:
        - n must be a whole number
        - the numbers entered must actually be valid integers
    """
    while True:
        try:
            n = int(input("Enter n: ").strip())
            if n <= 0:
                print("n must be a positive whole number (n >= 1).")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number for n.")

    while True:
        raw = input("Enter numbers: ").strip()
        try:
            numbers = [int(x) for x in raw.split()]
            break
        except ValueError:
            print("Please enter numbers separated by spaces (e.g. 1 2 3 4 6 7).")

    return n, numbers

def find_missing_mathematical(n, numbers):
    """
    Approach 1: Mathematical (sum formula).

    Explanation:
        The sum of numbers from 1 to n is given by the formula n*(n+1)/2.
        Since exactly one number is missing from our list, the actual sum
        of the list will be less than this expected sum. The difference
        between the expected sum and the actual sum is the missing number.
    """
    expected_sum = n * (n + 1) // 2

    actual_sum = 0
    for num in numbers:
        actual_sum += num

    return expected_sum - actual_sum

def find_missing_data_structure(n, numbers):
    """
    Approach 2: Data-structure-based (boolean presence array).

    Explanation:
        Create a list `seen` of size n+1 (indices 0 to n), all initialized
        to False. Walk through the input numbers and mark seen[num] = True
        for each one. Then scan indices 1 to n; the index that is still
        False is the missing number.

    Note:
        Implemented manually with a boolean array rather than Python's
        set() or similar shortcuts, to build the data structure from scratch.
    """
    seen = [False] * (n + 1)

    for num in numbers:
        if 0 <= num <= n:
            seen[num] = True

    for i in range(1, n + 1):
        if not seen[i]:
            return i

    return -1  # no number missing (shouldn't happen with valid input)


def main():
    n, numbers = get_input()
    print(f"\nYou entered n = {n}")
    print(f"Numbers list = {numbers}")

    missing_math = find_missing_mathematical(n, numbers)
    print(f"\n[Mathematical Approach] Missing number: {missing_math}")

    missing_ds = find_missing_data_structure(n, numbers)
    print(f"[Data-Structure Approach] Missing number: {missing_ds}")


if __name__ == "__main__":
    main()