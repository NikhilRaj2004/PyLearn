import streamlit as st
import numpy as np

def thevenin_equivalent(R1, R2, R3, V1, V2):
    # Calculate Thevenin's equivalent resistance
    Rth = R1 + R2 * R3 / (R2 + R3)

    # Calculate Thevenin's equivalent voltage
    Vth = V1 * R3 / (R2 + R3) + V2

    return Rth, Vth

def main():
    st.title("Thevenin's Theorem Calculator")

    # Input fields for circuit parameters
    R1 = st.number_input("Resistance R1 (Ohms)")
    R2 = st.number_input("Resistance R2 (Ohms)")
    R3 = st.number_input("Resistance R3 (Ohms)")
    V1 = st.number_input("Voltage V1 (Volts)")
    V2 = st.number_input("Voltage V2 (Volts)")

    # Calculate and display results
    if st.button("Calculate"):
        Rth, Vth = thevenin_equivalent(R1, R2, R3, V1, V2)
        st.write("Thevenin's Equivalent Resistance:", Rth, "Ohms")
        st.write("Thevenin's Equivalent Voltage:", Vth, "Volts")

if __name__== "__main__":
    main()