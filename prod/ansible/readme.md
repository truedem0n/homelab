
# Ansible one liner
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/playbook.yml

# For ansible on alpine
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/alpine.yml

## VMs
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/vms/vpn.yml


## LXC containers

# adguard
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/lxc/adguard.yml

/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/lxc/light.yml > /var/log/ansible-pull.log 2>&1

## Lubuntu
/usr/bin/ansible-pull -U https://github.com/truedem0n/homelab.git prod/ansible/lubuntu/main.yml > /var/log/ansible-pull.log 2>&1


# backups
@daily /usr/bin/restic -r /mnt/backups/restic-backup backup /mnt/pve/local-nfs/docker/ --password-file ~/restic_p

/usr/bin/restic -r /mnt/backups/restic-backup snapshots --password-file ~/restic_p


# watchtower
docker run -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --run-once

# Useful proxmox cmd
echo 1 > /proc/sys/kernel/sysrq
echo b > /proc/sysrq-trigger