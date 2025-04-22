
# 📊 Financial Statement Analyzer

An interactive Streamlit app that allows users to upload company financial statements and automatically calculate key financial ratios—enabling quick performance evaluation across profitability, liquidity, leverage, and efficiency dimensions.

---

## 🚀 Features

- Upload financial data in `.csv` format
- Automatically compute essential financial ratios:
  - Gross Margin
  - Net Margin
  - Return on Assets (ROA)
  - Return on Equity (ROE)
  - Current & Quick Ratios
  - Debt to Equity Ratio
  - Interest Coverage Ratio
- Visualize ratio trends over time
- Built with a clean and responsive Streamlit interface

---

## 📸 Screenshots

*Coming soon*: Add screenshots of the app in action showing the table and chart views.

---

## 🧪 Sample Input

You can test the app using the `sample_financials.csv` file provided in the `data/` folder. The structure should include:

```csv
Year,Revenue,COGS,Operating_Income,Net_Income,Total_Assets,Total_Liabilities,Shareholders_Equity,Current_Assets,Current_Liabilities,Inventory,Interest_Expense
2022,500000,300000,80000,60000,900000,400000,500000,300000,150000,50000,10000
...
```

---

## 📁 Project Structure

```
financial-statement-analyzer/
├── app/
│   ├── app.py              # Streamlit application
│   └── utils.py            # Ratio calculation logic
├── data/
│   └── sample_financials.csv
├── requirements.txt
└── README.md
```

---

## 💻 Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/financial-statement-analyzer.git
cd financial-statement-analyzer/app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 🛠 Technologies Used

- Python 3.9+
- Streamlit
- Pandas
- Matplotlib

---

## 📚 Use Cases

- Equity research and financial analysis
- Portfolio screening and fundamental analysis
- Academic and business analytics learning

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Mohammad Waqas**  
[LinkedIn](https://www.linkedin.com/in/mohammad-waqas-29972959/) | MSBA @ Georgetown | Sr. Banker @ BofA

---

## ⭐️ Feedback or Contributions

Feel free to open an issue, fork the repo, or suggest enhancements—I'd love to collaborate!
