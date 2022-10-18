# not ransomware - is a simple python ransomware script

## What is not ransomware?
not ransomware is basically a ransomware script using sockets to communicate with the attacker and cyptography in python that enrypts all files in its dir are encrypted and with little changes all files that the script has access to can be encrypted also.

1. The server binds sockets together so that the client and nodes can connect.
2. After the node has connected it will run the encryption and all files in the dir will be encrypted
3. Then the key will be sent to the server and client
4. after that the client can specify the node then use the decrypt command to decrypt all encrypted files

## How to install and run?

How to install git for cloning

1. Install git
   ```sh
   sudo apt install git
   ```



Cloning using git.

1. Clone the repo
   ```sh
   git clone https://github.com/fluffydolphin/not-ransomware.git
   ```
   
2. Cd into not ransomware
   ```sh
   cd not-ransomware
   ```
   
2. Cd into server, client or node
   ```sh
   cd server
   ```
   ```sh
   cd client
   ```
   ```sh
   cd node
   ```
3. Run command for either server, client or bot
   ```sh
   python3 server
   ```
   ```sh
   python3 client
   ```
   ```sh
   python3 node
   ```
  
That's all it takes to install and run not-ransomware.

## Commands and Configuration for not ransomware
It is possible to modify the behaviour of not-ransomware with cli
arguments. In order to get an up-to-date help document, just run
`-h`.

you can change the server ip on the client and bot but not on the server, the default host ip on the server is 0.0.0.0 (localhost).

* -p, --port
* * Port of the Server, default 421


These commands are for after you have started HiveMind and adjusted the behaviour

* !help!
* * Shows you this
* !connected!
* * Shows you how many and which nodes are connected based on there number
* node_number!decrypt!
* * decrypts a specifc node
* !quit!
* * This is used for quiting either the client or the node (you have to use this or else you will get a broken pipe error) 
