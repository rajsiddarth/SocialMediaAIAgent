import json
import streamlit as st
from openai import OpenAI

from helper import get_openai_api_key


st.set_page_config(page_title="Social Media AI Agent", page_icon="🤖")
st.title("🤖 Social Media Customer Agent")
st.caption("Analyze a social post and draft a support-style reply.")


def build_client() -> OpenAI:
    api_key = get_openai_api_key()
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set. Add it to your environment or .env file.")
    return OpenAI(api_key=api_key)


def process_mention(client: OpenAI, mention: str, company: str, product: str) -> dict:
    prompt = f"""
You are a social media support assistant for {company}.
Analyze this post and return JSON with exactly these keys:
- sentiment: one of [positive, neutral, negative]
- needs_response: boolean
- response: concise and empathetic public response (max 60 words)
- support_ticket_description: either null or a short sentence if escalation is needed
- rationale: 1 short sentence on why this response was chosen

Product: {product}
Post: {mention}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    raw = response.output_text.strip()

    # Fallback for models that wrap JSON with markdown fences.
    cleaned = raw.replace("```json", "").replace("```", "").strip()
    result = json.loads(cleaned)

    required_keys = {
        "sentiment",
        "needs_response",
        "response",
        "support_ticket_description",
        "rationale",
    }
    missing = required_keys - set(result.keys())
    if missing:
        raise ValueError(f"Model response is missing keys: {', '.join(sorted(missing))}")

    return result


company = st.text_input("Company name", value="Acme")
product = st.text_input("Product", value="Acme AI")
mention = st.text_area(
    "Social media post",
    placeholder="Example: I love the new Acme AI update, but it keeps crashing when I upload videos.",
    height=140,
)

if st.button("Generate response", type="primary", disabled=not mention.strip()):
    try:
        with st.spinner("Analyzing post..."):
            client = build_client()
            result = process_mention(client, mention, company, product)

        st.subheader("Analysis")
        st.write(f"**Sentiment:** {result['sentiment']}")
        st.write(f"**Needs response:** {result['needs_response']}")
        st.write(f"**Rationale:** {result['rationale']}")

        st.subheader("Draft response")
        st.success(result["response"])

        if result["support_ticket_description"]:
            st.subheader("Support escalation")
            st.warning(result["support_ticket_description"])

    except json.JSONDecodeError:
        st.error("The model did not return valid JSON. Try again.")
    except Exception as exc:
        st.error(str(exc))

st.divider()
st.markdown(
    """
**Deploy quickly:**
1. Push this repo to GitHub.
2. Create a Streamlit Cloud app pointing to `app.py`.
3. Add `OPENAI_API_KEY` in app Secrets.
"""
)
