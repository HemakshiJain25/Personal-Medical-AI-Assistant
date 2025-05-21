from .agent_base import AgentBase
class MentalHealthSupportBot(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="MentalHealthSupportBot", max_retries=max_retries, verbose=verbose)

    def execute(self, message):
        messages = [
            {"role": "system", "content": (
                "You are a compassionate AI offering first-level support for mental health. Respond with empathy and provide basic self-care suggestions, emotional validation, and links to professional resources if appropriate. Avoid diagnosis.")},
            {"role": "user", "content": message}
        ]
        return self.call_llama(messages, max_tokens=300)