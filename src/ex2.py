import csv
def find_total_visits():
    total_visits = {}
    file_names = {"C:\\Users\\f9xuyp3\python-3\\files\\week-1.csv", "C:\\Users\\f9xuyp3\python-3\\files\\week-2.csv", "C:\\Users\\f9xuyp3\python-3\\files\\week-3.csv"}
    for file_name in file_names:
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                # The below code skips the header line
                next(reader)
                for row in reader:
                    if len(row) >= 2:
                        member_name = row[0]
                        visits = [int(val) for val in row[1:]]
                        total_visits[member_name] = total_visits.get(member_name, 0) + sum(visits)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            continue
        
    totalVisits = 0
    for key, value in total_visits.items():
        totalVisits += value
    return totalVisits


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()
