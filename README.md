# HTB - Nuclear Sale Walkthrough

This is a solution walkthrough to Nuclear on Hack The Box. Details on how the
solution functions are documented in comments in [solution.py](solution.py).

## Running the Walkthrough

### Linux

This tool uses tcpflow and python 3 for the purpose of readability only. This
could equally be accomplished with wireshark and commonly available online
tools for manipulating hex, byte arrays, and xor operations. First ensure
you have tcpflow available:

```bash
# Install with apt (or yum, dnf, etc)
apt-get install -y tcpflow
```

Then run the solution.py:

```bash
python3 solution.py
```

### Docker

Alternatively you can execute the demo in docker as follows:

```bash
docker build -t htb-nuclear-sale .
docker run --rm -it -v /path/to/challenge.pcap:/app/challenge.pcap temp
...output of the solution.py...
HTB{whatever_the_flag_is}
```
