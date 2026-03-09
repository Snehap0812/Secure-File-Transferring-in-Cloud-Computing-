from Crypto.PublicKey import ECC
import os

os.makedirs("keys", exist_ok=True)

key = ECC.generate(curve="P-256")

private_key = key.export_key(format="PEM")
public_key = key.public_key().export_key(format="PEM")

with open("keys/ecc_private.pem", "wt") as f:
    f.write(private_key)

with open("keys/ecc_public.pem", "wt") as f:
    f.write(public_key)

print("ECC Keys Generated Successfully")