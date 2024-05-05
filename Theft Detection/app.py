import pandas as pd
import streamlit as st

# Define function to check suspicious activity
def check_suspicious_activity(consumption_data):
    suspicious_flags = []
    for i, row in consumption_data.iterrows():
        # Rule 1: Check for abnormally low consumption
        if row.mean() < 100:  # Adjust threshold as needed
            suspicious_flags.append(1)
        else:
            # Rule 2: Check for sudden and large fluctuations
            if (row.diff().abs() > 500).any():  # Adjust threshold as needed
                suspicious_flags.append(1)
            else:
                suspicious_flags.append(0)
    
    return suspicious_flags

# Function to check suspicious activity based on user input
def predict_suspicious_activity(user_input):
    # Create a DataFrame with user input
    user_data = pd.DataFrame([user_input], columns=range(1, 27))  # Assuming 26 values
    
    # Check suspicious activity
    suspicious_flag = check_suspicious_activity(user_data)
    
    if 1 in suspicious_flag:
        return "Suspicious activity detected."
    else:
        return "No suspicious activity detected."

# Streamlit web app
def main():
    # st.image("logo.png",width=20,height=20, use_column_width=True)
    # st.title("Suspicious Activity Prediction")
    col1, col2 = st.columns([1, 5])

    with col1:
        st.image("logo.png", width=100)

    with col2:
        st.title("Suspicious Activity Prediction")

    st.write("Enter 26 consumption values:")

    # Create input boxes for user to enter values
    user_input = []
    for i in range(1, 27):
        user_input.append(st.number_input(f"Value {i}", value=0, step=1))

    # Predict suspicious activity
    if st.button("Predict"):
        result = predict_suspicious_activity(user_input)
        st.write(result)

if __name__ == "__main__":
    main()
