import csv

LOANS_FILE = "loans.csv"

COURSES = ["COMP 1510", "MATH 1151", "COMM 2215"]
SHELVES = [4, 1, 7]

DEMO_RECORDS = [
    {"date": "Nov 17", "title": "Project Hail Mary",
     "borrower": "elee", "days": 12, "renewals": 1},
    {"date": "Nov 18", "title": "The Overstory",
     "borrower": "Chen, Rosa", "days": 27, "renewals": 0},
    {"date": "Nov 19", "title": "Spelunky",
     "borrower": "jmoreno", "days": 4, "renewals": 1},
]


def days_of(record: dict) -> int:
    """
    Report the number of days one loan has been out.

    :param record: one loan record
    :return: the loan's days field
    """
    return record["days"]


def longest_loan(records: list) -> dict:
    """
    Return the loan record that has been out the most days.

    :param records: the loan records to look through
    :return: the record with the largest days field. On a tie, the
             record that came first
    """
    return max(records, key=days_of())


def shelves_by_course(courses, shelves):
    pass


def longest_first(records):
    pass


def parse_row(row):
    pass


def numbered_listing(records):
    pass


def load_loans(path: str) -> list:
    """
    Read a CSV of loans and return the records that parsed.

    :param path: the CSV file to read, opened with newline="" and
                 encoding="utf-8"
    :return: one parsed record per good row, in file order. A row
             whose number fails to convert is skipped with a printed
             line and costs the program nothing
    """
    records = []
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            try:
                records.append({
                    "date": row[0],
                    "title": row[1],
                    "borrower": row[2],
                    "days": int(row[3]),
                    "renewals": int(row[4]),
                })
            except ValueError:
                print("Skipping a row with a bad number:", row[1])
    return records


def main():
    """
    Print the loan desk's morning demonstration.
    """
    print("=== Creekview Branch loan desk ===\n")

    print("The longest loan right now:")
    loan = longest_loan(DEMO_RECORDS)
    print(f'{loan["title"]}: {loan["days"]} days out')


if __name__ == "__main__":
    main()
