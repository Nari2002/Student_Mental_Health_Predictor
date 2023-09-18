import streamlit as st
import numpy as np
import pickle
import sklearn




model=pickle.load(open("Student_Mental_Health_System.pkl","rb"))

cources=['Engineering', 'Islamic education', 'BIT', 'Laws', 'Mathemathics',
   'Pendidikan islam', 'BCS', 'Human Resources', 'Irkhs',
   'Psychology', 'KENMS', 'Accounting ', 'ENM', 'Marine science',
   'KOE', 'Banking Studies', 'Business Administration', 'Law',
   'KIRKHS', 'Usuluddin ', 'TAASL', 'Engine', 'ALA',
   'Biomedical science', 'koe', 'Kirkhs', 'BENL', 'Benl', 'IT', 'CTS',
   'engin', 'Econs', 'MHSC', 'Malcom', 'Kop', 'Human Sciences ',
   'Biotechnology', 'Communication ', 'Diploma Nursing',
   'Pendidikan Islam ', 'Radiography', 'psychology', 'Fiqh fatwa ',
   'DIPLOMA TESL', 'Koe', 'Fiqh', 'Islamic Education', 'Nursing ',
   'Pendidikan Islam'] 
codes=[17, 25,  4, 33, 37, 41,  2, 20, 23, 42, 26,  1, 14, 36, 28,  5,  9,
           32, 27, 45, 44, 16,  0,  7, 47, 29,  3,  6, 22, 10, 46, 15, 34, 35,
           31, 21,  8, 11, 13, 40, 43, 48, 19, 12, 30, 18, 24, 38, 39]
#matchs
def health_pred(Cource,Marital_status,Depression,Anxiety,PanicAttack):
    if Cource in cources:
        index=cources.index(Cource)
        Cource=codes[index]
    
    if Marital_status=="Single":
        Marital_status=0
    else:
        Marital_status=1
    if Depression=="No":
        Depression=0
    else:
        Depression=1
    if Anxiety=="No":
        Anxiety=0
    else:
        Anxiety=1
    if PanicAttack=="No":
        PanicAttack=0
    else:
        PanicAttack=1
    prediction=model.predict([[Cource,Marital_status,Depression,Anxiety,PanicAttack]])   
    print(prediction)
    if (prediction==0):
        return "Hurray!! Your Mental Health is Normal"
    else:
        return "Dear Student You Need Treatment"

def main():
    st.title("Student Mental Health Predictor")
    st.image("https://metro.co.uk/wp-content/uploads/2017/10/menal-health-at-uni.png?quality=90&strip=all&zoom=1&resize=768%2C576",width=650)
    Cource=st.selectbox("cources",cources)
    code2=("No","Yes")
    code3=("Single","Commited or InRelationship")
    Marital_status=st.selectbox("Martial status",code3)
    Depression=st.selectbox("Do you have Depression",code2)
    Anxiety=st.selectbox("Do you have Anxiety?", code2)
    PanicAttack=st.selectbox("Do you have Panic attack?",code2)
    diagnosis=''
    if st.button("Predict My Mental Health"):
        
        diagnosis=health_pred(Cource,Marital_status,Depression,Anxiety,PanicAttack)
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
