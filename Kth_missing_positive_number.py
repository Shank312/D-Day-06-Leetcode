
def findKthPositive(arr, k):
    # Count of missing numbers found so far
    missing = 0

    # Current we are checking (start from 1 since we want positive numbers)
    current = 1

    # Index for traversing the given array
    i = 0

    # Keep looping until we return the Kth missing number
    while True:
        # Case 1: If current number exist in arr, skip it
        if i < len(arr) and arr[i] == current:
            i += 1                             # move to next element in arr
        else:
        # Case 2: The current number is missing 
             missing += 1

             # If we found the Kth missing number, return it
             if missing == k:
                 return current
        
        # move to the next number
        Current += 1

    