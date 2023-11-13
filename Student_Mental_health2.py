import streamlit as st
import numpy as np
import pickle
import sklearn

model = pickle.load(open("Student_Mental_Health_System.pkl", "rb"))

cources = ['Engineering', 'Islamic education', 'BIT', 'Laws', 'Mathematics',
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
codes = [17, 25, 4, 33, 37, 41, 2, 20, 23, 42, 26, 1, 14, 36, 28, 5, 9,
         32, 27, 45, 44, 16, 0, 7, 47, 29, 3, 6, 22, 10, 46, 15, 34, 35,
         31, 21, 8, 11, 13, 40, 43, 48, 19, 12, 30, 18, 24, 38, 39]

def health_pred(Course, Marital_status, Depression, Anxiety, PanicAttack):
    if Course in cources:
        index = cources.index(Course)
        Course = codes[index]

    Marital_status = 1 if Marital_status == "Commited or InRelationship" else 0
    Depression = 1 if Depression == "Yes" else 0
    Anxiety = 1 if Anxiety == "Yes" else 0
    PanicAttack = 1 if PanicAttack == "Yes" else 0

    prediction = model.predict([[Course, Marital_status, Depression, Anxiety, PanicAttack]])

    if prediction == 0:
        return st.markdown('<h1 class="title">Hurray!! Your Mental Health is Normal</h1><br>', unsafe_allow_html=True)
    else:
        return st.markdown('<h1 class="title">Dear Student, You May Need Treatment</h1><br>', unsafe_allow_html=True)

def main():
   st.markdown('<h1 class="title">Student Mental Health Predicto</h1><br>', unsafe_allow_html=True)
   

    # Set background image
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://health.clevelandclinic.org/wp-content/uploads/sites/3/2023/08/college-Students-mental-health1-1397488501-770x533-1.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
   st.markdown(
    """
    <style>
    /* CSS for title */
    .title {
        font-size: 36px;
        color: white; /* Black font color */
        text-align: center;
        background-color: black; /* White background color */
        padding: 10px; /* Add padding for spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Place input controls in the sidebar
    with st.sidebar:
        st.image("https://metro.co.uk/wp-content/uploads/2017/10/menal-health-at-uni.png?quality=90&strip=all&zoom=1&resize=768%2C576", width=300)
        Course = st.selectbox("Select your course", cources)
        Marital_status = st.selectbox("Marital status", ["Single", "Commited or InRelationship"])
        Depression = st.selectbox("Do you have Depression?", ["No", "Yes"])
        Anxiety = st.selectbox("Do you have Anxiety?", ["No", "Yes"])
        PanicAttack = st.selectbox("Do you have Panic attack?", ["No", "Yes"])

    diagnosis = ''
    if st.button("Predict My Mental Health"):
        diagnosis = health_pred(Course, Marital_status, Depression, Anxiety, PanicAttack)

    st.success(diagnosis)

if __name__ == '__main__':
    main()

