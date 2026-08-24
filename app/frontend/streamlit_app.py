import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/ask"
HEALTH_URL = "http://127.0.0.1:8000/health"


st.set_page_config(
    page_title="ResolveAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# Styling
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
        padding: 2rem 0 1.5rem 0;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -2px;
        margin-bottom: 0.3rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        opacity: 0.7;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Session State
# ============================================================

if "question" not in st.session_state:
    st.session_state.question = ""

if "answer_data" not in st.session_state:
    st.session_state.answer_data = None


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 ResolveAI")

    st.caption(
        "Enterprise Knowledge Assistant"
    )

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
        **FastAPI**  
        ↓  
        **LangGraph**  
        ↓  
        **Qdrant Vector Search**  
        ↓  
        **Relevance Check**  
        ↓  
        **Qwen LLM**
        """
    )

    st.divider()

    st.markdown("### API Status")

    try:

        health_response = requests.get(
            HEALTH_URL,
            timeout=5
        )

        if health_response.status_code == 200:
            st.success("Backend connected")
        else:
            st.error("Backend unavailable")

    except requests.exceptions.RequestException:

        st.error("Backend unavailable")


# ============================================================
# Hero
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
    unsafe_allow_html=True
)


st.divider()


# ============================================================
# Example Questions
# ============================================================

st.markdown("### 💡 Try an example")


example_questions = {
    "Travel expenses":
        "How long do I have to submit my travel expenses?",

    "Password policy":
        "What is the password policy?",

    "VPN troubleshooting":
        "How do I troubleshoot VPN access?"
}


col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "Travel expenses",
        use_container_width=True
    ):

        st.session_state.question = (
            example_questions["Travel expenses"]
        )

        st.session_state.answer_data = None


with col2:

    if st.button(
        "Password policy",
        use_container_width=True
    ):

        st.session_state.question = (
            example_questions["Password policy"]
        )

        st.session_state.answer_data = None


with col3:

    if st.button(
        "VPN troubleshooting",
        use_container_width=True
    ):

        st.session_state.question = (
            example_questions["VPN troubleshooting"]
        )

        st.session_state.answer_data = None


# ============================================================
# Question Input
# ============================================================

st.markdown("### 💬 Ask ResolveAI")


question = st.text_area(
    "Your question",
    key="question",
    placeholder="Ask a question about company policies...",
    height=120,
    label_visibility="collapsed"
)


ask_button = st.button(
    "Ask ResolveAI",
    type="primary",
    use_container_width=True
)


# ============================================================
# API Request
# ============================================================

if ask_button:

    if not question.strip():

        st.warning(
            "Please enter a question before asking."
        )

    else:

        with st.spinner(
            "Searching the company knowledge base..."
        ):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question.strip()
                    },
                    timeout=120
                )


                if response.status_code == 200:

                    st.session_state.answer_data = (
                        response.json()
                    )

                else:

                    try:

                        detail = response.json().get(
                            "detail",
                            "Unable to process the request."
                        )

                    except Exception:

                        detail = (
                            "Unable to process the request."
                        )

                    st.error(
                        f"API Error: {detail}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Unable to connect to the ResolveAI backend. "
                    "Please make sure FastAPI is running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request timed out. Please try again."
                )

            except Exception as error:

                st.error(
                    f"Unexpected error: {error}"
                )


# ============================================================
# Display Answer
# ============================================================

if st.session_state.answer_data:

    data = st.session_state.answer_data


    # --------------------------------------------------------
    # Answer
    # --------------------------------------------------------

    st.markdown("### 🧠 Answer")

    with st.container(border=True):

        st.write(
            data["answer"]
        )


    # --------------------------------------------------------
    # Sources
    # --------------------------------------------------------

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
# Footer
# ============================================================

st.divider()


st.caption(
    "ResolveAI • AI-powered enterprise knowledge assistant"
)