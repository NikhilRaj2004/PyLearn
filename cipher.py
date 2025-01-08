import streamlit as st

def caesar_cipher(text, shift):
    alphabets = "abcdefghijklmnopqrstuvwxyz" * 2
    cipher = ""
    for char in text.lower():
        if char.isalpha():  # Only process alphabetic characters
            index = alphabets.find(char)
            cipher += alphabets[index + shift]
        else:
            cipher += char  # Keep non-alphabetic characters as is
    return cipher.upper()

st.title("Caesar Cipher Encryption Tool")
st.header("Encrypt Text Using a Caesar Cipher")
st.subheader("Provide a text and a shift value to generate an encrypted version of the text.")

# Input fields for text and shift
text = st.text_input("Enter the text to encrypt:")
shift = st.number_input("Enter the shift value:", min_value=0, step=1)

if st.button("Encrypt"):
    if text:
        encrypted_text = caesar_cipher(text, shift)
        st.write(f"Encrypted Text: {encrypted_text}")
    else:
        st.error("Please enter some text to encrypt.")
