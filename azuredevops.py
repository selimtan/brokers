import requests
import json

# Azure DevOps için gerekli bilgileri değiştirin
organization = "{organization_name}"
project = "{project_name}"
token = "{personal_access_token}"

# REST API'nin endpoint'ini ve sorgulama parametrelerini oluşturun
url = f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems?api-version=6.1&$top=100&$select=System.Id,System.Title,System.State"
headers = {"Authorization": f"Basic {token}"}

# REST API'ye istek gönderin ve sonucu işleyin
response = requests.get(url, headers=headers)
if response.status_code == 200:
    issues = json.loads(response.text)["value"]
    for issue in issues:
        print(f"Issue ID: {issue['id']}, Title: {issue['fields']['System.Title']}, State: {issue['fields']['System.State']}")
else:
    print(f"Failed to get issues. Response code: {response.status_code}, Reason: {response.reason}")
Bu örnek, belirtilen Azure DevOps örgütü ve projesi için ilk 100 issue'ı alır ve her birinin ID'si, 
