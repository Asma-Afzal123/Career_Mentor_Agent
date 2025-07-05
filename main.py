# Streamlit version of Career Mentor Agent (Runs on localhost)
import streamlit as st

# Mock skill roadmap tool
def get_career_roadmap(career: str) -> str:
    skill_data = {
        "Software Engineer": ["Python", "Data Structures", "Algorithms", "Git", "System Design"],
        "Graphic Designer": ["Adobe Photoshop", "Illustrator", "Typography", "Color Theory"],
        "Data Analyst": ["Excel", "SQL", "Python", "Power BI", "Statistics"],
        "Teacher": ["Lesson Planning", "Classroom Management", "Subject Expertise", "Communication Skills"],
        "Digital Marketer": ["SEO", "Content Creation", "Analytics", "Email Marketing", "Social Media Ads"],
        "Accountant": ["Financial Reporting", "Bookkeeping", "Tax Laws", "Excel", "QuickBooks"],
        "Doctor": ["Anatomy", "Physiology", "Patient Care", "Clinical Skills", "Medical Ethics"]
    }
    skills = skill_data.get(career, ["Skill info not available"])
    return f"Skills for {career}: " + ", ".join(skills)

# Agent-like classes
class CareerAgent:
    def suggest_career(self, interest: str):
        interest = interest.lower()
        if any(word in interest for word in ["design", "graphic", "poster", "logo", "illustration"]):
            return "Graphic Designer"
        elif any(word in interest for word in ["data", "statistics", "analysis", "excel", "charts", "numbers"]):
            return "Data Analyst"
        elif any(word in interest for word in ["code", "coding", "programming", "python", "software", "developer", "app", "website"]):
            return "Software Engineer"
        elif any(word in interest for word in ["teach", "students", "school", "education", "classroom"]):
            return "Teacher"
        elif any(word in interest for word in ["marketing", "social media", "ads", "branding", "content"]):
            return "Digital Marketer"
        elif any(word in interest for word in ["accounting", "finance", "tax", "ledger", "audit"]):
            return "Accountant"
        elif any(word in interest for word in ["medicine", "hospital", "patients", "doctor", "treatment"]):
            return "Doctor"
        else:
            return "Data Analyst"

class SkillAgent:
    def get_skills(self, career: str):
        return get_career_roadmap(career)

class JobAgent:
    def get_jobs(self, career: str):
        jobs = {
            "Software Engineer": ["Web Developer", "Mobile App Developer", "DevOps Engineer"],
            "Graphic Designer": ["UI Designer", "Brand Identity Designer"],
            "Data Analyst": ["Business Analyst", "Data Scientist"],
            "Teacher": ["School Teacher", "Private Tutor", "Curriculum Designer"],
            "Digital Marketer": ["SEO Specialist", "Content Strategist", "Social Media Manager"],
            "Accountant": ["Chartered Accountant", "Tax Consultant", "Auditor"],
            "Doctor": ["General Physician", "Surgeon", "Pediatrician"]
        }
        return jobs.get(career, ["No roles found"])

# Streamlit UI
st.set_page_config(page_title="Career Mentor Agent")
st.title("🎓 Career Mentor Agent")
st.write("Guide your future by discovering your ideal career path!")

user_input = st.text_input("Tell us about your interests:", "Type your Interest here")

if st.button("Find My Career Path"):
    career_agent = CareerAgent()
    skill_agent = SkillAgent()
    job_agent = JobAgent()

    career = career_agent.suggest_career(user_input)
    skills = skill_agent.get_skills(career)
    jobs = job_agent.get_jobs(career)

    st.subheader("🎯 Career Path Suggested")
    st.success(career)

    st.subheader("📘 Skill Roadmap")
    st.info(skills)

    st.subheader("💼 Related Job Roles")
    st.write(", ".join(jobs))
