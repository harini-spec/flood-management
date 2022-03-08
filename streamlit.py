import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model_reg.pkl','rb'))

st.title("Flood prediction")
st.markdown("Here we are using annual rainfall as a parameter to predict flood")

def main():
    st.subheader("Enter the annual rainfall")
    annual = st.text_input('', 0,100)

    st.subheader("Flood prediction")

    res = model.predict([[annual]])
    st.code(res[0])

if __name__ == "__main__":
    main()