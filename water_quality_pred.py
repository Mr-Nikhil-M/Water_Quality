# this is main code:

import streamlit as st
import pickle
import numpy as np

# Set page configuration
st.set_page_config(page_title="Water Quality Prediction")

# Custom CSS styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content .block-container {
        margin-top: 10px;
    }
    .sidebar .sidebar-content .block-container a {
        color: #007bff;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# JavaScript to remove default text when typing starts
remove_default_text_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
  const inputElements = document.querySelectorAll('input[type="text"]');
  inputElements.forEach(function(input) {
    const defaultText = input.getAttribute('placeholder');
    input.addEventListener('input', function(event) {
      if (input.value === defaultText) {
        input.value = '';
      }
    });
    input.addEventListener('blur', function(event) {
      if (input.value === '') {
        input.value = defaultText;
      }
    });
  });
});
</script>
"""


def main():
    st.title("Water Quality Prediction")

    # Render JavaScript
    st.markdown(remove_default_text_js, unsafe_allow_html=True)

    # GitHub link emoji at the top right corner
    st.sidebar.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue?logo=GitHub)](https://github.com/your_username/your_repo)",
        unsafe_allow_html=True)

    # Google Colab link emoji below GitHub link
    st.sidebar.markdown(
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your_username/your_repo)",
        unsafe_allow_html=True)

    # Input fields for various features
    with st.form(key='water_quality_prediction_form'):
        st.header('Input Features')
        st.write('Enter the values for each feature:')
        aluminium = st.text_input("Aluminium", "Type here", key="aluminium")
        ammonia = st.slider("Ammonia", min_value=0.0, max_value=3000.0, value=50.0)
        arsenic = st.text_input("Arsenic", "Type here", key="arsenic")
        barium = st.text_input("Barium", "Type here", key="barium")
        cadmium = st.text_input("Cadmium", "Type here", key="cadmium")
        chloramine = st.text_input("Chloramine", "Type here", key="chloramine")
        chromium = st.text_input("Chromium", "Type here", key="chromium")
        copper = st.text_input("Copper", "Type here", key="copper")
        flouride = st.text_input("Flouride", "Type here", key="flouride")
        bacteria = st.slider("Bacteria", min_value=0.0, max_value=10.0, value=0.6)
        viruses = st.text_input("Viruses", "Type here", key="viruses")
        lead = st.text_input("Lead", "Type here", key="lead")
        nitrates = st.slider("Nitrates", min_value=0.0, max_value=30.0, value=0.0)
        nitrites = st.text_input("Nitrites", "Type here", key="nitrites")
        mercury = st.text_input("Mercury", "Type here", key="mercury")
        perchlorate = st.number_input("Perchlorate", min_value=0.0, max_value=100.0, value=32.0)
        radium = st.text_input("Radium", "Type here", key="radium")
        selenium = st.text_input("Selenium", "Type here", key="selenium")
        silver = st.text_input("Silver", "Type here", key="silver")
        uranium = st.text_input("Uranium", "Type here", key="uranium")

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        # Convert input values to float and store in a list
        features = []
        for value in [aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper, flouride, bacteria,
                      viruses, lead, nitrates, nitrites, mercury, perchlorate, radium, selenium, silver, uranium]:
            if value and value != "Type here":
                features.append(float(value))
            else:
                features.append(None)

        # Load the trained model and scaler
        model = pickle.load(open('water.sav', 'rb'))
        scaler = pickle.load(open('scalerwater.sav', 'rb'))

        # Scale the input features
        scaled_features = scaler.transform([features])
        # Make prediction
        prediction = model.predict(scaled_features)

        # Display prediction result
        st.header('Prediction')
        if prediction == 0:
            st.write("The water is predicted to be: Safe to drink 🚰")
        else:
            st.write("The water is predicted to be: Not safe to drink ❌")


if __name__ == "__main__":
    main()


# import streamlit as st
# import pickle
# import numpy as np
#
# # Set page configuration
# st.set_page_config(page_title="Water Quality Prediction")
#
# # Custom CSS styling
# st.markdown("""
#     <style>
#     /* Add your CSS styles here */
#     .sidebar .sidebar-content {
#         background-color: #f0f2f6;
#     }
#     .sidebar .sidebar-content .block-container {
#         margin-top: 10px;
#     }
#     .sidebar .sidebar-content .block-container a {
#         color: #007bff;
#         text-decoration: none;
#     }
#     </style>
# """, unsafe_allow_html=True)
#
# def main():
#     st.title("Water Quality Prediction")
#
#     # GitHub link emoji at the top right corner
#     st.sidebar.markdown(
#         "[![GitHub](https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue?logo=GitHub)](https://github.com/your_username/your_repo)",
#         unsafe_allow_html=True)
#
#     # Google Colab link emoji below GitHub link
#     st.sidebar.markdown(
#         "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your_username/your_repo)",
#         unsafe_allow_html=True)
#
#     # Input fields for various features
#     with st.form(key='water_quality_prediction_form'):
#         st.header('Input Features')
#         st.write('Enter the values for each feature:')
#         aluminium = st.text_input("Aluminium", "Type here", key="aluminium")
#         ammonia = st.slider("Ammonia", min_value=0.0, max_value=3000.0, value=50.0)
#         arsenic = st.text_input("Arsenic", "Type here", key="arsenic")
#         barium = st.text_input("Barium", "Type here", key="barium")
#         cadmium = st.text_input("Cadmium", "Type here", key="cadmium")
#         chloramine = st.text_input("Chloramine", "Type here", key="chloramine")
#         chromium = st.text_input("Chromium", "Type here", key="chromium")
#         copper = st.text_input("Copper", "Type here", key="copper")
#         flouride = st.text_input("Flouride", "Type here", key="flouride")
#         bacteria = st.slider("Bacteria", min_value=0.0, max_value=10.0, value=0.6)
#         viruses = st.text_input("Viruses", "Type here", key="viruses")
#         lead = st.text_input("Lead", "Type here", key="lead")
#         nitrates = st.slider("Nitrates", min_value=0.0, max_value=30.0, value=0.0)
#         nitrites = st.text_input("Nitrites", "Type here", key="nitrites")
#         mercury = st.text_input("Mercury", "Type here", key="mercury")
#         perchlorate = st.number_input("Perchlorate", min_value=0.0, max_value=100.0, value=32.0)
#         radium = st.text_input("Radium", "Type here", key="radium")
#         selenium = st.text_input("Selenium", "Type here", key="selenium")
#         silver = st.text_input("Silver", "Type here", key="silver")
#         uranium = st.text_input("Uranium", "Type here", key="uranium")
#
#         # Clear default text when user interacts with input
#         form_state = st.form_submit_button(label='Predict')
#         if form_state:
#             for key in form_state:
#                 if key != 'triggered':
#                     st.session_state[key] = form_state[key]
#
#     # Retrieve values from session state
#     input_values = {}
#     for key in st.session_state:
#         if key != 'water_quality_prediction_form':
#             input_values[key] = st.session_state[key]
#
#     if input_values:
#         # Convert input values to float and store in a list
#         features = []
#         for value in input_values.values():
#             if value and value != "Type here":
#                 features.append(float(value))
#             else:
#                 features.append(None)
#
#         # Load the trained model and scaler
#         model = pickle.load(open('water.sav', 'rb'))
#         scaler = pickle.load(open('scalerwater.sav', 'rb'))
#
#         # Scale the input features
#         scaled_features = scaler.transform([features])
#         # Make prediction
#         prediction = model.predict(scaled_features)
#
#         # Display prediction result
#         st.header('Prediction')
#         if prediction == 0:
#             st.write("The water is predicted to be: Safe to drink 🚰")
#         else:
#             st.write("The water is predicted to be: Not safe to drink ❌")
#
#
# if __name__ == "__main__":
#     main()


