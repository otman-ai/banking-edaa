import streamlit as st
import pandas as pd
import json
import pickle
from sklearn.preprocessing import LabelEncoder
st.set_page_config(page_title="Bank Client Data management",layout="wide")


@st.cache_resource
def load_model(model_path):
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
file_name = "model/model_file.p"
model = load_model(file_name)

with open("Dataset/uniques.json","r") as f:
   df = json.load(f)


st.sidebar.title("The Pages")

st.title("Bank client subscribed prediction")

st.markdown("<h6>The main idea of this page is to use the existent machine learning model to predict the shares of certains clients in a given features.<h6>",unsafe_allow_html=True)
st.markdown("<h6>Complete the following information to make prediction.</h6>",unsafe_allow_html=True)

input_title = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan',
       'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays',
       'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx',
       'cons.conf.idx', 'euribor3m', 'nr.employed']

input_title_col = ['job', 'marital', 'education', 'default', 'housing', 'loan',
                'poutcome','day_of_week','contact']

jobs = df["job"]
marital_type =df["marital"]

col1,col2,col3,col4  = st.columns((1,1,1,1))

def transform(value,values):
    encoder = LabelEncoder()
    data_encoder = encoder.fit_transform(values)
    val = encoder.transform([value])
    return val
col5,col6,col7,col8 = st.columns((1,1,1,1))
with col1:
    age = st.number_input("Age of the client",step=1)
with col2:
    job = st.selectbox("The job of the client",jobs)
    job = transform(job,jobs)[0]
with col3:
    marital = st.selectbox("The marital of the client",marital_type)
    marital = transform(marital,marital_type)[0]
    print(marital)
with col4:
    education = st.selectbox("Education type of the client",df["education"])
    education = transform(education,df["education"])[0]

with col5:
    month = st.select_slider("Month",range(1,13))
    month = transform(month,range(1,13))[0]

with col6:
    housing = st.selectbox("Housing Credit",df["housing"])
    housing = transform(housing,df["housing"])[0]

with col7:
    contact = st.selectbox("contact communication type",df["contact"])
    contact = transform(contact,df["contact"])[0]

with col8:
    poutcome = st.selectbox("Outcome of the previous marketing campaign",df["poutcome"])
    poutcome = transform(poutcome,df["poutcome"])[0]

col9,col10,col11,col12 = st.columns((1,1,1,1))

with col9:
    day_of_week = st.selectbox("last contact day of the week",df["day_of_week"])
    day_of_week = transform(day_of_week,df["day_of_week"])[0]

with col10:
    duration = st.number_input("last contact duration, in seconds",step=1)
with col11:
    campaign = st.number_input("Compaign",step=1)
with col12:
    pdays = st.number_input("Pdays",step=1)
col13,col14,col15,col16 = st.columns((1,1,1,1))

with col13:
    previous = st.number_input("Previous",step=1)
with col14:
    emp_var_rate = st.number_input("employment variation rate")
with col15:
    cons_price_idx = st.number_input("consumer price index")
with col16:
    cons_conf_idx = st.number_input("consumer confidence index")

col18,col17,col19 = st.columns((1,1,1))
with col17:
    euribor3m = st.number_input("euribor 3 month rate")
with col18:
    nr_employed = st.number_input("number of employees")
with col19:
    default = st.selectbox("Default",df["default"])
    default = transform(default,df["default"])[0]


loan = st.selectbox("Loan",df["loan"])
loan = transform(loan,df["loan"])[0]

if st.button("Predict The client type"):
    features = [age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,
                    pdays,previous,poutcome,emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed]
    predict = model.predict([features])
    classes = ["The client well not subscribe","The Client will subscribe"]
    print(predict)
    st.success(classes[predict[0]])
 