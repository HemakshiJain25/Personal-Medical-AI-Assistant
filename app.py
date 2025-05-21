# app.py

import streamlit as st
from agents import AgentManager
from utils.logger import logger
import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

def main():
    st.set_page_config(page_title="Multi-Agent AI System", layout="wide")
    st.title("Personal Medical AI Assisstant")

    st.sidebar.title("Select Task")
    task = st.sidebar.selectbox("Choose a task:", [
        "Summarize Medical Text",
        "Mental HealthCare and Support",
        "Lifestyle Coach",
        "Pre-Diagnosis",
        "Lab Results Simplifier",
        "Jargon Simplifier",
        "Visit Prep",
         "Advisor"
    ])

    agent_manager = AgentManager(max_retries=2, verbose=True)

    if task == "Summarize Medical Text":
        summarize_section(agent_manager)
    elif task == "Mental HealthCare and Support":
        healthcare_support_section(agent_manager)
    elif task=="Lifestyle Coach":
        coach_section(agent_manager)
    elif task=="Lab Results Simplifier":
        lab_section(agent_manager)
    elif task=="Jargon Simplifier":
        jargon_section(agent_manager)
    elif task=="Visit Prep":
        prep_section(agent_manager)
    elif task=="Advisor":
        advisor_section(agent_manager)                
    elif task=="Pre-Diagnosis":
        symptom_section(agent_manager)    

def summarize_section(agent_manager):
    st.header("Summarize Medical Text")
    text = st.text_area("Enter medical text to summarize:", height=200)
    if st.button("Summarize"):
        if text:
            main_agent = agent_manager.get_agent("summarize")
            with st.spinner("Summarizing..."):
                try:
                    summary = main_agent.execute(text)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"SummarizeAgent Error: {e}")
                    return        
        else:
            st.warning("Please enter some text to summarize.")

def healthcare_support_section(agent_manager):
    st.header("Get Pesonalised Heath Care and Support")
    topic = st.text_input("Enter:")
    if st.button("output"):
        if topic:
            writer_agent = agent_manager.get_agent("Mental Health Care support")
            with st.spinner("Suggesting..."):
                try:
                    draft = writer_agent.execute(topic)
                    st.write(draft)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Error: {e}")
                    return
        else:
            st.warning("Please enter.")

def coach_section(agent_manager):
    st.header(" Here: I am you personalised Lifesytle coach!!")
    medical_data = st.text_area("Enter:", height=200)
    if st.button("Output"):
        if medical_data:
            main_agent = agent_manager.get_agent("Lifestyle Coach")
            with st.spinner("Processing..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("My Suggestions:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Error: {e}")
                    return
        else:
            st.warning("Please enter.")


def symptom_section(agent_manager):
     st.header("Wanna a Pre-Diagnosis?Here I am to help you!!")
     text = st.text_area("Enter medical symptoms:", height=200)
     if st.button("output"):
        if text:
            main_agent = agent_manager.get_agent("Pre-Diagnosis")
            
            with st.spinner("answering..."):
                try:
                    summary = main_agent.execute(text)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Error: {e}")
                    return
        else:
            st.warning("Please enter some text.")

def lab_section(agent_manager):
    st.header("Wanna simplify your medical reports?")
    medical_data = st.text_area("Enter data:", height=200)
    if st.button("Process"):
        if medical_data:
            main_agent = agent_manager.get_agent("Lab Results Simplifier")
            with st.spinner("Processing data..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("Simplified Vesion:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Error: {e}")
                    return
        else:
            st.warning("Please enter.")            



def jargon_section(agent_manager):
    st.header("Wanna understand difficult medical terms??Ask Me!!")
    medical_data = st.text_area("Enter data:", height=200)
    if st.button("Process"):
        if medical_data:
            main_agent = agent_manager.get_agent("Jargon Simplifier")
            with st.spinner("Processing data..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("Simplified Vesion:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Error: {e}")
                    return
        else:
            st.warning("Please enter.") 

def prep_section(agent_manager):
    st.header("If want to visit doctor, I am here to help you out!!")
    medical_data = st.text_area("Enter data:", height=200)
    if st.button("Process"):
        if medical_data:
            main_agent = agent_manager.get_agent("Visit Prep")
            with st.spinner("Processing data..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("My Output:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Error: {e}")
                    return
        else:
            st.warning("Please enter.")



def advisor_section(agent_manager):
    st.header("Want some medical advise??Ask Me!!")
    medical_data = st.text_area("Enter data:", height=200)
    if st.button("Process"):
        if medical_data:
            main_agent = agent_manager.get_agent("advisor")
            with st.spinner("Processing data..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("Advice:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Error: {e}")
                    return
        else:
            st.warning("Please enter.")
            
                               

if __name__ == "__main__":
    main()