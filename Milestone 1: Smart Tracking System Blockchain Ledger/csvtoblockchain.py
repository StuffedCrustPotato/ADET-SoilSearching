import pandas as pd
from web3 import Web3
import time

# Loading IoT data from csv
df = pd.read_csv("iot_data.csv")
df.columns = ["sensor_id", "temp", "humidity", "aqi", "soil_moisture", "soil_ph", "timestamp"]
# print(df.head())

# Connect to local Ganache blockchain
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if web3.is_connected():
    print("Connected web 3 is yay")
else:
    print("NOOOOOOOOOOOOOOOOOOO")

contract_adddress = "0x966811DAA91BF02F265cc560E071FF02a5a45f77"

abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "timestmap",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "sensorID",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "temperature",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "humidity",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "airQuality",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "soil_moisture",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "soil_ph",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "sensorTime",
				"type": "string"
			}
		],
		"name": "DataStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_sensorID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_temperature",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_humidity",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_airQuality",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_soil_moisture",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_soil_ph",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_sensorTime",
				"type": "string"
			}
		],
		"name": "storeData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "dataRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "sensorID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "temperature",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "humidity",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "airQuality",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "soil_moisture",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "soil_ph",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "sensorTime",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getRecord",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "MAX_ENTRIES",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

contract = web3.eth.contract(address = contract_adddress, abi = abi)

web3.eth.default_account = web3.eth.accounts[1]

print(f"Connected to start contract at {contract_adddress}")

def send_iot_data (sensorID, temperature, humidity, airQuality, soil_moisture, soil_ph, sensorTime):

    txn = contract.functions.storeData(sensorID, temperature, humidity, airQuality, soil_moisture, soil_ph, sensorTime).transact({
    'from': web3.eth.default_account,
    'gas': 3000000
    })

    reciept = web3.eth.wait_for_transaction_receipt(txn)
    print(f"Data stored {sensorID, temperature, humidity, airQuality, soil_moisture, soil_ph, sensorTime}, Txn Hash: {reciept.transactionHash.hex()}")


# for _, row in df.iterrows():
#     send_iot_data(
#         str(row["sensor_id"]),
#         str(row["temp"]),
#         str(row["humidity"]),
#         str(row["aqi"]),
#         str(row["soil_moisture"]),
#         str(row["soil_ph"]),
#         str(row["timestamp"])
#     )
#     time.sleep(1)  # Pause to avoid rate limits


total_records = contract.functions.getTotalRecords().call()
print(f"Total Records: {total_records}")

record = contract.functions.getRecord(0).call()
print("First stored Record:", record)

(
    timestamp,
    sensorId,
    temperature,
    humidity,
    airQ,
    soil_moisture,
    soil_ph,
    sensortime
) = record

print("\nFirst Stored Record (decoded):")
print(f"  Timestamp (Unix): {timestamp}") # This is a Unix timestamp
print(f"  Sensor ID: {sensorId}")
print(f"  Temperature: {temperature}°C") # Divide by 10
print(f"  Humidity: {humidity}%")
print(f"  Air Quality Index: {airQ} (AQI)")
print(f"  Soil Moisture: {soil_moisture}")
print(f"  pH: {soil_ph}") # Divide by 10
print(f" Sensor_Timestamp: {sensortime}")
