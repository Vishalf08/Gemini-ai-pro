from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
genai.configure(api_key=os.getenv("Google_API"))

def get_gemini_response(question,prompt):
      model=genai.GenerativeModel('gemini-pro')
      response=model.generate_content([prompt[0],question])
      return response.text


def read_sql_query(sql,db):
      conn=sqlite3.connect(db)
      cur=conn.cursor()
      cur.execute(sql)
      rows=cur.fetchall()
      conn.commit()
      conn.close()
      for row in rows:
            print(row)
      return rows
st.set_page_config(page_title="I can retriew any sql query")
st.header(':blue[Find the information from employee table] :sunglasses:')
question=st.text_input("input: ",key="",placeholder='Hello, How can i help you !')

submit=st.button("Submit your questions")
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name Emp and has the following columns - Emp_id,Name,Department,Salary, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM Emp ;
    \nExample 2 - Tell me all the students studying in Data Analyst Department?, 
    the SQL command will be something like this SELECT * FROM Emp
    where Departemnt="Data Analyst"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """]
import streamlit as st
# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1554234362-59a913f24b78?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTR8fGtpdGV8ZW58MHx8MHx8fDA%3D");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

if submit:
      response=get_gemini_response(question,prompt)
      print(response)
      data=read_sql_query(response,"Emp.db")
      st.subheader(':blue[Result]')
      
      for row in data:
            print(row)
            st.header(row)

