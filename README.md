# Property Price Prediction Model

A Machine Learning-based property valuation system developed to estimate residential property prices using housing-related features such as area, bedrooms, bathrooms, parking availability, location score, property age, and furnishing status. This project uses **Linear Regression** for numerical price prediction, **Pickle** for model serialization, and **Streamlit** for real-time property cost estimation.

---

## 📌 Project Overview

Accurate property valuation is a major requirement in the real estate industry. Property prices depend on several important factors including total area, number of rooms, parking facilities, property age, furnishing level, and location quality. This project automates residential property price estimation by training a regression model on structured housing records and predicting approximate market value based on user inputs.

---

## 🎯 Objectives

- Predict residential property prices automatically
- Analyze the influence of housing features on price valuation
- Reduce manual real-estate estimation effort
- Deploy a real-time property prediction web application

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Linear Regression
- Pickle
- Streamlit
- OpenPyXL
- Jupyter Notebook

---

## 📂 Dataset Information

This project uses a structured residential housing dataset containing multiple numerical property features for supervised regression model training.

### Dataset Features:

| Column Name | Description |
|-------------|-------------|
| Area | Total property area in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Parking | Parking availability |
| Location_Score | Quality score of property location |
| Property_Age | Age of the property |
| Furnishing_Status | Furnished / Unfurnished indicator |
| Price | Target residential property price |

Dataset File: `property_price_prediction_dataset.csv.xlsx`

---

## ⚙️ Machine Learning Workflow

1. Load Excel housing dataset using Pandas  
2. Perform feature-target separation  
3. Apply train-test split  
4. Train Linear Regression regression model  
5. Predict prices on unseen test records  
6. Evaluate model using regression metrics  
7. Save trained model using Pickle  
8. Deploy model using Streamlit web interface

---

## 📈 Model Performance

The trained Linear Regression property valuation model achieved excellent numerical prediction performance on test housing records.

- **R² Score:** 0.993
- **Mean Absolute Error (MAE):** 44,113
- **Mean Squared Error (MSE):** 2,686,488,855

The model was able to estimate residential property prices with very high regression accuracy and minimal average numerical error.

---

## 💻 Real-Time Prediction Example

```python
new_house = np.array([[2000, 3, 2, 1, 8, 5, 1]])
predicted_price = model.predict(new_house)
```

Output:

```python
Predicted Property Price Generated Successfully
```

---

## 🚀 Streamlit Web Application

A Streamlit-based frontend application is integrated with the Pickle model where users can enter property specifications and instantly receive the estimated residential market price.

### To Run the App:

```bash
streamlit run property_price_prediction.py
```

---

## 📁 Project Structure

```bash
Property-Price-Prediction-Model/
│
├── property_price_prediction_dataset.csv.xlsx
├── Property_Price_Prediction.ipynb
├── property_price_model.pkl
├── property_price_prediction.py
└── README.md
```

---

## ✅ Key Features

- Structured housing price dataset analysis
- Linear Regression-based residential property valuation
- Achieved R² score of 0.993
- Low prediction error with MAE of 44,113
- Pickle serialized trained regression model
- Real-time Streamlit deployment
- Interactive user property input interface

---

## 🔮 Future Enhancements

- Integrate real-time market datasets
- Train with advanced regressors like Random Forest and XGBoost
- Add property analytics dashboard
- Deploy online for public usage

---

## 👨‍💻 Author

**PONNADA RUDRA NAGA TEJA**  
Email: ponnadarudra99@gmail.com  
LinkedIn: linkedin.com/in/ponnada-rudra-naga-teja-586561323  
GitHub: github.com/ponnadarudra99-wq
