import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk

# Data
data = {
    'hours': [1,2,3,4,5,6,7,8],
    'attendance': [60,65,70,75,80,85,90,95],
    'marks': [30,35,40,50,55,60,70,80]
}

df = pd.DataFrame(data)

# Model
X = df[['hours', 'attendance']]
y = df['marks']

model = LinearRegression()
model.fit(X, y)

# Function
def predict():
    h = float(hours_entry.get())
    a = float(attendance_entry.get())
    result = model.predict([[h, a]])
    result_label.config(text=f"Predicted Marks: {result[0]:.2f}")

# UI
root = tk.Tk()
root.title("Student Predictor")

tk.Label(root, text="Study Hours").pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

tk.Label(root, text="Attendance").pack()
attendance_entry = tk.Entry(root)
attendance_entry.pack()

tk.Button(root, text="Predict", command=predict).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()