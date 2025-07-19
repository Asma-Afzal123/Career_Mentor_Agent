from agents.career_agent import career_agent
from agents.skill_agent import skill_agent
from agents.job_agent import job_agent

def main():
    print("🎓 Welcome to Career Mentor Agent 🎓")
    career = career_agent()
    skill_agent(career)
    job_agent(career)

if __name__ == "__main__":
    main()
