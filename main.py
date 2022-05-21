import json
import requests

from decouple import config


class NotionAccountingApi:
    token = config('NOTION_ACCESS_TOKEN')
    url_get_db = "https://api.notion.com/v1/databases/{}/query"
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    accounting_db_id = 'ef040e4fb96c47f89041c55e22618d19'

    def get_accounting_db(self):
        response = requests.post(
            url=self.url_get_db.format(self.accounting_db_id), 
            json=dict(page_size=100),
            headers=self.headers,
        )
        print(response.json())


api_req = NotionAccountingApi()
api_req.get_accounting_db()
