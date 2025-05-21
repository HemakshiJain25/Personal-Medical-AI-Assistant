from .agent_base import AgentBase

class SymptomToConditionTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SymptomToConditionTool", max_retries=max_retries, verbose=verbose)

    def execute(self, symptoms_text):
        messages = [
            {"role": "system", "content": (
                "You are a medical AI assistant. Given a patient's description of their symptoms in natural language, "
                "your job is to provide:\n"
                "- Possible medical conditions\n"
                "- When they should see a doctor (urgency)\n"
                "- What signs/symptoms to monitor\n\n"
                "Keep the language simple and empathetic. Always recommend seeing a healthcare professional if the symptoms may be serious."
            )},
            {"role": "user", "content": (
                f"A patient says: \"{symptoms_text}\"\n\n"
                "Please provide:\n"
                "1. Possible conditions\n"
                "2. When to see a doctor\n"
                "3. What to monitor\n"
            )}
        ]
        response = self.call_llama(messages, max_tokens=350)
        return response
