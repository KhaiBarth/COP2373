#In this assignment,  I am creating a function that validates user entered phone numbers, ssn, and zip code. The program reads user input and decides if the data is valid.
import re

# Create phone number input validation methods with correct formatting
def validate_phone_number(phone):

    pattern = r'^(?:\(\d{3}\)\s?|\d{3}[-.\s]?)(\d{3})[-.\s]?(\d{4})$'
    return re.match(pattern, phone) is not None

# Create social security input validation methods with correct formatting
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.match(pattern, ssn) is not None

# Create zip code input validation methods with correct formatting
def validate_zip_code(zip_code):

    pattern = r'^\d{5}(-\d{4})?$'
    return re.match(pattern, zip_code) is not None

# Have user input required data
def main():
    phone_number = input("Enter phone number: ")
    ssn = input("Enter Social Security Number: ")
    zip_code = input("Enter Zip Code: ")

    phone_valid = validate_phone_number(phone_number)
    ssn_valid = validate_ssn(ssn)
    zip_valid = validate_zip_code(zip_code)
# Display results for each
    print(f"Phone Number Valid: {phone_valid}")
    print(f"Social Security Number Valid: {ssn_valid}")
    print(f"Zip Code Valid: {zip_valid}")


if __name__ == "__main__":
    main()
