import csv

# Read employee records from CSV file
employee_records = []
with open('employee_records.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employee_records.append(row)

if not employee_records:
    print("No employee records found.")
else:
    # Calculate average salary
    total_salary = sum(float(record['Salary']) for record in employee_records)
    average_salary = total_salary / len(employee_records)
    print(f"Average Salary: ${average_salary:.2f}")

    # Find top 3 earners
    sorted_records = sorted(employee_records, key=lambda x: float(x['Salary']), reverse=True)
    top_earners = sorted_records[:3]
    print("\nTop 3 Earners:")
    for i, earner in enumerate(top_earners, start=1):
        print(f"{i}. {earner['Name']}: ${earner['Salary']}")
