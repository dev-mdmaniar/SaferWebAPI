from fastapi import FastAPI
from typing import Union
from safer import CompanySnapshot
import json

app = FastAPI()

@app.get("/test/")
def read_root():
    return {'message': 'Hello World'}

@app.get("/test/item/{itemId}")
def read_item(itemId:int, q: Union[str, None] = None):
    return {"temId": itemId, "query para": q}


@app.get("/api/CompanySnapshot/{dotNumber}")
async def get_comppany_snapshot(dotNumber: int):
    data = getCompanySnapshotData(dotNumber)
    return {"data": data}

def getCompanySnapshotData(dotNumber:int):
    # call SAFER API for company snapshot
    client = CompanySnapshot()
    print(f'Please wait... fetching Company Snapshot details for {dotNumber}...')

    company = client.get_by_usdot_number(int(dotNumber))

    print(f'Company Snapshot data for {dotNumber}: ')
    print(company.to_json())
    
    companySnapshot = json.loads(company.to_json())

    # TODO: Error handling

    return companySnapshot

