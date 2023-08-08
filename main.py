import pandas as pd
import json
import os
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
#import pymongo
from PIL import Image
#from pymongo.mongo_client import MongoClient
#from pymongo.server_api import ServerApi
#from googleapiclient.discovery import build
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="phonepepulse"

)

print(mydb)
mycursor = mydb.cursor(buffered=True)
#with st.sidebar:

select = option_menu(None, ["Home","About","Basic insights"],
                           icons=["bar-chart","house","toggles"],
                           default_index=0,
                           orientation="horizontal",
                           styles={"container": {"padding":"0!important","background-color":"white","size":"cover","width":"100%"},
                                   "icon":{"color":"black","font-size":"20px"},
                                   "nav-link":{"font-size":"20px","text-align":"center","margin":"0px","--hover-color":"#6F36AD"},
                                   "nav-link-selected": {"background-color":"#6F36AD"}})

with st.sidebar:

        st.image(Image.open(r"C:\Users\ravin\OneDrive\Desktop\PhonePe_Pulse.jpg"))
        st.image(Image.open(r"C:\Users\ravin\OneDrive\Desktop\ind.jpeg"))


if select=="Home":
    col1, col2 = st.columns(2, gap='large')

    col1.image(Image.open(r"C:\Users\ravin\OneDrive\Desktop\phoneimage.png"),width=300)
    with col1:
        st.write("PhonePe is an Indian digital payments and financial services company[8] headquartered in Bengaluru, Karnataka, India.[9][10] PhonePe was founded in December 2015,[3] by Sameer Nigam, Rahul Chari and Burzin Engineer.[11] The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016.[12]")
        st.download_button("down load the app now","https://www.phonepe.com/app-download/")
    with col2:
        st.video(r"C:\Users\ravin\OneDrive\Desktop\phonepevideo.mp4")

d=pd.read_csv(r"C:\Users\ravin\Downloads\Agg_Users.csv")
df=pd.DataFrame(d)
fig = px.choropleth(df, locations='State',scope='asia', color='State',hover_name='State',title='Live Geo Visulization Of India')
st.plotly_chart(fig)






if select=="About":
    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open(r"C:\Users\ravin\OneDrive\Desktop\phonepe-upi.jpg"))
        st.video(r"C:\Users\ravin\Downloads\Introducing PhonePe Pulse.mp4")
    with col2:
        st.image(Image.open(r"C:\Users\ravin\OneDrive\Desktop\phoneimage.png"))
        st.write(...)
        st.write("The Indian digital payments story has truly captured the world's imagination."
                     "From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data."
                     "When PhonePe started 5 years ago, we were constantly looking for definitive data sources on digital payments in India."
                     "Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top use cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?" \
                     "This year, as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why, and how of digital payments in India." \
                     "As we crossed 2000 Cr. transactions and 30 Crore registered users this year, we realized that, as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages, and grows its money. So it was time to demystify and share the what, why, and how of digital payments in India.")
    st.write(...)
    col1,col2=st.columns(2,gap='large')
    with col1:
        st.subheader("THE BEAT OF  PHONEPE")
        st.write("___")
        st.write("phonepe became a leading digital payment company")
        st.image(Image.open(r"C:\Users\ravin\OneDrive\Desktop\ppe.jpg"))
        with open(r"C:\Users\ravin\OneDrive\Desktop\Pulse_Report_2021_L_Cr.pdf","rb") as f:
            data=f.read()
        st.download_button("DOWNLOAD FILE",data,file_name="anual report.pdf")
    with col2:
        st.image(Image.open(r"C:\Users\ravin\OneDrive\Desktop\Phonepe-Pulse-Digital-0709_001.webp"))

if select=="Basic insights":
    st.write("### Select  to get Insights:")
    options= [
              "Top 10 states based on year and amount of transanction",
             "list 10 states based on type and amount of transanction",
              "Top 10 Tranmsanction Type based on states and district",
              "Top 10 RegisteredUsers based on states and district",
              "list of 10 districts based on states amount of transanction",
              "list of 10 tranasaction count based on districts and states",
              "Top 10 brands  based on states and Transaction count"]
    select=st.selectbox("select the options",options)
    if select=="Top 10 states based on year and amount of transanction":
        mycursor.execute("SELECT DISTINCT state, year, SUM(Transaction_amount) AS amount FROM agg_trans GROUP BY state, year ORDER BY year DESC;")
        df = pd.DataFrame(mycursor.fetchall(), columns=['state ','year','amount'])
        col1,col2=st.columns(2,gap='large')
        with col1:
            st.write(df)

            st.subheader(" Top 10 states based on year and amount of transanction")
        fig = px.bar(df,
                     x="year",
                     y='amount',
                     orientation='v',

                     )
        st.plotly_chart(fig, use_container_width=True)



