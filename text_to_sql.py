import streamlit as st
import pandas as pd
import psycopg2
from groq import Groq

# Database connection
def get_db_connection():
    return psycopg2.connect(
        host="aws-1-ap-south-1.pooler.supabase.com",
        port=5432,
        database="postgres",
        user="postgres.acgatuhehvvlkltmxoqi",
        password="VEDANTISGOD",
        sslmode="require",
        connect_timeout=10
    )

# Groq AI setup - REPLACE WITH YOUR ACTUAL KEY
client = Groq(api_key="")

st.title("📊 Text-to-SQL AI Analyst")
st.write("Ask questions about your wellness data in plain English!")

question = st.text_input("💬 Your question:", "Show me average mood by sleep quality")

if st.button("Run Query"):
    with st.spinner("Converting to SQL..."):
        prompt = f"""Convert this question to PostgreSQL SQL.

CRITICAL RULES:
1. Table name "mental_wellness_6" must be in double quotes
2. All column names must be in double quotes
3. Use these exact column names: "User_ID", "Date", "Mood_Score", "Sleep_Hours", "Sleep_Quality", "Screen_Time_Hours", "Physical_Activity_Min", "Social_Interaction_Hours", "Work_Productivity_Score", "Weather", "Diet_Quality", "Stress_Level"

Example: SELECT AVG("Mood_Score") FROM "mental_wellness_6" GROUP BY "Sleep_Quality"

Question: {question}

Return ONLY the SQL query. No markdown. No backticks."""
        
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        
        sql = completion.choices[0].message.content.strip()
        sql = sql.replace("```sql", "").replace("```", "").strip()
        
        st.code(sql, language="sql")
    
    with st.spinner("Running query..."):
        conn = get_db_connection()
        df = pd.read_sql(sql, conn)
        conn.close()
        
        st.success("Query executed!")
        st.dataframe(df)