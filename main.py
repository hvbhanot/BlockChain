import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        # Initialize the blockchain with the genesis block
        self.chain = []
        self.create_block(proof=1, prev_hash='0')

    def create_block(self, proof, prev_hash):
        # Create a new block and add it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'prev_hash': prev_hash
        }
        self.chain.append(block)
        return block

    def get_prev_block(self):
        # Get the previous block in the chain
        return self.chain[-1]

    def proof_of_work(self, prev_proof):
        # Perform the proof of work algorithm to find the new proof
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof ** 2 - prev_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        # Create a SHA-256 hash of a block
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        # Check if the blockchain is valid
        block_index = 1
        previous_block = chain[0]
        while block_index < len(chain):
            block = chain[block_index]
            if block['prev_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = chain[block_index]
            block_index += 1
        return True


# Mining the blockchain

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
blockchain = Blockchain()


@app.route("/mine_block", methods=['GET'])
def mine_block():
    # Endpoint to mine a new block
    prev_block = blockchain.get_prev_block()
    prev_proof = prev_block['proof']
    proof = blockchain.proof_of_work(prev_proof)
    prev_hash = blockchain.hash(prev_block)
    block = blockchain.create_block(proof, prev_hash)
    response = {
        'message': 'Congratulations!! You just mined a block.',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'prev_hash': block['prev_hash']
    }
    return jsonify(response), 200


@app.route("/get_chain", methods=['GET'])
def get_chain():
    # Endpoint to get the full blockchain
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


@app.route("/is_valid", methods=['GET'])
def is_valid():
    # Endpoint to check if the blockchain is valid
    is_present = blockchain.is_chain_valid(blockchain.chain)
    if is_present:
        response = {
            'message': 'The blockchain is valid'
        }
    else:
        response = {
            'message': 'The blockchain is not valid'
        }
    return jsonify(response), 200


# Run the Flask web server
app.run(host='0.0.0.0', port=5000)
