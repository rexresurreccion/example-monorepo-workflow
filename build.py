import requests
import os

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]
GITHUB_REF_NAME = os.environ["GITHUB_REF_NAME"]
headers = {
  "Accept": "application/vnd.github+json",
  "Authorization": f"Bearer {GITHUB_TOKEN}",
  "X-GitHub-Api-Version": "2022-11-28",
}
print(f"GITHUB_REF_NAME: {GITHUB_REF_NAME}")
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
          "ref": GITHUB_REF_NAME,
          "inputs": {
            "data1": "Hello world",  # This can be an output from previous task
          }.
        },
      )
      response.raise_for_status()
      print(workflow_response.json())

