from hashlib import sha256

def mine_bitcoins():
    MAX_NONCE = 100000000000
    difficulty = 6

    def SHA256(text):
        return sha256(text.encode("ascii")).hexdigest()

    def mine(block_number, transactions, previous_hash, prefix_zeros):
        prefix_str = '0' * prefix_zeros
        for nonce in range(MAX_NONCE):
            text = str(block_number) + transactions + previous_hash + str(nonce)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                #Successfully mined bitcoins
                return new_hash

        raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")

    transactions = '''
    Akshat->Saumya->60,
    Saumya->Samarth->90
    '''
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5, transactions, 'f40dd37a01d3fe6e999441a6918dc2c0cc048957661ce5a8c72e60cc64d09e13', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
    f = open('bitcoin_mining.txt', 'w')
    f.write(new_hash)
    f.close()
