# Blockchain with Python and Flask

Welcome to my blockchain project! This project is a basic implementation of a blockchain using Python and Flask. It includes features such as block mining, chain validation, and a simple web interface to interact with the blockchain.

## Features

- **Blockchain Initialization:** Starts with a genesis block.
- **Mining Blocks:** Implements a proof-of-work algorithm to mine new blocks.
- **Chain Validation:** Ensures the integrity of the blockchain.
- **Web Integration:** Provides endpoints to mine blocks, retrieve the blockchain, and validate it through a Flask web server.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/blockchain-python-flask.git
    cd blockchain-python-flask
    ```

2. Install the required packages:
    ```bash
    pip install Flask
    ```

### Running the Application

1. Start the Flask web server:
    ```bash
    python blockchain.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

### API Endpoints

- **Mine a Block**
  - **URL:** `/mine_block`
  - **Method:** `GET`
  - **Description:** Mines a new block and adds it to the blockchain.

- **Get the Full Blockchain**
  - **URL:** `/get_chain`
  - **Method:** `GET`
  - **Description:** Retrieves the full blockchain.

- **Check Blockchain Validity**
  - **URL:** `/is_valid`
  - **Method:** `GET`
  - **Description:** Checks if the blockchain is valid.

## Example Requests

### Mine a Block

```bash
curl http://127.0.0.1:5000/mine_block
