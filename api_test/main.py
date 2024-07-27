import httpx
import time,os
import asyncio

BASE_URL = os.getenv("BASE_URL")
API_KEY_NAME = os.getenv('API_KEY_NAME')
API_KEY = os.getenv('API_KEY')
headers = {
    API_KEY_NAME: API_KEY
}

async def test_list_jobs():
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/jobs", headers=headers)
    total_time = time.time() - start_time
    print(f"List Jobs - Status: {'Success' if response.status_code == 200 else 'Failure'}, Time: {total_time:.2f}s, Data: {response.json()}")

async def test_get_job(job_id):
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/jobs/{job_id}", headers=headers)
    total_time = time.time() - start_time
    print(f"Get Job - Status: {'Success' if response.status_code == 200 else 'Failure'}, Time: {total_time:.2f}s, Data: {response.json()}")

async def test_create_job():
    job_data = {
        "job_name": "Test Job",
        "job_schedule": "22:30 thursday may 30",
        "job_description": "A test job",
        "job_type": "test",
        "job_params": {"param1": "value1"}
    }
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/jobs", json=job_data, headers=headers)
    total_time = time.time() - start_time
    print(f"Create Job - Status: {'Success' if response.status_code == 200 else 'Failure'}, Time: {total_time:.2f}s, Data: {response.json()}")
    return response.json().get("job_id")

async def test_delete_all_jobs():
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/jobs", headers=headers)
    total_time = time.time() - start_time
    print(f"Delete All Jobs - Status: {'Success' if response.status_code == 200 else 'Failure'}, Time: {total_time:.2f}s, Data: {response.json()}")

async def test_delete_job(job_id):
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/jobs/{job_id}", headers=headers)
    total_time = time.time() - start_time
    print(f"Delete Job - Status: {'Success' if response.status_code == 200 else 'Failure'}, Time: {total_time:.2f}s, Data: {response.json()}")

async def run_tests():
    await test_list_jobs()
    job_id = await test_create_job()
    await test_get_job(job_id)
    await test_delete_job(job_id)
    await test_delete_all_jobs()

if __name__ == "__main__":
    asyncio.run(run_tests())
