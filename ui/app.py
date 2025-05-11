import streamlit as st
import requests
import json
import time

st.set_page_config(page_title="Sentiment & Intent Analyzer", layout="centered")

ANALYSIS_API_URL = "http://localhost:8000/predict"

st.title("📱 Sentiment & Intent Analysis App")
st.markdown("Analyze customer and sales representative conversations about iPhone in real-time.")

uploaded_file = st.file_uploader("📂 Upload conversation file (.json with 'sentences' list)", type="json")

def get_emotion_color(emotion):
    return {
        "positive": "#d4edda",   # green
        "negative": "#f8d7da",   # red
        "neutral":  "#f0f0f0"    # gray
    }.get(emotion, "white")

if uploaded_file is not None:
    try:
        conversation_data = json.load(uploaded_file)
        sentences = conversation_data.get("sentences", [])

        if not sentences:
            st.error("❌ No 'sentences' found in the uploaded file.")
        else:
            st.success(f"✅ Found {len(sentences)} sentences. Starting analysis...")

            results = []
            progress_bar = st.progress(0)

            for i, sentence in enumerate(sentences):
                with st.spinner(f"Analyzing sentence {i+1}/{len(sentences)}: \"{sentence}\""):
                    try:
                        response = requests.post(ANALYSIS_API_URL, json={"conversation": sentence})
                        if response.status_code == 200:
                            result = response.json()
                            result_data = result["result"]
                            results.append(result)

                            color = get_emotion_color(result_data.get("sentiment"))

                            st.markdown(
                                f"""
                                <div style='background-color: {color}; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                                    <strong>📌 Sentence:</strong> {result_data.get("sentence")}<br>
                                    <strong>🧠 Intent:</strong> {result_data.get("intent")}<br>
                                    <strong>❤️ Emotion:</strong> {result_data.get("sentiment").capitalize()}<br>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        else:
                            st.warning(f"⚠️ API error: {response.status_code}")
                    except Exception as e:
                        st.error(f"🔥 Server error: {e}")

                progress_bar.progress((i + 1) / len(sentences))
                time.sleep(0.2)

            st.success("🎉 All sentences analyzed!")

            if results:
                st.markdown("---")
                st.subheader("📊 Summary Table")
                st.dataframe([
                    {
                        "Sentence": r["result"]["sentence"],
                        "Intent": r["result"]["intent"],
                        "Emotion": r["result"]["sentiment"]
                    } for r in results
                ])

    except Exception as e:
        st.error(f"⚠️ Invalid JSON file: {e}")
