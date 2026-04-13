import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Technical Sensor Expert", layout="wide")

st.title("🛠️ محلل قيم الحساسات (Technical Data Only)")

def professional_search(brand, code):
    # استخدام كلمات مفتاحية هندسية واستهداف مواقع المحترفين فقط
    tech_queries = [
        f"site:ross-tech.com {code} sensor measuring blocks",
        f"site:bimmerpost.com {code} sensor voltage resistance values",
        f"site:mbworld.org {code} sensor specification data",
        f"{brand} {code} 'nominal value' sensor voltage"
    ]
    
    all_results = []
    try:
        with DDGS() as ddgs:
            for q in tech_queries:
                results = list(ddgs.text(q, max_results=2))
                all_results.extend(results)
        return all_results
    except:
        return []

brand = st.sidebar.selectbox("الماركة", ["Audi", "BMW", "Mercedes", "VW"])
code = st.text_input("أدخل كود المحرك (مثل: 3.0 TFSI أو N55):")

if st.button("استخراج القيم الفنية"):
    if code:
        with st.spinner("جاري تنقيب البيانات من منتديات المهندسين وكتيبات الصيانة..."):
            res = professional_search(brand, code)
            
            if res:
                st.success(f"تم العثور على {len(res)} مصادر تقنية متخصصة")
                for item in res:
                    # تصميم البطاقة لتبدو تقنية أكثر
                    with st.container():
                        st.markdown(f"### 📄 {item['title']}")
                        st.info(item['body'])
                        st.caption(f"المصدر الفني: {item['href']}")
                        st.divider()
            else:
                st.warning("لم نجد بيانات دقيقة في المصادر المتخصصة. تأكد من كود المحرك.")
