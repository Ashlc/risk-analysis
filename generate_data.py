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
    age_range = random.choice(["18-25", "26-35", "36-45", "46-55", "56+"])
    employment = random.choice(employment_status)
    intention_val = random.choice(intention)
    education = random.choice(education_level)
    credit_hist = random.choice(credit_history)
    income = random.choice(income_ranges)
    debt = None
    guarantor = random.choice(guarantor_status)

    if employment == "Unemployed":
        debt = random.choice(debt_level)
    else:
        # Adjusting debt level based on income
        if income == "$0 to $15K":
            debt = random.choice(["High", "Low"])
        elif income == "$15K to $35K":
            debt = random.choice(["High", "Low", "None"])
        elif income == "$35K to $50K":
            debt = random.choice(["Low", "None"])
        else:
            debt = "None"

    # Calculating Debt-to-Income Ratio
    income_value = income_ranges.index(income) * 15000  # Assuming mid-point of income range
    if income_value == 0:
        dti_ratio = 0  # To avoid division by zero
    else:
        dti_ratio = random.uniform(0, 1.5) * 1000 / income_value  # Random DTI between 0 and 1.5
    dti_ratio = round(dti_ratio, 2)

    # Adjust risk level based on conditions
    if credit_hist == "Good" and guarantor == "Adequate":
        risk = random.choice(["Low", "Moderate"])
    else:
        risk = random.choice(["High", "Moderate"])
    
    # Adjusting intention based on education level
    if education == "High School":
        intention_val = random.choice(["Pay debts", "Invest in business"])
    elif education == "Graduate":
        intention_val = random.choice(["Buy a house", "Invest in business"])
    else:
        intention_val = random.choice(["Buy a house", "Pay debts"])

    # Adjusting employment status based on age range
    if age_range in ["18-25", "26-35"]:
        employment = random.choice(["Unemployed", "Employed", "Self-Employed"])
    elif age_range in ["36-45", "46-55"]:
        employment = random.choice(["Employed", "Unemployed"])
    else:
        employment = "Employed"

    # Adjusting risk level based on conditions
    if credit_hist == "Good" and guarantor == "Adequate":
        if debt == "High":
            risk = random.choice(["Moderate", "Low"])
        elif debt == "Low":
            risk = "Low"
        else:
            if intention_val == "Buy a house":
                risk = random.choice(["Low", "Moderate"])
            elif intention_val == "Invest in business":
                risk = "Moderate"
            else:
                risk = "Low"
    else:
        if debt == "None":
            risk = "Low"
        elif debt == "Low":
            risk = random.choice(["Low", "Moderate"])
        else:
            if intention_val == "Buy a house":
                risk = random.choice(["Moderate", "High"])
            elif intention_val == "Invest in business":
                risk = random.choice(["Moderate", "High"])
            else:
                risk = "High"


    data["Age Range"].append(age_range)
    data["Employment Status"].append(employment)
    data["Intention"].append(intention_val)
    data["Education Level"].append(education)
    data["Credit History"].append(credit_hist)
    data["Debt Level"].append(debt)
    data["Guarantor Status"].append(guarantor)
    data["Income"].append(income)
    data["Debt-to-Income Ratio"].append(dti_ratio)
    data["Risk Level"].append(risk)

df = pd.DataFrame(data)
df.to_csv("data/credit_analysis.csv", index=False)
print("CSV file generated successfully!")
