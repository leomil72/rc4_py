
# RC4 STREAM CIPHER

## What is it?
The RC4 is a stream cipher originally developed by Ron Rivest while in RSA Security in 1987.
Although it was kept secret, a description of the algorithm was circulated on the Cyberpunks
mailing list and later on a public newsgroup a code appeared that gave the same results as
the algorithm known as RC4. From that moment the algorithm spread rapidly and became public
knowledge. despite this fact, for years both Rivest and RSA itself never confirmed that the
code in circulation was indeed that of RC4. Only in 2014 did Rivest confirm that the circulating
code does indeed belong to RC4.

The algorithm is a stream cipher that accepts as input a key up to 256 bytes long. From this
key it generates a keystream that is then used for the actual encryption. Since it is a stream
cipher with a symmetric key, decryption of a ciphertext is done by the same procedure.

## Warranty
The software is provided "AS IS" without any warranty, either expressed or implied,
including, but not limited to, the implied warranties of merchantability and fitness
for a particular purpose. The author will not be liable for any special, incidental,
consequential or indirect damages due to loss of data or any other reason.

## Security
The algorithm is not cryptographically secure: it was hacked many years ago and is proposed
here for academic purposes only. If your priority is security, turn to other algorithms certified
as cryptographically secure by national or international government agencies.

## License
This software is released under the terms of the GNU General Public License v3.0 or later