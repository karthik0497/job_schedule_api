
from fastapi import *
from api_route import router as job_router
from config import *

app = FastAPI(
    title=settings.APP_NAME,
)

app.include_router(job_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)