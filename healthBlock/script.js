Web3 = require('web3')
fs = require('fs')
web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
code = fs.readFileSync('HealthcareContract.sol').toString()
solc = require('solc')
compiledCode = solc.compile(code)
abiDefinition = JSON.parse(compiledCode.contracts[':HDataAccessManager'].interface)
HealthContract = web3.eth.contract(abiDefinition)
byteCode = compiledCode.contracts[':HDataAccessManager'].bytecode
deployedContract = HealthContract.new({data: byteCode, from: web3.eth.accounts[0], gas: 4700000})

deployedContract.address
contractInstance = HealthContract.at(deployedContract.address)

contractInstance.addUser('Sukhbir',{from: web3.eth.accounts[0]})
contractInstance.totalUsers.call()