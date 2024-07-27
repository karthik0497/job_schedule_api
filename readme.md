Copy code
# Job Scheduler API

This project is a FastAPI application for managing job schedules with PostgreSQL as the backend database.

### Setup

1. **Clone the repository**:
    ```
    git clone <repository-url>
    cd <repository-directory>
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

**5. Add ssl Certificate**

### Configuring SSL Certificates for PostgreSQL/CockroachDB

**1. Download the Certificate**

Use the following command to download the SSL certificate:

for window
```
mkdir -p $env:appdata\postgresql\; Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/f2bee8e2-397f-4458-8ed7-b244779cadda/cert -OutFile $env:appdata\postgresql\root.crt
```
for linux and mac
```
curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/f2bee8e2-397f-4458-8ed7-b244779cadda/cert'
```

for linus use like this 

```
curl -o /home/cockroach-cert.crt https://cockroachlabs.cloud/clusters/f2bee8e2-397f-4458-8ed7-b244779cadda/cert
```

**2. Update PostgreSQL Client Configuration**

Ensure that your PostgreSQL or CockroachDB client is configured to use the downloaded certificate.

**For Local PostgreSQL Client:**

- **Move the Certificate:**

  Move the downloaded certificate to the default PostgreSQL directory:

  ```
  mkdir -p ~/home/.postgresql
  mv /home/cockroach-cert.crt ~/.postgresql/root.crt
  ```

- **Set Permissions:**

  Ensure the certificate file has the appropriate permissions:

  ```
  chmod 644 ~/.postgresql/root.crt
  ```

---

By following these steps, you ensure that your PostgreSQL or CockroachDB client can securely connect to the server using the SSL certificate.


6 .**Run main python file to execute uvicorn**:
      ```
      python main.py
      ```