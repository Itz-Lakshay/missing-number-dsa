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


def main():
    n, numbers = get_input()
    print(f"\nYou entered n = {n}")
    print(f"Numbers list = {numbers}")

    missing_math = find_missing_mathematical(n, numbers)
    print(f"\n[Mathematical Approach] Missing number: {missing_math}")


if __name__ == "__main__":
    main()