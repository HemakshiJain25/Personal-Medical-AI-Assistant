from .agent_base import AgentBase

class MedicationAdvisorTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="MedicationAdvisorTool", max_retries=max_retries, verbose=verbose)

    def execute(self, medications):
        messages = [
            {"role": "system", "content": (
                '''You are a medication assistant AI. For the given list of medications, provide:
                1. A safe and easy-to-follow schedule
                2. Key food or drug interaction warnings
                3. Common and notable side effects
                Always encourage consulting a healthcare provider before making changes.'''
            )},
            {"role": "user", "content": f"I am taking: {medications}"}
        ]
        return self.call_llama(messages, max_tokens=300)
