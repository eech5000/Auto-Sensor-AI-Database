import streamlit as st
import pandas as pd
import json
import os

# --- وظائف إدارة قاعدة البيانات ---
DB_FILE = 'database.json'

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {"search_history": []}

def save_engine_data(engine_code, specs):
    data = load_data()
    # إضافة المحرك الجديد للذاكرة
    data["search_history"].append({"engine": engine_code, "specs": specs})
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- واجهة التطبيق الرئيسية ---
st.set_page_config(page_title="AI Automotive Expert", layout="wide")

st.title("🛡️ نظام الذاكرة التقنية للمحركات الألمانية")
st.sidebar.header("إدارة البيانات")

if st.sidebar.button("عرض المحركات المحفوظة"):
    history = load_data()
    st.sidebar.write(f"عدد المحركات في الذاكرة: {len(history['search_history'])}")

# ... (بقية كود الواجهة السابق مع تعديل بسيط في زر البحث)
engine_input = st.text_input("أدخل كود المحرك للتحليل:")

if st.button("تحليل وحفظ في القاعدة"):
    # محاكاة جلب بيانات (سنحولها لبحث حقيقي في الخطوة القادمة)
    mock_specs = [
        {"Sensor": "O2 Sensor", "Value": "0.1-0.9V", "Status": "Verified"},
        {"Sensor": "MAP Sensor", "Value": "1000 mbar", "Status": "Verified"}
    ]
    
    # حفظ البيانات في الذاكرة
    save_engine_data(engine_input, mock_specs)
    st.success(f"تم تحليل محرك {engine_input} وحفظ بياناته في قاعدة البيانات بنجاح!")
    st.table(pd.DataFrame(mock_specs))
