from .agent_base import AgentBase
class LifestyleCoachTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="LifestyleCoachTool", max_retries=max_retries, verbose=verbose)

    def execute(self, condition):
        messages = [
            {"role": "system", "content": (
                "You are a lifestyle coach focused on managing chronic health conditions. For the given condition, offer personalized and practical daily health tips involving diet, physical activity, habits, and mental wellness. Be clear and actionable.")},
            {"role": "user", "content": f"Give me daily tips for managing: {condition}"}
        ]
        return self.call_llama(messages, max_tokens=300)