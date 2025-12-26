# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# Example
# records = [["chi",20],["beta",50], ["alpha",50]]
# The ordered list of scores is [20.0, 50.0], so the second lowest score is . There are two students with that score: ["beta", "alpha"] . Ordered alphabetically, the names are printed as:
# alpha
# beta
def find_second_lowest_students(records):
    if not records:
        return []  # Handle empty input gracefully

    # Sorting records by score
    records.sort(key=lambda x: x[1])
    # Extract scores
    scores = [record[1] for record in records]
    # Unique scores sorted
    unique_scores = sorted(set(scores))

    if len(unique_scores) < 2:
        return []  # Return empty list if no second lowest grade

    # Second lowest score
    second_lowest_score = unique_scores[1]
    # Find students with the second lowest score
    second_lowest_students = [record[0] for record in records if record[1] == second_lowest_score]
    # Sort names alphabetically
    second_lowest_students.sort()
    return second_lowest_students



if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # Print each name on a new line
    for student in find_second_lowest_students(records):
        print(student)