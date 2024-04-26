import pandas as pd
import matplotlib.pyplot as plt

def display_pie_chart():
    month = input("Enter the month (0 for all months): ")
    year = "20" + input("Enter the last two digits of the year: ")

    df = pd.read_csv("finances.csv")

    if month != "0":
        month = int(month)
    year = int(year)

    if month != "0":
        df = df[(df["Month"] == month) & (df["Year"] == year)]
    else:
        df = df[df["Year"] == year]

    specific_types = df["Type_Specific"].unique()
    amounts = []

    for type in specific_types:
        amount = df[df["Type_Specific"] == type]["Amount"].sum()
        amounts.append(amount)

    # Create labels that include the amount 
    labels = [f'{t} (${a:.2f})' for t, a in zip(specific_types, amounts)] 

    plt.pie(amounts, labels=labels, autopct='%1.1f%%')
    plt.title(f"Expenses in {month}/{year}" if month != 0 else f"Expenses in {year}")
    plt.show()

display_pie_chart()