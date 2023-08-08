from collections import defaultdict

def main():
    n = int(input())  # Read the number of integers
    nums = list(map(int, input().split()))  # Read a line of space-separated integers and convert to a list
    m = 0  # Initialize maximum frequency variable
    r = 0  # Initialize count of integers with maximum frequency
    have = defaultdict(int)  # Create a defaultdict to store frequencies of integers

    # Loop through the list of numbers
    for x in nums:
        have[x] += 1  # Increment the frequency count for the current number
        m = max(m, have[x])  # Update the maximum frequency

    # Count how many integers have the maximum frequency
    for freq in have.values():
        if freq == m:
            r += 1

    # Print the count of integers with the maximum frequency
    print(r)

if __name__ == "__main__":
    main()
