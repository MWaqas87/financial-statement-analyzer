
import pandas as pd

def calculate_ratios(df):
    df["Gross_Profit"] = df["Revenue"] - df["COGS"]
    df["Gross_Margin"] = df["Gross_Profit"] / df["Revenue"]
    df["Net_Margin"] = df["Net_Income"] / df["Revenue"]
    df["ROE"] = df["Net_Income"] / df["Shareholders_Equity"]
    df["ROA"] = df["Net_Income"] / df["Total_Assets"]
    df["Current_Ratio"] = df["Current_Assets"] / df["Current_Liabilities"]
    df["Quick_Ratio"] = (df["Current_Assets"] - df["Inventory"]) / df["Current_Liabilities"]
    df["Debt_to_Equity"] = df["Total_Liabilities"] / df["Shareholders_Equity"]
    df["Interest_Coverage"] = df["Operating_Income"] / df["Interest_Expense"]
    return df
