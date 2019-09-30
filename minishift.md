# minishift

works on DO

how to install:

## prepare kvm

sudo apt install qemu-kvm libvirt-daemon libvirt-daemon-system
curl -L https://github.com/dhiltgen/docker-machine-kvm/releases/download/v0.10.0/docker-machine-driver-kvm-ubuntu16.04 -o /usr/local/bin/docker-machine-driver-kvm
chmod +x /usr/local/bin/docker-machine-driver-kvm

## install bin

download from https://github.com/minishift/minishift/releases

## start

minishift start --cpus 3 --memory 15G --public-hostname 100.115.92.202 --routing-suffix 100.115.92.202.nip.io --disk-size=200G

## accessing it from laptop

ssh -L 0.0.0.0:8443:192.168.42.243:8443 167.71.76.81
		^ bind ip		^ $(minishift ip)    ^ DO VPS ip