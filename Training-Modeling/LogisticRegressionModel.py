import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report
from joblib import dump 

# Load dataset
df = pd.read_csv(r'Datasets\realistic_food_adulteration_samples.csv')

# Define features and label
features = ['food_type', 'adulterant', 'adulteration_level']
label = 'is_adulterated'

X = df[features]
y = df[label].astype(int)  # Convert True/False to 1/0


# Preprocessing steps
categorical_features = ['food_type', 'adulterant']
numeric_features = ['adulteration_level']

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
    ('num', StandardScaler(), numeric_features)
])

# Create pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(solver='liblinear'))  # good for small data
])

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Predict and evaluate
y_pred = pipeline.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# # Function to take user input and predict
# def predict_user_sample(pipeline):
#     print("\nEnter the details of the food sample for prediction:")

#     food_type = input("Food Type (Milk/Wheat/Honey/Chili Powder/Turmeric): ")
#     adulterant = input("Adulterant (Water/Detergent/Starch/Urea/Soapstone/Chalk Powder/Sugar Syrup/Jaggery Syrup/Brick Powder/Salt Powder/Metanil Yellow/None): ")
#     adulteration_level = float(input("Adulteration Level (e.g., 0.5, 3.2): "))

#     # Create a dataframe for the input
#     user_input = pd.DataFrame([{
#         'food_type': food_type,
#         'adulterant': adulterant,
#         'adulteration_level': adulteration_level
#     }])

#     # Predict
#     prediction = pipeline.predict(user_input)[0]

#     if prediction == 1:
#         print("\n🚨 The sample is predicted to be ADULTERATED.")
#     else:
#         print("\n✅ The sample is predicted to be CLEAN.")

# # Example usage
# predict_user_sample(pipeline)

dump(pipeline, 'adulterationPrediction-model.joblib')
