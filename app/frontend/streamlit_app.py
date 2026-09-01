import sys
from pathlib import Path

import streamlit as st


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from app.graph.rag_graph import rag_graph


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResolveAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        text-align: center;
        padding: 1.5rem 0 2rem 0;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: -2px;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        opacity: 0.65;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "question" not in st.session_state:
    st.session_state.question = ""

if "answer_data" not in st.session_state:
    st.session_state.answer_data = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 ResolveAI")

    st.caption("Enterprise Knowledge Assistant")

    st.divider()

    st.markdown("### About")

    st.write(
        "ResolveAI answers employee questions using "
        "retrieved company policy documents."
    )

    st.divider()

    st.markdown("### Architecture")

    st.markdown(
        """
        **Streamlit**  
        ↓  
        **LangGraph**  
        ↓  
        **Gemini Embeddings**  
        ↓  
        **Qdrant Cloud**  
        ↓  
        **Relevance Check**  
        ↓  
        **Gemini LLM**
        """
    )

    st.divider()

    st.success("Qdrant Cloud connected")


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">ResolveAI</div>
        <div class="hero-subtitle">
            Enterprise Knowledge Assistant
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# EXAMPLE QUESTIONS
# ============================================================

st.markdown("### 💡 Try an example")


example_questions = {
    "Travel expenses":
        "How long do I have to submit my travel expenses?",

    "Password policy":
        "What is the password policy?",

    "VPN troubleshooting":
        "How do I troubleshoot VPN access?",
}


col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "Travel expenses",
        use_container_width=True,
        key="travel_button",
    ):

        st.session_state.question = (
            example_questions["Travel expenses"]
        )

        st.session_state.answer_data = None

        st.rerun()


with col2:

    if st.button(
        "Password policy",
        use_container_width=True,
        key="password_button",
    ):

        st.session_state.question = (
            example_questions["Password policy"]
        )

        st.session_state.answer_data = None

        st.rerun()


with col3:

    if st.button(
        "VPN troubleshooting",
        use_container_width=True,
        key="vpn_button",
    ):

        st.session_state.question = (
            example_questions["VPN troubleshooting"]
        )

        st.session_state.answer_data = None

        st.rerun()


# ============================================================
# QUESTION
# ============================================================

st.markdown("### 💬 Ask ResolveAI")


question = st.text_area(
    "Question",
    key="question",
    placeholder="Ask a question about company policies...",
    height=120,
    label_visibility="collapsed",
)


# ============================================================
# ASK BUTTON
# ============================================================

if st.button(
    "Ask ResolveAI",
    type="primary",
    use_container_width=True,
    key="ask_button",
):

    # Clear previous answer
    st.session_state.answer_data = None

    if not question.strip():

        st.warning(
            "Please enter a question before asking."
        )

    else:

        with st.spinner(
            "Searching the company knowledge base..."
        ):

            try:

                result = rag_graph.invoke(
                    {
                        "question": question.strip(),
                        "results": [],
                        "answer": "",
                        "sources": [],
                    }
                )

                st.session_state.answer_data = {
                    "question": question.strip(),
                    "answer": result["answer"],
                    "sources": result["sources"],
                }

                st.rerun()

            except Exception as error:

                error_message = str(error)

                st.error(
                    "Unable to process your question."
                )

                if "RESOURCE_EXHAUSTED" in error_message:

                    st.warning(
                        "Gemini embedding quota has been reached. "
                        "Please wait and try again."
                    )

                else:

                    st.caption(
                        f"Error: {error_message}"
                    )


# ============================================================
# DISPLAY ANSWER
# ============================================================

if st.session_state.answer_data:

    data = st.session_state.answer_data


    # ========================================================
    # ANSWER
    # ========================================================

    st.markdown("### 🧠 Answer")

    with st.container(border=True):

        st.write(
            data["answer"]
        )


    # ========================================================
    # SOURCES
    # ========================================================

    if data.get("sources"):

        st.markdown("### 📚 Sources")


        for source in data["sources"]:

            document = source["document"]

            page = source["page"]

            score = source["score"]


            with st.container(border=True):

                st.markdown(
                    f"📄 **{document}**"
                )


                source_col1, source_col2 = st.columns(2)


                with source_col1:

                    st.caption(
                        f"Page {page}"
                    )


                with source_col2:

                    st.caption(
                        f"Relevance {score:.4f}"
                    )


    else:

        st.info(
            "No supporting sources were found "
            "for this answer."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "ResolveAI • AI-powered enterprise knowledge assistant"
)