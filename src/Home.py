import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Bob | Compliance-Bot 🤑")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**","[ivan-pua/sxsw-hackathon](https://github.com/ivan-pua/sxsw-hackathon)")

    st.write("**Blog:** [ivanpua.com](https://ivanpua.com/)")

    st.write("**LinkedIn:** [Ivan Pua](https://www.linkedin.com/in/qieshang-pua/)")
    st.write("**Created by Ivan, huge credits to [Yvann](https://twitter.com/yvann_hub)**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Bob, Your Payroll Compliance Buddy 🤑</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>Meet Bob, your intelligent payroll compliance assistant. 
    Bob's mission is to ensure payroll compliance by comparing actual employee salary against 
    expected salary. Any discrepancies are cross-checked with the NSW Fairwork legislation. 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 What Are We Solving?")
st.write("""
- **Problem**: Large enterprises like 7-Eleven have been fined millions of dollars for underpaying their employees. Whether intentional or not, this has not only lead to massive fines, significant financial losses as a result of poor reputation, and low morale among employees.
- **How it works**: Bob, powered by Langchain, uses OpenAI's GPT-3 model to chat on tabular data (CSV). It extracts the most up-to-date legislation from Australian Fairwork website to check for compliance. The entire application is built using Streamlit.
- **Features**: 
    - Upload production (actual) and development (award engine configured) payroll data in CSV format
    - Ask questions about your payroll data, such as any differences between production and development
    - Check if your payroll data adheres to [Australian Fairwork Award legislation](https://www.fairwork.gov.au/)
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**Bob is under regular development. Feel free to contribute and help me make it even more better!**
""", unsafe_allow_html=True)





