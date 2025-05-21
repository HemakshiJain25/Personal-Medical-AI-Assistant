import gradio as gr
from agents import AgentManager
from utils.logger import logger
import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# Initialize agent manager
agent_manager = AgentManager(max_retries=2, verbose=True)

# Custom CSS for styling
custom_css = """
#title { 
    text-align: center;
    color: #2d3436;
    font-family: 'Arial', sans-serif;
}
.description {
    text-align: center;
    color: #636e72;
    font-size: 1.1em;
}
.sidebar {
    background-color: #f5f6fa !important;
    border-radius: 10px !important;
    padding: 20px !important;
}
.tab-item {
    background-color: #f5f6fa !important;
    border-radius: 5px !important;
    padding: 10px !important;
    margin: 5px !important;
}
.tab-item.selected {
    background-color: #a29bfe !important;
    color: white !important;
}
.output-label {
    font-size: 1.2em !important;
    font-weight: bold !important;
    color: #6c5ce7 !important;
}
"""

def summarize_medical_text(text):
    if not text:
        return "Please enter some text to summarize."
    try:
        main_agent = agent_manager.get_agent("summarize")
        return main_agent.execute(text)
    except Exception as e:
        logger.error(f"SummarizeAgent Error: {e}")
        return f"Error: {str(e)}"

def healthcare_support(topic):
    if not topic:
        return "Please enter your query."
    try:
        writer_agent = agent_manager.get_agent("Mental Health Care support")
        return writer_agent.execute(topic)
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

def lifestyle_coach(medical_data):
    if not medical_data:
        return "Please enter your information."
    try:
        main_agent = agent_manager.get_agent("Lifestyle Coach")
        return main_agent.execute(medical_data)
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

def pre_diagnosis(text):
    if not text:
        return "Please enter your symptoms."
    try:
        main_agent = agent_manager.get_agent("Pre-Diagnosis")
        return main_agent.execute(text)
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

def lab_results_simplifier(medical_data):
    if not medical_data:
        return "Please enter your lab results."
    try:
        main_agent = agent_manager.get_agent("Lab Results Simplifier")
        return main_agent.execute(medical_data)
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

def jargon_simplifier(medical_data):
    if not medical_data:
        return "Please enter the medical terms you want simplified."
    try:
        main_agent = agent_manager.get_agent("Jargon Simplifier")
        return main_agent.execute(medical_data)
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

def visit_prep(medical_data):
    if not medical_data:
        return "Please enter your information."
    try:
        main_agent = agent_manager.get_agent("Visit Prep")
        return main_agent.execute(medical_data)
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

def medical_advisor(medical_data):
    if not medical_data:
        return "Please enter your question."
    try:
        main_agent = agent_manager.get_agent("advisor")
        return main_agent.execute(medical_data)
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {str(e)}"

# Create the Gradio interface
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    <h1 id="title">Personal Medical AI Assistant</h1>
    <p class="description">Your intelligent companion for medical information and support</p>
    """)
    
    with gr.Tabs() as tabs:
        with gr.TabItem("Summarize Medical Text", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    text_input = gr.TextArea(label="Enter medical text to summarize:", lines=10)
                    summarize_btn = gr.Button("Summarize", variant="primary")
                with gr.Column():
                    output_summary = gr.TextArea(label="Summary:", interactive=False)
            summarize_btn.click(summarize_medical_text, inputs=text_input, outputs=output_summary)
        
        with gr.TabItem("Mental HealthCare and Support", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    topic_input = gr.Textbox(label="Enter your mental health query:")
                    support_btn = gr.Button("Get Support", variant="primary")
                with gr.Column():
                    output_support = gr.TextArea(label="Response:", interactive=False)
            support_btn.click(healthcare_support, inputs=topic_input, outputs=output_support)
        
        with gr.TabItem("Lifestyle Coach", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    coach_input = gr.TextArea(label="Tell me about your lifestyle:", lines=10)
                    coach_btn = gr.Button("Get Advice", variant="primary")
                with gr.Column():
                    output_coach = gr.TextArea(label="Lifestyle Suggestions:", interactive=False)
            coach_btn.click(lifestyle_coach, inputs=coach_input, outputs=output_coach)
        
        with gr.TabItem("Pre-Diagnosis", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    symptoms_input = gr.TextArea(label="Describe your symptoms:", lines=10)
                    diagnose_btn = gr.Button("Analyze Symptoms", variant="primary")
                with gr.Column():
                    output_diagnosis = gr.TextArea(label="Analysis:", interactive=False)
            diagnose_btn.click(pre_diagnosis, inputs=symptoms_input, outputs=output_diagnosis)
        
        with gr.TabItem("Lab Results Simplifier", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    lab_input = gr.TextArea(label="Enter your lab results:", lines=10)
                    lab_btn = gr.Button("Simplify Results", variant="primary")
                with gr.Column():
                    output_lab = gr.TextArea(label="Simplified Version:", interactive=False)
            lab_btn.click(lab_results_simplifier, inputs=lab_input, outputs=output_lab)
        
        with gr.TabItem("Jargon Simplifier", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    jargon_input = gr.TextArea(label="Enter medical terms to simplify:", lines=10)
                    jargon_btn = gr.Button("Simplify Terms", variant="primary")
                with gr.Column():
                    output_jargon = gr.TextArea(label="Simplified Explanation:", interactive=False)
            jargon_btn.click(jargon_simplifier, inputs=jargon_input, outputs=output_jargon)
        
        with gr.TabItem("Visit Prep", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    visit_input = gr.TextArea(label="What do you need help preparing for?", lines=10)
                    visit_btn = gr.Button("Prepare for Visit", variant="primary")
                with gr.Column():
                    output_visit = gr.TextArea(label="Preparation Guide:", interactive=False)
            visit_btn.click(visit_prep, inputs=visit_input, outputs=output_visit)
        
        with gr.TabItem("Medical Advisor", elem_classes="tab-item"):
            with gr.Row():
                with gr.Column():
                    advisor_input = gr.TextArea(label="Ask your medical question:", lines=10)
                    advisor_btn = gr.Button("Get Advice", variant="primary")
                with gr.Column():
                    output_advisor = gr.TextArea(label="Medical Advice:", interactive=False)
            advisor_btn.click(medical_advisor, inputs=advisor_input, outputs=output_advisor)

if __name__ == "__main__":
    app.launch()