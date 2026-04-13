import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Engine Expert", layout="wide")

st.title("🏎️ نظام خبير الحساسات")

def start_search(q):
    try:
        # محاولة البحث بأكثر من طريقة
        with DDGS() as ddgs:
            # زيادة عدد النتائج وتوسيع نطاق البحث
            results = list(ddgs.text(f"{q} engine sensors technical specifications", max_results=5))
            return results
    except Exception as e:
        # عرض الخطأ في حال وجوده للمساعدة في التشخيص
        return [{"title": "خطأ تقني", "body": f"لم نتمكن من الاتصال بمحرك البحث: {str(e)}"}]

brand = st.sidebar.selectbox("الماركة", ["Audi", "BMW", "Mercedes", "VW"])
code = st.text_input("أدخل كود المحرك (مثال: EA888):")

if st.button("بدء البحث العميق"):
    if code:
        with st.spinner("جاري استخراج البيانات من المصادر العالمية..."):
            query = f"{brand} {code}"
            res = start_search(query)
            
            if res:
                st.success(f"تم العثور على معلومات لمحرك {code}")
                for item in res:
                    with st.expander(item.get('title', 'بدون عنوان')):
                        st.write(item.get('body', 'لا يوجد تفاصيل'))
                        st.caption(f"الرابط: {item.get('href', '#')}")
            else:
                st.warning("لم يتم العثور على نتائج. حاول كتابة كود المحرك بشكل أبسط (مثلاً N55 بدلاً من BMW N55).")
    else:
        st.error("يرجى إدخال كود المحرك")
