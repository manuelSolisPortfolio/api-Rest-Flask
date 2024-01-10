#!/bin/bash
set -e
#Check if sonarnet doesn't exist
if [ ! "$(docker network ls | grep sonarnet)" ]; then
    docker network create sonarnet
fi

#Check if sonarqube containers exist
if [ "$(docker ps -q -f name=sonarqube)" ]; then
    docker rm -f sonarqube
fi

#Start SonarQube container
docker run -d --name sonarqube \
  -e SONARQUBE_USER=admin \
  -e SONARQUBE_PASSWORD=admin \
  --network sonarnet \
  -p 9000:9000 sonarqube 

# Wait for SonarQube to start
echo "Waiting for SonarQube server to start..."
while ! curl -s -f -u admin:admin "http://localhost:9000/api/system/status" | grep -q '"status":"UP"'; do
    sleep 1
done

#Check if sonarscan containers exist
if [ "$(docker ps -aq -f name=sonarscan)" ]; then

    docker rm -f sonarscan
fi

# Run sonar scanner cli
docker run -d --name sonarscan \
    --network sonarnet \
    -e SONAR_HOST_URL=http://sonarqube:9000 \
    sonarsource/sonar-scanner-cli\
    -Dsonar.login=admin \
    -Dsonar.password=admin \
    -Dsonar.projectKey=my-project \
    -Dsonar.sources=./app
docker exec -it sonarscan sh -c 'pwd && ls -l && mkdir app &&  chmod 777 app && cd /usr/src/app && ls -l'
docker cp . sonarscan:/usr/src/app 
docker exec -it sonarscan sh -c 'pwd && \
    ls -l && \
    cd /usr/src/app && \
    pwd && \
    ls -la && \
    rm -r ./flask_kubernetes && \
    ls -la && \
    sonar-scanner -Dsonar.login=admin \
    -Dsonar.password=admin \
    -Dsonar.projectKey=my-project'

# Showing scanner results
echo "Showing issues..."
curl -u admin:admin http://localhost:9000/api/issues/search?componentKeys=my-project
