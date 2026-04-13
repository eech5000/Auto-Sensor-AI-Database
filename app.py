
import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Sensor Technical Engine", layout="wide")

st.title("🔬 مستخرج بيانات Bosch & Siemens المرجعية")
st.write("البحث في كتالوجات الشركات المصنعة للحساسات وقواعد بيانات OEM")

def deep_tech_search(brand, code):
    # استهداف شركات التصنيع والمواصفات الفنية الصارمة
    queries = [
        f"{brand} {code} sensor Bosch datasheet voltage",
        f"{brand} {code} Siemens VDO sensor resistance values",
        f"{brand} {code} MAF MAP sensor nominal values site:autocats.ws",
        f"{brand} {code} engine technical data sheet PDF",
        f"characteristic curve for {brand} {code} pressure sensor"
    ]
    
    results_list = []
    try:
        with DDGS() as ddgs:
            for q in queries:
                res = list(ddgs.text(q, max_results=2))
                results_list.extend(res)
        return results_list
    except:
        return []

brand = st.sidebar.selectbox("الماركة", ["Audi", "BMW", "Mercedes", "VW"])
engine = st.text_input("كود المحرك (مثل: EA837, N20, M271):")

if st.button("استخراج القيم المرجعية"):
    if engine:
        with st.spinner("جاري فحص فهارس Bosch و Siemens وقواعد البيانات الفنية..."):
            tech_data = deep_tech_search(brand, engine)
            
            if tech_data:
                st.success(f"تم العثور على {len(tech_data)} وثيقة تقنية")
                for data in tech_data:
                    with st.container():
                        st.markdown(f"#### 🛠️ {data['title']}")
                        # تسليط الضوء على الأرقام داخل النص
                        st.info(data['body'])
                        st.caption(f"المصدر: {data['href']}")
                        st.divider()
            else:
                st.warning("لم نجد بيانات مباشرة. جرب إضافة 'MAF' أو 'O2' بجانب كود المحرك.")
    else:
        st.error("أدخل كود المحرك أولاً")
