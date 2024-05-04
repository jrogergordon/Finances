import pandas as pd

# Specify the month and year here
month = "5"
year = "2024"
# type_specific = "Subscr"
# type_general = "Necessity"

# Define the types
specific_types = ["BS Food", "Miscellaneous BS", "Subscriptions", "Debt Payments", "Transportation", "Groceries", "Health Care", "Phone", "Internet", "Rent", "Games", "Grooming", "Weed"]
general_types = ["Fun Self", "Necessity", "Social", "Romantic"]

def add_entry():
    global month, year
    # type_specific, type_general
    
    print("Specific Types:")
    for i, type in enumerate(specific_types):
        print(f"{i+1}. {type}")
    type_specific_index = int(input("Enter the number of the specific type of transaction: "))
    type_specific = specific_types[type_specific_index - 1]

    print("\nGeneral Types:")
    for i, type in enumerate(general_types):
        print(f"{i+1}. {type}")
    type_general_index = int(input("Enter the number of the general type of transaction: "))
    type_general = general_types[type_general_index - 1]

    amount = float(input("Enter the amount: "))

    new_entry = {
        "Month": month,
        "Year": year,
        "Type_Specific": type_specific,
        "Type_General": type_general,
        "Amount": amount
    }

    try:
        df = pd.read_csv("finances.csv")
        df = df.append(new_entry, ignore_index=True)
        df.to_csv("finances.csv", index=False)
    except FileNotFoundError:
        pd.DataFrame([new_entry]).to_csv("finances.csv", index=False)

    print("Entry added successfully!")

while True:
    add_entry()
    cont = input("Do you want to add another entry? (yes/no): ")
    if cont.lower() != "yes":
        break