if select=="list 10 states based on type and amount of transanction":
        mycursor.execute("SELECT DISTINCT state,SUM(Transaction_count) as total	 FROM top_trans GROUP BY state ORDER BY total ASC LIMIT 10 ;")
        df = pd.DataFrame(mycursor.fetchall(), columns=['state', 'total_Transanction'])
        col1,col2=st.columns(2,gap='large')
        with col1:
            st.write(df)
        with col2:
            st.subheader("10 states based on type and amount of transanction")


            fig = px.bar(df,
                         x="state",
                         y='total_Transanction',
                         orientation='v',
                         color='state'

                         )
            st.plotly_chart(fig, use_container_width=True)

if select=="Top 10 Tranmsanction Type based on states and district":
    mycursor.execute("SELECT district, SUM(amount) AS total_Transaction FROM map_trans GROUP BY state ORDER BY total_Transaction DESC LIMIT 10;")
    col1, col2 = st.columns(2, gap='large')

    df = pd.DataFrame(mycursor.fetchall(), columns=['district','total_Transanction'])
    with col1:
        st.write(df)
    with col2:
        st.subheader("Top 10 Tranmsanction Type based on states and district" )
        fig = px.bar(df,
                     x="district",
                     y='total_Transanction',
                     orientation='v',
                     color='district'

                     )
        st.plotly_chart(fig, use_container_width=True)
if select=="Top 10 RegisteredUsers based on states and district":


    mycursor.execute("SELECT state, SUM(registeredUsers) AS registeredUsers FROM top_users GROUP BY state ORDER BY registeredUsers DESC LIMIT 10;")

    df = pd.DataFrame(mycursor.fetchall(), columns=['state','registeredUsers'])
    col1,col2=st.columns(2,gap='large')
    with col1:
        st.write(df)
    with col2:
        st.subheader("Top 10 RegisteredUsers based on states and district")
        fig = px.bar(df,
                     x="state",
                     y='registeredUsers',
                     orientation='v',
                     color='state'

                     )
        st.plotly_chart(fig, use_container_width=True)

if select=="list of 10 districts based on states amount of transanction":



     mycursor.execute("SELECT district, SUM(Transaction_amount) AS Transaction_amount FROM top_trans GROUP BY district ORDER BY Transaction_amount DESC LIMIT 10;")
     df = pd.DataFrame(mycursor.fetchall(), columns=['district', 'Transaction_amount'])
     col1,col2=st.columns(2,gap='large')
     with col1:
        st.write(df)
     with col2:
         st.subheader("top 10 districts based on states amount of transanction ")
         fig = px.bar(df,
                      x="district",
                      y='Transaction_amount',
                      orientation='v',
                      color='district'

                      )
         st.plotly_chart(fig, use_container_width=True)

if select=="list of 10 tranasaction count based on districts and states":

    mycursor.execute("SELECT district, SUM(count) AS Transaction_count FROM map_trans GROUP BY district ORDER BY Transaction_count DESC LIMIT 10;")

    df = pd.DataFrame(mycursor.fetchall(), columns=['district', 'Transaction_count'])
    col1,col2=st.columns(2,gap='large')
    with col1:
        st.write(df)
    with col2:
        st.subheader("list of 10 tranasaction count based on districts and states")
        fig = px.bar(df,
                     x="district",
                     y='Transaction_count',
                     orientation='v',
                     color='district'

                     )
        st.plotly_chart(fig, use_container_width=True)

if select=="Top 10 brands  based on states and Transaction count":

    mycursor.execute("SELECT brand, SUM(count) AS Transaction_count FROM agg_users GROUP BY brand ORDER BY brand DESC LIMIT 10;")
    df = pd.DataFrame(mycursor.fetchall(), columns=['brand', 'Transaction_count'])
    col1,col2=st.columns(2,gap='large')
    with col1:
        st.write(df)
    with col2:
        st.subheader("Top 10 brands  based on states and Transaction count")
        fig = px.bar(df,
                     x="brand",
                     y='Transaction_count',
                     orientation='v',
                     color='brand'

                     )
        st.plotly_chart(fig, use_container_width=True)
















































