"""
A solution to the 'Nuclear Sale' challenge on hack the box by David Cheeseman
"""
import os
import glob
import re

if not os.path.isfile('/target/challenge.pcap'):
    print("To run this demo challenge.pcap must be mounted to /target")
    exit(1)

os.system('tcpflow -r -o dump /target/challenge.pcap')

"""
Looking at the TCP streams in wireshark we can see there are 3 messages passed
that are 72 characters in the set 0-9 and a-f; so hex representations of bytes.
Let's grab those programatically (so I don't commit the actual hex string into
my gist).
"""
msgs = []
for f in glob.glob("dump/*"):
    matches = re.findall("[0-9a-fA-F]{72}", open(f).read())
    if len(matches) > 0:
        msgs += [bytes.fromhex(m) for m in matches]
print(msgs)

"""
So we have:

plaintext = ?

msgs[0] = plaintext ^ sales_key
msgs[1] = plaintext ^ management_key
msgs[3] = plaintext ^ management_key ^ sales_key

We need to isolate a single key, so remove plaintext and the other key in play.
As one can easily see, that is easily done by XORing msg_1 with msg_3

First cancel out plaintext:
(plaintext ^ sales_key) ^ (plaintext ^ management_key ^ sales_key)
Then cancel out sales_key:
(sales_key) ^ (management_key ^ sales_key)
Leaves the management key by iteself.
management_key
"""

def xor(msg1, msg2):
    return bytes([msg1[i] ^ msg2[i] for i in range(len(msg1))])

managment_key = xor(msgs[0], msgs[2])

"""
Since msg_2 is only encrypted with the management key we can xor it against the
key to get the plaintext.
"""

plaintext = xor(msgs[1], managment_key).decode()

"""
To no surprise, the plaintext will be the flag in the format of:
HTB{dont_use_xor_and_one_time_pads_multiple_time_also_this_isnt_the_flag}
"""
print(plaintext)
