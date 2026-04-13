
import streamlit as st
import pandas as pd
from duckduckgo_search import DDGS

st.set_page_config(page_title="Engine Expert", layout="wide")

st.title("🏎️ نظام خبير الحساسات")

def start_search(q):
    try:
        with DDGS() as ddgs:
            return [r for r in ddgs.text(f"{q} engine sensors voltage", max_results=3)]
    except:
        return []

brand = st.sidebar.selectbox("الماركة", ["Audi", "BMW", "Mercedes"])
code = st.text_input("كود المحرك")

if st.button("بحث"):
    if code:
        with st.spinner("جاري البحث..."):
            res = start_search(f"{brand} {code}")
            if res:
                for item in res:
                    st.write(f"### {item['title']}")
                    st.write(item['body'])
            else:
                st.error("لا توجدنتائج")
