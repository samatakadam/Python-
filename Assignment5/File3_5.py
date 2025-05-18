def is_eligible(age):
    return age >= 18

def check_voting_eligibility(age):
    if is_eligible(age):
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

def main():
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Invalid input! Age cannot be negative.")
    else:
        check_voting_eligibility(age)

if __name__ == "__main__":
    main()