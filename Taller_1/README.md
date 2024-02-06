´´´ shell
docker build -t penguinsapi .
´´´

´´´ shell
docker run -d --name penguinsapicontainer -p 8089:80 penguinsapi
´´´

0.0.0.0:80/get_models

0.0.0.0:80/predict/random_tree


