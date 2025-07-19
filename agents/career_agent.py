def career_agent():
    """Suggests career paths based on user interests."""
    while True:
        interest = input("What are your interests? (e.g., data, design, coding): ")
        if "data" in interest.lower():
            print("You may enjoy becoming a Data Scientist.")
            return "Data Scientist"
        elif "web" in interest.lower() or "coding" in interest.lower():
            print("You might like becoming a Web Developer.")
            return "Web Developer"
        else:
            print("Try exploring general career fields like IT, Design, or Business.")
            return "General"
