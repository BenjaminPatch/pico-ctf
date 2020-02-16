import sys
sys.path.append('/home/benpa/pico-ctf/')

from pwn import asm
from pwn import shellcraft
from pwn import ssh

import password_reader

# Read my password from a file so I don't have to delete password when uploading
pw = password_reader.get_password();
pw = pw.split("\n")[0]

path = "/problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0"

ssh_client = ssh(host="2019shell1.picoctf.com", user="AlKanNot", password=pw)

sh = ssh_client.process("/bin/sh");
sh.sendlineafter("$", f"cd {path}");
sh.sendlineafter("$", "cat .cant_see_me");

sh.interactive()
