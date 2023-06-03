import streamlit as st
import pickle
import pandas as pd
import sklearn

model = pickle.load(open('model.pkl', 'rb'))

st.title("TITANIC SURVIVAL PRIDICTOR")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

pclass_values = [1,2,3]
sex_values = ['male', 'female']
embarked_values = ['Southampton', 'Cherbourg', 'Queenstown']

with col1:
    pclass = st.selectbox("Select Pessanger Class", pclass_values)
    age = st.number_input("Enter Age")
with col2:
    sex = st.selectbox("Enter Gender", sex_values)
    fare = st.number_input("Enter Fare")
with col3:
    embarked = st.selectbox("Select Embarked Place", embarked_values)
with col4:
    family_size = st.number_input("Enter Family Size")
   
if st.button("Predict"):
    if embarked == 'Southampton':
        embarked = 'S'
    elif embarked == 'Cherbourg':
            embarked = 'C'
    else:
            embarked = 'Q'

    input_data = [[pclass, sex, age, fare, embarked, family_size]]
    input_data = pd.DataFrame(input_data, columns=['pclass', 'sex', 'age','fare', 'embarked', 'familysize'])

    prdiction = model.predict(input_data)
    if prdiction == 0:
        prdiction = "Not Survived"
    else:
        prdiction = "Survived"

    st.subheader(prdiction)

    