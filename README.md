# The Missing Number (DSA)

## Problem Statement
You are given a list containing numbers from 1 to n, but one number is missing
from the list. Write a program that takes `n` and the list of numbers as
input, finds the missing number, and prints the result.

**Example:**
```
Enter n: 7
Enter numbers: 1 2 3 4 6 7
Missing number: 5
```

## Requirements
- Works with lists of different sizes
- Does not use a built-in function that directly solves the problem
- Solved using a custom algorithm
- Bonus: solved using two different approaches (mathematical & data-structure-based)
- Bonus: time and space complexity of both approaches compared

## Project Structure
```
missing-number-dsa/
├── src/
│   └── missing_number.py   # main program
└── README.md
```

## Approach

### 1. Mathematical Approach
The sum of numbers from 1 to n is given by the formula `n*(n+1)/2`. Since
exactly one number is missing, the actual sum of the given list will be
less than this expected sum. The missing number is simply:

```
missing number = expected_sum - actual_sum
```

The actual sum is computed with a manual loop (not Python's `sum()`) to
keep the algorithm fully self-implemented.

- **Time complexity:** O(n) — one pass through the list to total it up
- **Space complexity:** O(1) — only a couple of extra variables

### 2. Data-Structure-Based Approach (Boolean Presence Array)
A boolean array `seen` of size `n+1` is created, all initialized to
`False`. Each number in the input list marks the corresponding index as
`True`. Scanning indices 1 to n, the first index still `False` is the
missing number.

- **Time complexity:** O(n) — one pass to mark, one pass to scan
- **Space complexity:** O(n) — the extra boolean array

### Complexity Comparison
| Approach              | Time | Space |
|------------------------|------|-------|
| Mathematical            | O(n) | O(1)  |
| Data-structure (array)  | O(n) | O(n)  |

**Conclusion:** Both approaches run in O(n) time, but the mathematical
approach is more space-efficient. The data-structure approach, however,
generalizes more easily to variations of this problem (e.g. finding
multiple missing numbers, or handling duplicates).

## Input Validation & Edge Cases
- `n` must be a positive whole number
- The numbers list must contain exactly `n-1` values (since one is missing)
- All numbers must be within the valid range (1 to n)
- Duplicate numbers are rejected
- Clear warning messages are shown for any invalid input, instead of
  silently producing an incorrect result

## How to Run
```bash
python src/missing_number.py
```

Example session:
```
========================================
   THE MISSING NUMBER (DSA)
========================================
Enter n: 7
Enter numbers: 1 2 3 4 6 7

--- Input Summary ---
n            : 7
Numbers list : [1, 2, 3, 4, 6, 7]

--- Results ---
[Mathematical Approach]     Missing number: 5
[Data-Structure Approach]   Missing number: 5

--- Complexity Comparison ---
Mathematical Approach:
  Time complexity : O(n)  - one pass to sum the numbers
  Space complexity: O(1)  - only a couple of extra variables used

Data-Structure Approach (boolean array):
  Time complexity : O(n)  - one pass to mark seen numbers, one pass to scan
  Space complexity: O(n)  - extra array of size n+1 used

Conclusion:
  Both approaches run in O(n) time, but the mathematical approach
  is more space-efficient (O(1) vs O(n)). The data-structure
  approach, however, generalizes more easily to variations of
  this problem (e.g. multiple missing numbers, duplicates).
========================================
```

## Skills Demonstrated
Arrays/lists, loops, basic algorithms, problem-solving, time & space
complexity analysis.

## Status
✅ Complete — built incrementally via meaningful Git commits.