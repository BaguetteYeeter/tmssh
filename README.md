# TMSSH

TMSSH is a command line SSH manager. It's very basic but useful.

## Installation

Use `pip install tmssh`.

## Usage

To start tmssh, type `tmssh` into a shell. It'll then ask for a command.

After exiting a server, it'll bring you back to the menu, and you can use 
either `ctrl+c`, `ctrl+d`, or `q` to exit it.

Servers are stored in `~/.ssh/tmssh_hosts` with one server per line. It uses
this format: `username@host arguments (comment)`

## Commands

- `a`

Adds a server to tmssh. It will then ask for the username@server, such as
`user@192.168.0.1`. You can also add any extra arguments here. It'll then ask
you to add an optional comment. This can be used for memorable server names.

After adding a server, it will be assigned a number. Type this number into
the command prompt and it will connect to that server.

- `r`

Removes a server. Type it's number to delete it.

- `q`

Quits TMSSH.

## FAQ

### Why is this better than plain ssh commands?

It remembers all your IP adresses, and it's much faster to type `tmssh↵1↵` than
it is to type `ssh username@192.168.0.101`.

### Why is this better than other ssh managers?

It's so simple it can't go wrong, it works in every command line, and doesn't
need a GUI and a subscription (this'll be free forever!).

### How do I edit a server?

I could make it built-in, but it's easier for you to just edit the hosts file.
(see commands/a)

### Can I change the colours?

Sure, however you have to edit the code, and in a future release it'll be 
easier.

### Your code sucks, I want to improve it.

Please do.

## Changelog

### 0.3

- Added server comments
- Improved README