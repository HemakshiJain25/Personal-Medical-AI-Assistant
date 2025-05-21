from .agent_base import AgentBase

class MedicalJargonSimplifierTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="MedicalJargonSimplifierTool", max_retries=max_retries, verbose=verbose)

    def execute(self, text):
        messages = [
            {"role": "system", "content": (
                "You are a medical language simplifier AI. Your task is to translate complex clinical or medical text into clear, accurate, and concise language that a patient without medical knowledge can easily understand.")},
            {"role": "user", "content": f"Simplify the following medical text for a patient: {text}"}
        ]
        return self.call_llama(messages, max_tokens=250)
