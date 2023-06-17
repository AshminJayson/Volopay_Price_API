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

The deployed api routes are available on https://volopay-api.onrender.com/<insert_route_here>

The application can then be accessed on port _localhost:8000_ and the _swagger file is available on localhost:8000/docs_ and _redoc on localhost:8000/redoc_

The postman collection is available on https://www.postman.com/navigation-observer-56103879/workspace/volopay-task/collection/26298297-ed28e07f-8709-4f71-b72d-1fd2accc8e2d?action=share&creator=26298297
