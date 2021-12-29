"""
Bloom Filter as Pokedex. 
Hash table but occasionally get
False positive hits
"""
import pyhash # noncypotraphic hash function availability
def main():
    # list of 0's and/or 1's
    bit_vector = [0]*20

    # Murrmur and FNV hash functions
    fnv = pyhash.fnv1_32()
    murmur = pyhash.murmur3_32()

    # calculate the output of FNV and MURMUR
    # hash functions for pika and charmander
    fnv_pika = fnv('Pikachu') % 20
    fnv_char = fnv('Charmander') % 20
    murmur_char = murmur('Charmander') % 20
    murmur_pika = murmur('Pikachu') % 20
    print(fnv_pika)
    print(fnv_char)
    print(murmur_char)
    print(murmur_pika)
    # add these results to bit vector as 1
    bit_vector[fnv_char] = 1
    bit_vector[fnv_pika] = 1
    bit_vector[murmur_char] = 1
    bit_vector[murmur_pika] = 1
    print(bit_vector)
    
    # now check if these results are in the bit-vector
    # when
    # a wild bulbasaur appears
    fnv_bulb = fnv("Bulbasaur") % 20
    murmur_bulb = murmur("Bulbasaur") % 20
    print(fnv_bulb)
    print(murmur_bulb)

    # In this case, we get that both are already in the bit_vector, so we
    # obtain a false positive

    # if either number was 0 in the bit vector we could say has not been seen.
    # the reason this hash table fails is because we only have a bit vector
    # of size 20! could easily make bit vector longer and not mod hashes by 20
    # to decrease rate of false positives.

if __name__ == "__main__":
    main()
