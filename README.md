# TMSSH

TMSSH is a command line SSH manager. It's very basic but useful.

## Usage

To start tmssh, type `tmssh` into a shell. It'll then ask for a command.

## Commands

- `a`

Adds a server to tmssh. It will then ask for the username@server, such as
`user@192.168.0.1`. You can also add any extra arguments here.

After adding a server, it will be assigned a number. Type this number into
the command prompt and it will connect to that server.

Servers are stored in `~/.ssh/tmssh_hosts` with one server per line.

- `r`

Removes a server. Either type it's number or full name to delete it.

- `q`

Quits TMSSH.