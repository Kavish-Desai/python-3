import boto3
from botocore.exceptions import ClientError

def calculate():
    calculations = []

    while True:
        try:
            user_input = input("Enter a number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break

            num1 = float(user_input)
            num2 = float(input("Enter another number: "))
            result = num1 + num2
            calculations.append(f"{num1} + {num2} = {result}\n")
            print(f"{num1} + {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
    
    if calculations:
        # Writing calculations to local log file
        file_name = 'calculator-log.txt'
        with open(file_name, 'w') as file:
            file.writelines(calculations)

        # Uploading log file to S3
        student_id = 'your_student_id'  # Replace with your actual student ID
        bucket_name = 'your_bucket_name'  # Replace with your S3 bucket name
        s3 = boto3.client('s3')
        s3.upload_file(file_name, bucket_name, f"{file_name.split('.')[0]}_{student_id}.txt")
        print("*** Uploaded to S3 ***")


def ex4():
    calculate()

ex4()
