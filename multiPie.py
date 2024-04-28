import pandas as pd
import matplotlib.pyplot as plt

def display_nested_pie_chart():
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

    # Data Preparation for Nested Chart
    df_grouped = df.groupby(['Type_General', 'Type_Specific'])['Amount'].sum()
    df_general = df_grouped.groupby(level=0).sum()

    # Create the nested pie chart 
    fig, ax = plt.subplots()

    # Outer circle (Type_General)
    wedges, _ = ax.pie(df_general.values, radius=1, labels=df_general.index, autopct="%1.1f%%")

    # Inner circles (Type_Specific)
    num_types_general = len(df_general.index) 
    colors = plt.cm.get_cmap('viridis')(np.linspace(0, 1, num_types_general))  # Vary colors

    for i, type_general in enumerate(df_general.index):
        data = df_grouped.loc[type_general]
        wedge_radius = 0.6  # Make the inner circles smaller 
        wedge_start = sum(df_general.values.cumsum()[:-1]) / sum(df_general.values) * 2 * np.pi

        ax.pie(data.values, radius=wedge_radius, colors=colors[i],
               labels=data.index, autopct="%1.1f%%", startangle=90 + wedge_start * 180 / np.pi)

    ax.set_title(f"Nested Expenses in {month}/{year}" if month != 0 else f"Nested Expenses in {year}")

display_nested_pie_chart()
