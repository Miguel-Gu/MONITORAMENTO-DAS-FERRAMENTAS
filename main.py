import os
import json
from datetime import datetime
import requests


URL = os.getenv("URL")


def toTeams(event):
    started_date = datetime.fromtimestamp(event["incident"]["started_at"]).isoformat(
    ) if event["incident"]["started_at"] else None
    ended_date = datetime.fromtimestamp(event["incident"]["ended_at"]).isoformat(
    ) if event["incident"]["ended_at"] else None

    policy_name = event["incident"]["policy_name"] if event["incident"]["policy_name"] != "" else '-'
    condition_name = event["incident"]["condition_name"] if event["incident"]["condition_name"] != "" else '-'
    response_code = event["incident"]["metric"]["labels"].get("response_code") if event["incident"]["metric"]["labels"].get("response_code") else None
    project_id = event["incident"]["resource"]["labels"]["project_id"]

    facts = [
        {
            "name": "Incident ID",
            "value": event["incident"]["incident_id"]
        },
        {
            "name": "Condition",
            "value": condition_name
        },
        {
            "name": "Project ID",
            "value": project_id
        }
    ]

    if response_code:
        facts.append({"name": "Status Code", "value": response_code})

    if started_date:
        facts.append({
            "name": "Started at",
            "value": started_date
        })
        if ended_date:
            facts.append({
                "name": "Ended at",
                "value": ended_date
            })

    colour = "#F5222D" if event["incident"]["state"] == "open" else "#1890FF"
    title = f"Incident opened for {policy_name}" if event["incident"][
        "state"] == "open" else f"Incident closed for {policy_name}"
    summary = event["incident"]["summary"] if event["incident"]["summary"] != "" else "No summary available."

    return json.dumps({
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": colour,
        "title": title,
        "text": summary,
        "summary": summary,
        "sections": [{
            "activityImage": "https://cloudconfusing.com/wp-content/uploads/2019/01/gcpLOGO.png",
            "facts": facts}],
        "potentialAction": [{
            "@context": "http://schema.org",
            "@type": "ViewAction",
            "name": "View Incident",
            "target": [event["incident"]["url"]]
        }]
    })


def handler(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    data = request.get_json()
    print(data)


    response = requests.post(
        url=URL,
        data=toTeams(data)
    )
    return response.content