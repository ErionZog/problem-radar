import json
from datetime import datetime

# In the future, this is where we will call APIs (Reddit, etc.)
# For now, we simulate some "fresh" problems so you can see automation working.

def get_problems():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    problems = [
        {
            "id": f"demo_support_load_{today}",
            "source": "simulated",
            "subreddit": "SaaS",
            "problem": "Solo founders struggle to keep up with customer support while coding.",
            "who": "solo SaaS founders",
            "examples": [
                "I spend half my day in the helpdesk and never get to coding.",
                "Support tickets pile up whenever I try to focus on new features."
            ],
            "frequency_score": 4,
            "intensity_score": 3,
            "link": "https://example.com/support-load"
        },
        {
            "id": f"demo_invoices_{today}",
            "source": "simulated",
            "subreddit": "freelance",
            "problem": "Freelancers find it hard to chase late invoices without damaging client relationships.",
            "who": "freelancers and consultants",
            "examples": [
                "I hate sending payment reminders because I feel annoying.",
                "Clients ignore my invoices for weeks and I don’t know when to push."
            ],
            "frequency_score": 3,
            "intensity_score": 4,
            "link": "https://example.com/late-invoices"
        },
        {
            "id": f"demo_context_switching_{today}",
            "source": "simulated",
            "subreddit": "Entrepreneur",
            "problem": "Founders keep getting pulled into tiny tasks and struggle to find deep focus time.",
            "who": "early-stage founders",
            "examples": [
                "My day is just Slack, email, and quick tasks. No deep work.",
                "I can never get 2–3 hours straight to work on the important stuff."
            ],
            "frequency_score": 5,
            "intensity_score": 3,
            "link": "https://example.com/context-switching"
        }
    ]
    return problems

def main():
    problems = get_problems()
    with open("problems.json", "w", encoding="utf-8") as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
