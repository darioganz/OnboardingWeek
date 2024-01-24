# Ethereum Price Alert Bot

This script continuously monitors the price of Ethereum and sends out a console alert whenever the price exceeds a predefined threshold. In this case its set to 2000 usd.

## Prerequisites

Before running this script, you will need Python 3.x installed on your system. 
Additionally, this script requires the `requests` module to perform HTTP requests to the CoinGecko API for fetching the current Ethereum price. 

## Installation

1. Clone the repository or download the script to your local machine.

2. Install the required Python modules using pip: "pip3 install requests"


## Usage

Run the script.


## Configuration

You can modify the following variables in the script according to your needs:

- `threshold_price`: Set this to the price at which you want to receive an alert.
- `check_interval`: Set how often (in seconds) you want the script to check the Ethereum price.

## Features

- Fetches the current Ethereum price from CoinGecko's API.
- Compares the current price to a user-defined threshold.
- Prints a fun alert message to the console if the price exceeds the threshold.




