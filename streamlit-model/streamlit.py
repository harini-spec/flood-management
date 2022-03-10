import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model_reg.pkl','rb'))
model1 = pickle.load(open('model_reg_jan.pkl','rb'))
model2 = pickle.load(open('model_reg_feb.pkl','rb'))
model3 = pickle.load(open('model_reg_mar.pkl','rb'))
model4 = pickle.load(open('model_reg_apr.pkl','rb'))
model5 = pickle.load(open('model_reg_may.pkl','rb'))

model6 = pickle.load(open('model_reg_jun.pkl','rb'))
model7 = pickle.load(open('model_reg_jul.pkl','rb'))
model8 = pickle.load(open('model_reg_aug.pkl','rb'))
model9 = pickle.load(open('model_reg_sept.pkl','rb'))
model10 = pickle.load(open('model_reg_oct.pkl','rb'))

model11 = pickle.load(open('model_reg_nov.pkl','rb'))
model12 = pickle.load(open('model_reg_dec.pkl','rb'))

st.title("Flood prediction")
st.markdown("Here we are using annual rainfall as a parameter to predict flood")
# ip=ip.replace(".","[.]")

def main():
    st.subheader("Enter the annual rainfall")
    annual = st.text_input('', 0,100)

    st.subheader("Flood prediction")

    res = model.predict([[annual]])
    st.code(res[0])

    st.title("Predict month-wise")

    option = st.selectbox(
        'Select a month',
        ("None","January","February","March","April","May","June","July","August","September","October","November","December"))

    if(option=="January"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model1.predict([[number]])
        st.code(res[0])

    if(option=="February"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model2.predict([[number]])
        st.code(res[0])

    if(option=="March"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model3.predict([[number]])
        st.code(res[0])

    if(option=="April"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model4.predict([[number]])
        st.code(res[0])

    if(option=="May"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model5.predict([[number]])
        st.code(res[0])

    if(option=="June"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model6.predict([[number]])
        st.code(res[0])

    if(option=="July"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model7.predict([[number]])
        st.code(res[0])
    
    if(option=="August"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model8.predict([[number]])
        st.code(res[0])

    if(option=="September"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model9.predict([[number]])
        st.code(res[0])

    if(option=="October"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model10.predict([[number]])
        st.code(res[0])

    if(option=="November"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model11.predict([[number]])
        st.code(res[0])

    if(option=="December"):
        # jan = st.text_input('', 0,100)
        number = st.number_input("Enter average rainfall", 0, 5000, 0, 100)
        res = model12.predict([[number]])
        st.code(res[0])

if __name__ == "__main__":
    main()