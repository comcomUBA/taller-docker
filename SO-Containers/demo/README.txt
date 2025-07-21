sudo mkdir /mnt/merged
cd overlay
mount -t overlay -o lowerdir=./lower,upperdir=./upper,workdir=./workdir overlay /mnt/merged
cd /mnt/merged

Mostrar en Docker:

docker pull nginx
docker inspect nginx | jq .[0].GraphDriver.Data