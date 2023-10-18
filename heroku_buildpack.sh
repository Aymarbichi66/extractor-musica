#!/bin/sh

echo "-----> Personalizado Buildpack para Python"

# Instala Python y dependencias
apt-get update
apt-get install -y python3 python3-pip

# Llama al buildpack de Python estándar
echo "-----> Llamando al buildpack de Python estándar"
curl https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz | tar xz -C /tmp/
/tmp/opt/buildpacks/python/bin/compile /tmp /app
