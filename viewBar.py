import pandas as pd
import matplotlib.pyplot as plt

def display_bar_chart():
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

    # Create the bar chart
    plt.bar(specific_types, amounts)

    # Add amount labels above each bar
    for i, amount in enumerate(amounts):
        plt.text(i, amount + 0.1, f"${amount:.2f}", ha='center') 

    df_grouped = df.groupby(['Type_General', 'Type_Specific'])['Amount'].sum().unstack()
    df_grouped.plot(kind='bar', stacked=True)

    plt.xlabel("Type_General")
    plt.ylabel("Amount")
    plt.title(f"Expenses in {month}/{year}" if month != 0 else f"Expenses in {year}")
    plt.show()

display_bar_chart()