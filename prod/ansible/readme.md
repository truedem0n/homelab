
# Ansible one liner
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbook.yml

# For ansible on alpine
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/alpine.yml


## LXC containers

# adguard
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/lxc/adguard.yml

/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/lxc/light.yml


# backups
@daily /usr/bin/restic -r /mnt/backups/restic-backup backup /mnt/pve/local-nfs/docker/ --password-file ~/restic_p