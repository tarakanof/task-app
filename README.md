# Task-App
## Simple http-server "Hello, worlkd" app

To run app with docker-compose in folder *development* run command:
```
docker-compose up
```
 - Application is availiable on localhost ip address on port 80. In browser go to `http://localhost`, or 
```
curl http://localhost
```
 - Metrics are exposed to `http://localhost/metrics`
```
curl http://localhost/metrics
```
 - Prometheus: `http://localhost:9090`
 - Grafana with sample dashboards: `http://localhost:3000` login: admin and password: admin

Prometheus config: `./development/prometheus/`
Grafana config and dashboard: `./development/grafana`

## Helm chart
Chart in `./deployment/tast-app`
*Some variables must be set before installing!*
look in `variables.yaml`
To install in kubernetes cluster:
```
helm upgrade --install ./deployment/tast-app
```
###

## About gitlab-ci:
Sample gitlab-ci with build and deploy to kubernetes stages.

This variables must be set in project CI/CD variables:
 - `PAT` private acces token
 - `VERSION` version of the app / docker image. Format: `0.0.0`
 - `MY_REGISTRY` docker registry url
 - `MY_REGISTRY_USER`
 - `MY_REGISTRY_USER_PASSWORD`
 - `KUBE_CONFIG`
