from .agent_base import AgentBase
class LabResultExplainerTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="LabResultExplainerTool", max_retries=max_retries, verbose=verbose)

    def execute(self, lab_result):
        messages = [
            {"role": "system", "content": (
                "You are a clinical lab result interpreter for patients. Explain the test, what the result means in layman's terms, and what the patient should ask their doctor about next. Keep it medically accurate and easy to understand.")},
            {"role": "user", "content": f"Explain this lab result: {lab_result}"}
        ]
        return self.call_llama(messages, max_tokens=300)