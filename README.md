# fastApiMicroServices
For Docker based
* git clone https://github.com/ashutoshnjha/fastApiMicroServices.git
* cd fastApiMicroServices/
* docker build -t anjhelloimg .
* docker run -d --name anjhellocon -p 8080:8080 anjhelloimg
* docker ps
* http://myIP-host:8080/
* http://myIP-host:8080/hit/1?query=hello%20ashulab
* docker stop anjhellocon # To stop
* docker rm anjhellocon  # To remove container
