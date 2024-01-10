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

# Wait for SonarQube analysis to complete
echo "Waiting for SonarQube analysis to complete..."
while ! curl -s -f -u admin:admin "http://localhost:9000/api/qualitygates/project_status?projectKey=my-project" | grep -q '"status":"OK"'; do
    sleep 1
done
# Showing scanner results
echo -e "Showing project analyses... \n"
curl -u admin:admin http://localhost:9000/api/project_analyses/search?project=my-project
echo -e "\n"
echo -e "\n Showing duplications... \n"
curl -u admin:admin http://localhost:9000/api/duplications/show?key=my-project
echo -e "\n"
echo -e "\n Showing issues... \n"
curl -u admin:admin http://localhost:9000/api/issues/search?componentKeys=my-project
echo -e "\n"
echo -e "\n Showing hotspots... \n"
curl -u admin:admin http://localhost:9000/api/hotspots/search?project=my-project
echo -e "\n"
echo -e "\n Showing measurements... \n"
curl -u admin:admin "http://localhost:9000/api/measures/component_tree?component=my-project&metricKeys=ncloc,complexity,violations,security_rating,bugs,vulnerabilities,code_smells,coverage"
