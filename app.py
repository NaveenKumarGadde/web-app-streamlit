# Imports
import streamlit as st 
import pandas as pd
import seaborn as sns 

# Header 
st.title('Data Analysis')
st.subheader('Data Analysis using Python & Streamit')

# Upload data set 
upload = st.file_uploader('Upload your Dataset(In CSV format)')
if upload is not None:
    data = pd.read_csv(upload)
    
# Showing Data set 
if upload is not None:
    if st.checkbox('Preview Dataset'): 
        if st.button('Head'):
            st.write(data.head()) 
        if st.button('Tail'):
            st.write(data.tail())

# Checking data type of each column
if upload is not None:
    if st.checkbox('Data type of each column'):
        st.text('Data types')
        st.write(data.dtypes)
        
# Find shape of data set 
if upload is not None:
    data_shape = st.radio('What dimension do you want to Check?',('Rows','Columns'))
    
    if data_shape == 'Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])
    
    if data_shape == 'Columns':
        st.text('Number of Columns')
        st.write(data.shape[1])
        
# Finding the null values 
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox('Null values in the Data Set'):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success('Good News!!!, No Missing Values')

# Finding Duplicate Values in Data set
if upload is not None: 
    test = data.duplicated().any() 
    if test == True:
        st.warning('Data set contains some Duplicate vales')
        dup= st.selectbox('Do you want to Remove Duplicate values?',('Select One','Yes','No'))
        
        if dup == 'Yes':
            data = data.drop_duplicates()
            st.text('Duplicates values are Removed')
        if dup == 'No':
            st.text('Ok, No Problem')
            
# Get Overall statistics
if upload is not None: 
    if st.checkbox('Summary of a Dataset'):
        st.write(data.describe(include='all'))

if st.button('About App'):
    st.text(' Built with Streamit')
    st.text('Thanks to Streamit')

if st.checkbox('By'):
    st.success('Naveen Kumar Gadde')
            
        
        

    

    
        
    
        
    
