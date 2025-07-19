def job_agent(career: str):
    """Returns real-world job roles."""
    jobs = {
        "Data Scientist": ["Data Analyst", "ML Engineer", "AI Researcher"],
        "Web Developer": ["Frontend Developer", "Backend Developer", "Full Stack Dev"]
    }
    print(f"\nJobs for {career}: {', '.join(jobs.get(career, ['No jobs found']))}")
