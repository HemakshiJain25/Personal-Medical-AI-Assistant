# agents/__init__.py

from .summarize_tool import SummarizeTool
from .mentalhealth_support import MentalHealthSupportBot
from .lifestyle_coach import LifestyleCoachTool
from .lab_result import LabResultExplainerTool
from .jargon_simplifier_tool import MedicalJargonSimplifierTool
from .doctor_visit_tool import DoctorVisitPrepTool
from .advisor import MedicationAdvisorTool
from .symptom_to_condition_tool import SymptomToConditionTool


class AgentManager:
    def __init__(self, max_retries=2, verbose=True):
        self.agents = {
            "Summarize": SummarizeTool(max_retries=max_retries, verbose=verbose),
            "Mental Health Care support": MentalHealthSupportBot(max_retries=max_retries, verbose=verbose),
            "Lifestyle Coach": LifestyleCoachTool(max_retries=max_retries, verbose=verbose),
            "Lab Results Simplifier": LabResultExplainerTool(max_retries=max_retries, verbose=verbose),
            "Jargon Simplifier": MedicalJargonSimplifierTool(max_retries=max_retries, verbose=verbose),
            "Visit Prep": DoctorVisitPrepTool(max_retries=max_retries, verbose=verbose),
            "Advisor": MedicationAdvisorTool(max_retries=max_retries, verbose=verbose),      # New agent
            "Pre-Diagnosis":SymptomToConditionTool(max_retries=max_retries, verbose=verbose)   # New agent
        }

    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Agent '{agent_name}' not found.")
        return agent