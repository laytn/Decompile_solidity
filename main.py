import os
import subprocess
import re
from web3 import Web3
from web3.middleware import geth_poa_middleware

# network 설정
web3 = Web3(Web3.HTTPProvider('https://public-node-api.klaytnapi.com/v1/cypress'))

# 디컴파일러 설정
clear = lambda : os.system('clear')
clear()
env = os.environ
newpath = r'/home/{username}/.local/bin'+env['PATH']
env['PATH'] = newpath
Contract_bytecode = web3.eth.get_code(web3.toChecksumAddress("0x93dd4a0b32b1e6495ec943d541a6f52e3cbcb834")).hex()

# 바이트코드 디컴파일러
def decompile(contractbytecode):
#     ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    r = subprocess.check_output(['panoramix',tokenbytecode],universal_newlines=True)
#     r1 = str(ansi_escape.sub('', r))
    return r

print(decompile(Contract_bytecode))
