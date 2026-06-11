# AI Text-to-SQL Analyst

Ask questions in plain English. AI generates SQL. Get answers instantly.


## Features
- Type any question about wellness data
- AI converts English to PostgreSQL SQL
- Runs on live database with 1,500+ records
- Returns results as a table instantly

## Tech Stack
- Streamlit - Web interface
- Groq API - LLM for SQL generation
- Supabase - PostgreSQL database
- Python - pandas, psycopg2

## Sample Questions
- "Show me average mood by sleep quality"
- "Which weather has the highest stress level?"
- "Average sleep hours by diet quality"
# 🔥 LIVE DEMO: [Click Here to Try the App](https://jwinyev3u8kksvhcxmiyb7.streamlit.app)
## Run Locally
```bash
pip install -r requirements.txt
streamlit run text_to_sql.py
