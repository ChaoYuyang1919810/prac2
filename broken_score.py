#CP1404/CP5632 - Practical
'''
This is program with function to break scores to different levels
'''

def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return  "Passable"
    elif score < 50:
        return "Bad"

main()