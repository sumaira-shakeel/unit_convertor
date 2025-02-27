
# project:01:unit_converter.py
# Build a Google Unit Converter using Python and Streamlit

import streamlit as st

# Apply custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: rgb(31, 66, 137);
        color: white;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: teal;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1> 🔄 Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("✔️ Easily convert units of length, weight, and temperature ✔️")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

# Dropdown for units
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_unit = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return (value / length_unit[from_unit]) * length_unit[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_unit = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return (value / weight_unit[from_unit]) * weight_unit[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Convert button
if st.button("🔄 Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    
    st.markdown(
        f"<div class='result-box'>✔️ {value} {from_unit} = <b>{result:.4f}</b> {to_unit} ✔️</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown("<div class='footer'>Created by Sumaira Shakeel ❤️</div>", unsafe_allow_html=True)

