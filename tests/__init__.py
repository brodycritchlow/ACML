from ACML import *

assert parse(r"C:\Users\brody\Documents\pyconf\tests\test1.config") == {'server': {'host': 'localhost', 'port': '8080', 'tls': {'enabled': True, 'certfile': '/path/to/cert.pem', 'keyfile': '/path/to/key.pem'}}}
