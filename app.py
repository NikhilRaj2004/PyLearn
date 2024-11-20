import streamlit as st

st.title("2205A21032")

def output(vth, rth, rl):
    il = vth / (rth + rl)
    pl = il * il * rl
    return il, pl

col1, col2 = st.columns(2)

with col1:
    vth = st.number_input("Vth (V)", value=10)
    rth = st.number_input("Rth (Ohms)", value=100)
    rl = st.number_input("Rl (Ohms)", value=100)
    compute = st.button("Compute")

with col2:
    if compute:
        il, pl = output(vth, rth, rl)
        st.write(f"Load Current = {il:.2f} A")
        st.write(f"Load Power = {pl:.2f} Watts")

