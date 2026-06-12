import streamlit as st
from legalassistant.crew import LegalAssistant

st.set_page_config(
    page_title="AI Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Personal AI Legal Assistant")

st.markdown("""
Enter a legal problem in plain English.

This assistant will:
- Understand the legal issue
- Find applicable IPC sections
- Retrieve matching precedent cases
- Generate a formal legal document
""")

user_input = st.text_area(
    "📝 Describe your legal issue",
    height=250
)

if st.button("🔍 Analyze Case"):

    if not user_input.strip():
        st.warning("Please enter a legal issue.")
        st.stop()

    with st.spinner("🔎 Analyzing your case and preparing legal output..."):

        result = LegalAssistant().crew().kickoff(
            inputs={
                "user_input": user_input
            }
        )

    st.success("✅ Legal Assistant completed the workflow!")

    # Extract task outputs
    try:
        case_summary = result.tasks_output[0].raw
        ipc_sections = result.tasks_output[1].raw
        precedents = result.tasks_output[2].raw
        legal_document = result.tasks_output[3].raw

        tab1, tab2, tab3, tab4 = st.tabs([
            "📋 Case Summary",
            "⚖️ IPC Sections",
            "📚 Precedents",
            "📄 Legal Draft"
        ])

        with tab1:
            st.code(case_summary)

        with tab2:
            st.code(ipc_sections)

        with tab3:
            st.write(precedents)

        with tab4:
            st.markdown(legal_document)

    except Exception:
        # Fallback
        if hasattr(result, "raw"):
            st.subheader("📄 Final Legal Document")
            st.markdown(result.raw)
        else:
            st.write(result)