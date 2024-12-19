# bash <(curl -Ls https://raw.githubusercontent.com/truedem0n/homelab/274fb8e5c0b6d96e2e592f6445e11f6f9c69d3e3/scripts/setup_alpine_vm.sh)

/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/distros/alpine/base.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/docker.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/primary_nfs.yml
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbooks/rsync.yml