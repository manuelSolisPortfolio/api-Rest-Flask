# Descarga e instala SonarQube
wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-8.9.2.zip
unzip sonarqube-8.9.2.zip

# Inicia SonarQube
cd sonarqube-8.9.2
./bin/sonar.sh start

# Descarga e instala el escáner de SonarQube
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.7.0.2472.zip
unzip sonar-scanner-cli-4.7.0.2472.zip

# Configura el token de acceso de SonarQube
echo "sonar.login=my-sonarqube-token" > sonar-scanner.properties

# Instala el escáner de zona
wget https://github.com/SonarSource/sonar-scanner-sonarqube-plugin/releases/download/v2.12.0/sonar-scanner-sonarqube-plugin-2.12.0.zip
unzip sonar-scanner-sonarqube-plugin-2.12.0.zip

# Actualiza el archivo de configuración del escáner de zona
echo "sonar.sonarqube.host=http://localhost:9000" > sonar-scanner-sonarqube-plugin.properties

# Ejecuta el análisis de SonarQube
sonar-scanner
