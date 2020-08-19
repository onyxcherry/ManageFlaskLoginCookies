from hashlib import sha512

def create_cookie(remote_address: str, user_agent: str) -> str:
    
    base = f"{remote_address.encode('utf-8')}|{user_agent.encode('utf-8')}"
    h = sha512()
    h.update(base.encode('utf-8'))
    return h.hexdigest()

remote_address = '127.0.0.1'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

print(create_cookie(remote_address, user_agent))
