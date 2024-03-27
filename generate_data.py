import pandas as pd
import random

# Defining ranges for each column
income_ranges = ["$0 to $15K", "$15K to $35K", "$35K to $50K", "Above $50K"]
employment_status = ["Employed", "Unemployed", "Self-Employed"]
intention = ["Buy a house", "Pay debts", "Invest in business"]
education_level = ["High School", "Graduate", "Postgraduate"]
credit_history = ["Unknown", "Poor", "Good"]
debt_level = ["High", "Low", "None"]
guarantor_status = ["None", "Adequate"]
risk_level = ["High", "Moderate", "Low"]

data = {
    "Age Range": [],
    "Employment Status": [],
    "Intention": [],
    "Education Level": [],
    "Credit History": [],
    "Debt Level": [],
    "Debt-to-Income Ratio": [],
    "Guarantor Status": [],
    "Income": [],
    "Risk Level": [],
}

for _ in range(1000):
    data["Age Range"].append(random.choice(["18-25", "26-35", "36-45", "46-55", "56+"]))
    data["Employment Status"].append(random.choice(employment_status))
    data["Intention"].append(random.choice(intention))
    data["Education Level"].append(random.choice(education_level))
    data["Credit History"].append(random.choice(credit_history))

    if data["Employment Status"][-1] == "Unemployed":
        data["Debt Level"].append(random.choice(debt_level))
    else:
        data["Debt Level"].append(random.choice(["Low", "None"]))

    data["Guarantor Status"].append(random.choice(guarantor_status))
    data["Income"].append(random.choice(income_ranges))
    
    # Calculating Debt-to-Income Ratio
    income_value = income_ranges.index(data["Income"][-1]) * 15000  # Assuming mid-point of income range
    if income_value == 0:
        dti_ratio = 0  # To avoid division by zero
    else:
        dti_ratio = random.uniform(0, 1.5) * 1000 / income_value  # Random DTI between 0 and 1.5
    data["Debt-to-Income Ratio"].append(round(dti_ratio, 2))

    # Adjust risk level based on conditions
    if data["Credit History"][-1] == "Good" and data["Guarantor Status"][-1] == "Adequate":
        data["Risk Level"].append(random.choice(["Low", "Moderate"]))
    else:
        data["Risk Level"].append(random.choice(["High", "Moderate"]))

df = pd.DataFrame(data)
df.to_csv("data/credit_analysis.csv", index=False)
print("CSV file generated successfully!")
