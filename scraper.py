import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def scrape_events():
    url = "https://realpython.github.io/fake-jobs/"

    try:
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
    except Exception as e:
        print("Error fetching website:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    events = []

    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        location = job.find("p", class_="location").text.strip()

        events.append({
            "title": title,
            "date": "2026-01-01",
            "location": location,
            "source": "FakeJobs"
        })

    return events
