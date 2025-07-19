def get_career_roadmap(career: str) -> str:
    """Returns a skill roadmap for a given career"""
    roadmaps = {
        "Data Scientist": "- Learn Python\n- Learn Pandas, NumPy\n- Learn ML with Scikit-learn\n- Projects & Kaggle",
        "Web Developer": "- HTML/CSS/JS\n- React ya Next.js\n- Backend: Django ya Node.js\n- Git + Hosting",
        "Graphic Designer": "- Adobe Photoshop\n- Adobe Illustrator\n- UI/UX tools (Figma)\n- Portfolio Projects"
    }
    return roadmaps.get(career, "No roadmap available for this field.")
