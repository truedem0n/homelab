# bash <(curl -Ls https://raw.githubusercontent.com/truedem0n/homelab/7f50100aad33612149058a1dffa2f1f1fd64232f/scripts/setup_alpine_vm.sh)

/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/distros/alpine/base.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/docker.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/primary_nfs.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/rsync.yml