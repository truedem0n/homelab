# 

apt install git ansible -y
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/distros/debian/base.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/docker.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/primary_nfs.yml

