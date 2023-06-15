## Running the code

```shell
#Clone the repository by running 
git clone https://github.com/AshminJayson/Volopay_Price_API

#Install necessary libraries in requirements.txt
cd Volopay_Price_API
pip install -r requirements.txt

#Run the fastapi backend
uvicorn main:app --reload --port=8000
```

The application can then be accessed on port *localhost:8000* and the *swagger file is available on localhost:8000/docs* and *redoc on localhost:8000/redoc*
