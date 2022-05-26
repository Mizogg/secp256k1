import secp256k1 as ice

with open("btc.txt") as file:
    add = file.read().split()
with open("rmd.txt", "w") as file:
    for x in add:
        file.write(ice.address_to_h160(x) + '\n')

ice.prepare_bin_file("rmd.txt", "btc_sorted.bin", True, True)