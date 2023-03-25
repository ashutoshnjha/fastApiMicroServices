# fastApiMicroServices
For Docker based
* git clone https://github.com/ashutoshnjha/fastApiMicroServices.git
* cd fastApiMicroServices/
* docker build -t fastapi-hello .
* docker run -d --name anjhellocon -p 8080:8080 fastapi-hello
* docker ps
* http://myIP-host:8080/
* http://myIP-host:8080/hit/1?query=hello%20ashulab
* docker stop anjhellocon # To stop
* docker rm anjhellocon  # To remove container
* Push to docker registry to run.
  * docker tag fastapi-hello anjha/fastapi-hello
  * docker push anjha/fastapi-hello
  * docker run -dp 8080:8080 anjha/fastapi-hello
* 
