import streamlit as st
import pandas as pd
import time
from duckduckgo_search import DDGS

# إعداد الصفحة
st.set_page_config(page_title="AI Engine Expert", layout="wide")

# دالة البحث
def run_search(query):
    try:
        with DDGS() as ddgs:
            results =
            return results
    except Exception as e:
        return f"Error: {e}"

# واجهة المستخدم
st.title("🏎️ نظام خبير الحساسات المتكامل")
st.write("البحث الحي في المصادر التقنية لسيارات VAG, BMW, Mercedes")

with st.sidebar:
    st.header("لوحة التحكم")
    brand = st.selectbox("الماركة:", ["Audi", "BMW", "Mercedes", "VW"])
    st.info("النظام يبحث الآن في المصادر العالمية المفتوحة.")

engine_code = st.text_input("أدخل كود المحرك (مثلاً: EA888 أو N55):")

if st.button("بدء البحث المباشر"):
    if engine_code:
        with st.spinner('جاري الاتصال بمحركات البحث العالمية...'):
            search_query = f"{brand} {engine_code}"
            results = run_search(search_query)
            
            if isinstance(results, list) and len(results) > 0:
                st.success(f"تم العثور على {len(results)} مصادر فنية!")
                for res in results:
                    with st.expander(res['title']):
                        st.write(res['body'])
                        st.caption(f"الرابط: {res['href']}")
            else:
                st.error("لم نتمكن من جلب بيانات حالياً، تأكد من اتصال الإنترنت أو حاول لاحقاً.")
    else:
        st.warning("يرجى إدخال كود المحرك أولاً.")
