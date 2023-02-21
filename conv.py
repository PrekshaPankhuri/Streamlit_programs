import streamlit as st
from PIL import Image

# Define the conversion factors
length_units = {
    "millimeters (mm)": 0.001,
    "centimeters (cm)": 0.01,
    "meters (m)": 1.0,
    "kilometers (km)": 1000.0,
}

weight_units = {
    "grams (g)": 0.001,
    "kilograms (kg)": 1.0,
}

volume_units = {
    "milliliters (ml)": 0.001,
    "liters (l)": 1.0,
    "kiloliters (kl)": 1000.0,
}

# Set the app title

# Set the app title with an icon
page_title = 'Unit Converter'
layout = 'centered'
page_icon = '⚖'
icon = Image.open("icon_i.png")
st.set_page_config(page_title= page_title, page_icon=icon, layout=layout)
st.title(page_title+" "+page_icon)

# Get the user input values
input_value = st.number_input("Enter a value:")
input_unit = st.selectbox("Select the input unit:", list(length_units.keys()) + list(weight_units.keys()) + list(volume_units.keys()))
output_unit = st.selectbox("Select the output unit:", list(length_units.keys()) + list(weight_units.keys()) + list(volume_units.keys()))

# Convert the input value to standard units
if input_unit in length_units:
    input_standard_value = input_value / length_units[input_unit]
elif input_unit in weight_units:
    input_standard_value = input_value / weight_units[input_unit]
else:
    input_standard_value = input_value / volume_units[input_unit]

# Convert the standard units to the output unit
if output_unit in length_units:
    output_standard_value = input_standard_value * length_units[output_unit]
elif output_unit in weight_units:
    output_standard_value = input_standard_value * weight_units[output_unit]
else:
    output_standard_value = input_standard_value * volume_units[output_unit]

# Display the output
st.write(f"{input_value} {input_unit} is equal to {output_standard_value:.2f} {output_unit}")
