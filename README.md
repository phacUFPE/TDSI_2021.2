# TDSI_2021.2

## Introduction
Project developed using Flask and SQLite to analyse the transfer of process to another server(s) when the default server be unavailable.

## Requirements
Python >=3.8
Pip >=21.3.1

After the repository cloned and the requirements satisfied you will be able to setup the project.

## Setup
### Backend
1. Go to the `backend` folder in the project folder.
2. Run the following command to install the dependencies:
```
pip install -r requirements.txt
```
3. Make sure that the `init_server.sh` file has permission. You can grant permission by running the command:
```
chmod 777 init_server.sh
```
**NOTE:** Before running the script make sure that the ports 5050 and 5055 are not being used by crucial system. They will be killed by the script.

4. To start the servers you need to run the `init_server.sh` file. You can run with:
```./init_server.sh ```
6. After running the script it gonna open two terminal's, one for each port.
7. Go to frontend setup.

### Frontend
1. Go to the `frontend` folder in the project folder.
2. Run the following command to install the modules:
```
npm install
```
3. After finished you can run the frontend using the command:
```
npm run serve
```
4. When the server is up, access the `http://localhost:8080` and try to add a product.

**NOTE:** After trying to add a new product, you will see that the terminal with the server in port 5050 will be killed and unavailable, but the product was inserted.
The product was insert because the frontend try to add in the default server, if it is not available, it will try to add in the backup server, that is the server in the port 5055.
