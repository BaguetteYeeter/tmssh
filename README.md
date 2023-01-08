# TMSSH

TMSSH is an ssh manager. It was written in Python3.

## Installation

Clone the git repo, cd into it, and run `bash install.sh`.

TMSSH requires `python3` installed.

## Usage

To open, run `tmssh`

If you get a Command Not Found, add `/usr/local/bin` to your $PATH

TMSSH is mainly built on commands. You type a command and press enter

### Add a host
Type `a` and press enter. Type in the username and hostname of the server. The host has now been added.

### Remove a host
To remove a host, you can't (i can't be bothered). So run `echo "" > ~/.ssh/tmssh_hosts` to reset the host file.

### Quit
To quit, type `q` and press enter. Or use ctrl+c.

### Connect to a host
Type the number next that is to the host and press enter. 