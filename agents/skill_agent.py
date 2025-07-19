from tools.skill_tools import get_career_roadmap

def skill_agent(career: str):
    """Returns skill roadmap for a career."""
    roadmap = get_career_roadmap(career)
    print(f"\nSkill roadmap for {career}:\n{roadmap}")
