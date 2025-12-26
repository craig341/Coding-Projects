# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.
# Example
# Given list is [2,3,6,6,5] . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
# If the list contains only one result then print "Not enough participants with different scores"

# Take array, and find 2nd largest integer

def solution(input_array):
    sorted_array = (set(input_array))  # remove duplicates by converting into a set
    if len(sorted_array) >= 2:
        new_arr = (sorted(sorted_array, key=int, reverse=True))  # sort array from largest to smallest
        return new_arr[1]  # print second-largest integer in the array
    else:
        return "Not enough participants with different scores"


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(solution(input_array=arr))
