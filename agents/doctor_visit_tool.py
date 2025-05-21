from .agent_base import AgentBase

class DoctorVisitPrepTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="DoctorVisitPrepTool", max_retries=max_retries, verbose=verbose)

    def execute(self, patient_input):
        messages = [
            {"role": "system", "content": (
                """You are a medical assistant that helps patients prepare for their doctor visits. 
                Based on their symptoms or concerns, provide:
                1. Key details to share with the doctor
                2. Important questions to ask
                3. Symptoms and metrics to track
                Be precise and patient-friendly."""
            )},
            {"role": "user", "content": f"Patient description: {patient_input}"}
        ]
        return self.call_llama(messages, max_tokens=300)
