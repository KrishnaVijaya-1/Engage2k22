import streamlit as st 
import pickle 
import numpy as np 
import pandas as pd 

df = pd.read_csv("Data1.csv") 
pipe = pickle.load(open("pipe.pkl", "rb")) 
st.title("Pokemon Legendary Predictor") 

pokemon = df['Name'].unique() 
 

pokemonname = st.selectbox('Name', df['Name'].unique()) 


     
Type1 = st.selectbox("Type1", df['Type 1'].unique()) 

Type2 = st.selectbox("Type2", df['Type 2'].unique())

Total= st.number_input("Total") 

Attack = st.number_input("Attack") 

 
Sp_Defense = st.number_input('Sp_Defense') 

Speed = st.number_input('Speed of pokemon')  

 
#Prediction 
if st.button('Predict Legendary'): 
     
     
    query = np.array([pokemonname,Type1,Type2,Total,Attack,Sp_Attack,Sp_Defense,Speed]) 
    query = query.reshape(1, 8) 
    prediction = str(int(np.exp(pipe.predict(query)[0])))
    if prediction == 0:
        st.title("The pokemon is not Legendary "+prediction)
    else:
        st.title("The pokemon is  Legendary"+prediction)
