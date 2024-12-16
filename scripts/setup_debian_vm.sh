# bash <(curl -Ls https://raw.githubusercontent.com/truedem0n/homelab/37d9ae6c68c074e2ffd9c6cc685acec54f563689/scripts/setup_debian_vm.sh)

apt install git ansible -y
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/distros/debian/base.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/docker.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/primary_nfs.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/rsync.yml
