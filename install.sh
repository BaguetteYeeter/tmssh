mkdir -p $HOME/.ssh

function perms {
    echo "Failed to install /usr/local/bin/tmssh. This is likely due to wrong permissions, try running install as root"
    exit 1
}

curl -fL -o /usr/local/bin/tmssh https://github.com/BaguetteYeeter/tmssh/raw/master/tmssh || perms
chmod +x /usr/local/bin/tmssh

curl -fL -o $HOME/.ssh/tmssh.py https://github.com/BaguetteYeeter/tmssh/raw/master/tmssh.py

if [[ -f "$HOME/.ssh/tmssh_hosts" ]]; then
    echo "Hosts file exists, not overwriting"
else
    curl -fL -o $HOME/.ssh/tmssh_hosts https://github.com/BaguetteYeeter/tmssh/raw/master/tmssh_hosts

echo "TMSSH Installed"
exit 0
