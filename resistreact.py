import streamlit as st
import math

def Tran_Eff(VSC, ISC, WSC):
    ZSC = VSC / ISC
    R1 = WSC / (ISC ** 2)
    X1 = math.sqrt(ZSC ** 2 - R1 ** 2)
    return R1, X1

st.title("02341A0259-PS8")
st.header("Transformer Winding Resistance and Reactance Calculator")

VSC = st.number_input("Enter VSC (in Volts):", min_value=0.0, step=1.0)
ISC = st.number_input("Enter ISC (in Amps):", min_value=0.0, step=1.0)
WSC = st.number_input("Enter WSC (in Watts):", min_value=0.0, step=1.0)

if st.button("Compute"):
    if ISC > 0:
        R1, X1 = Tran_Eff(VSC, ISC, WSC)
        st.write(f"Winding Resistance (R1): {R1:.4f} Ohms")
        st.write(f"Reactance (X1): {X1:.4f} Ohms")
    else:
        st.error("ISC must be greater than 0.")