
## Running the API locally

### Without using Docker

To run the API without using Docker, follow the below given steps :
- Enter into src.
- Activate virtualenv if you want.
- Install dependencis using ``` pip install -r requirements.txt```. You might need to provide superuser access.
- Run the server using ``` python3 run.py ```

The server will be running at http://127.0.0.1:5000

### With Docker

To run using Docker, follow the below given instructions :
- First ensure that you have Docker CLI installed.
- Next, build the Docker image using ```docker build -t scribble:v1 . ```
- Next run the docker image using the following: 
  ``` docker run --rm -it -p 8080:8080 -e CLUSTER_NAME=[your-hasura-cluster-name] scribble:v1 ```

The server will be running at http://127.0.0.1:8080
