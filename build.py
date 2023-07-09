import requests
import os

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]
headers = {
  "Accept": "application/vnd.github+json",
  "Authorization": f"Bearer {GITHUB_TOKEN}",
  "X-GitHub-Api-Version": "2022-11-28",
}

#  https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#list-repository-workflows
response = requests.get(
    headers=headers,
    url=f"https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/workflows",
)
response.raise_for_status()
for workflow in response.json()["workflows"]:
    name = workflow["path"].split("/")[-1]
    if name.startswith("dispatch"):
      #  https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#create-a-workflow-dispatch-event
      workflow_response = requests.post(
        headers=headers,
        url=f"https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/workflows/{workflow['id']}/dispatches",
        json={
          "data1": "Hello World",  #  This can be an output from a previous task,
        },
      )
      response.raise_for_status()
      print(workflow_response.json())

