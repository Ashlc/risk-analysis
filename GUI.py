import tkinter as tk
from tkinter import ttk
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the pkl model
model = joblib.load("model/rf_credit_risk_model.pkl")


# Function to query the model
def query_model(data: dict):
    encoder = LabelEncoder()

    query = pd.DataFrame(
        {
            "Age Range": [data["Age Range"]],
            "Employment Status": [data["Employment Status"]],
            "Intention": [data["Intention"]],
            "Education Level": [data["Education Level"]],
            "Credit History": [data["Credit History"]],
            "Debt Level": [data["Debt Level"]],
            "Debt-to-Income Ratio": [data["Debt-to-Income Ratio"]],
            "Guarantor Status": [data["Guarantor Status"]],
            "Income": [data["Income"]],
        }
    )

    encoded = query.copy()
    for column in encoded.columns:
        encoded[column] = encoder.fit_transform(encoded[column])

    # Make predictions
    predictions = model.predict(encoded)

    return predictions


# Create main window
root = tk.Tk()
root.title("Loan Application Prediction")
# Set window size
root.geometry("400x450")
root.configure(bg="#fff")

# Create labels and entry/select elements
fields = [
    ("Age Range", "select", ["18-25", "26-35", "36-45", "46-55", "56+"]),
    ("Employment Status", "select", ["Employed", "Unemployed", "Self-employed"]),
    ("Intention", "select", ["Buy a house", "Invest in business", "Pay debts"]),
    ("Education Level", "select", ["High School", "Graduate", "Postgraduate"]),
    ("Credit History", "select", ["Good", "Bad", "Unknown"]),
    ("Debt Level", "select", ["None", "Low", "High"]),
    ("Debt-to-Income Ratio", "number", None),
    ("Guarantor Status", "select", ["None", "Adequate"]),
    (
        "Income",
        "select",
        ["$0 to $15k", "$15K-$35K", "$50K-$75K", "$35K-$50K", "Above $50K"],
    ),
]


# Function to create elements
def create_elements():
    for idx, (label_text, widget_type, options) in enumerate(fields):
        label = ttk.Label(
            root,
            text=label_text,
            width=20,
            anchor="w",
            background="white",
            foreground="#27ae60",
        )
        label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
        if widget_type == "number":
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky="ew")
            entries[label_text] = entry
        elif widget_type == "select":
            entry = tk.StringVar(root)
            entry.set(options[0])
            dropdown = ttk.Combobox(root, textvariable=entry, values=options, width=17)
            dropdown.grid(row=idx, column=1, padx=10, pady=5, sticky="ew")
            entries[label_text] = entry


# Function to get user input and query model
def predict_loan():
    user_input = {key: val.get() for key, val in entries.items()}
    print(user_input)
    prediction = query_model(user_input)
    result.config(text=f"{prediction[0]}")


# Create elements
entries = {}
create_elements()

# Create predict button
button = tk.Button(
    root,
    text="Predict",
    command=lambda: predict_loan(),
    bg="#27ae60",
    fg="white",
    bd=0,
    height=2,
    width=10,
)

button.grid(row=len(fields), columnspan=2, pady=20, sticky="ew")

# Create result label
result_label = ttk.Label(root, text="Risk Level: ", background="white")
result_label.grid(row=len(fields) + 1, columnspan=2, pady=5)

# Result label
result = ttk.Label(root, text="", font=("Arial", 14), background="white")
result.grid(row=len(fields) + 2, columnspan=2, pady=10)  # Place on a different row

# Centering elements horizontally
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=5)
    if isinstance(child, (ttk.Entry, ttk.Combobox)):
        child.configure(width=20)

# Configure rows and columns to fill available space
root.grid_rowconfigure(len(fields) + 3, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the application
root.mainloop()
