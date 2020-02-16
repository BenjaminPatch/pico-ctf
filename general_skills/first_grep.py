import sys
sys.path.append('/home/benpa/pico-ctf/')

from pwn import asm
from pwn import shellcraft
from pwn import ssh

import password_reader

# Read my password from a file so I don't have to delete password when uploading
pw = password_reader.get_password();
pw = pw.split("\n")[0]

path = "/problems/first-grep_0_93be1631acf1a93b98cdcc3e7b9fdc52"

ssh_client = ssh(host="2019shell1.picoctf.com", user="AlKanNot", password=pw)

sh = ssh_client.process("/bin/sh");
sh.sendlineafter("$", f"cd {path}");
sh.sendlineafter("$", "cat file | grep \"picoCTF{\"");

sh.interactive()
