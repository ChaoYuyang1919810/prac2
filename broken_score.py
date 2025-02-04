#CP1404/CP5632 - Practical
'''
This is program with function to break scores to different levels
'''

def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

#  the correct code should be, for example, if you input 92, the program will output two results!
def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return  "Passable"
    elif score < 50:
        return "Bad"

main()