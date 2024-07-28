
# Job Schedule API

This project is a job scheduling API built with FastAPI and connected to a PostgreSQL database. The API and database are hosted on Render, allowing you to interact with them directly.
## Host URL

The API is accessible at the following base URL:

```
https://job-schedule-api.onrender.com
```

## API Documentation

For detailed API documentation, visit the FastAPI docs at:
use:
```
API_KEY="123456"
```
```
https://job-schedule-api.onrender.com/docs
```



###


This project is a FastAPI application for managing job schedules with PostgreSQL as the backend database.

### Setup

1. **Clone the repository**:
    ```
    git clone https://github.com/karthik0497/job_schedule_api.git
    ```

2. **Accctivate a virtual environment**:
    ```
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a file named `env.sh` in the root directory of your project:
      ```
      export API_KEY="123456"
      export DATABASE_URL="postgresql://username:password@hostname:port/database?sslmode=verify-full"
      export API_KEY_NAME="access_token"
      ```
    - Replace `username`, `password`, `hostname`, `port`, and `database` with your actual database credentials.
    - Or run with same database url

    - Load the environment variables:
      ```
      source env.sh
      ```

5. **Run main python file to execute uvicorn**:
      ```
      python main.py
      ```
