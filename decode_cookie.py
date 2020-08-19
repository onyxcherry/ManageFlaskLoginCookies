import zlib

from itsdangerous import base64_decode

def decode(cookie: str) -> str:
    try:
        compressed = False
        payload = cookie

        if payload.startswith('.'):
            compressed = True
            payload = payload[1:]

        data = payload.split(".")[0]

        data = base64_decode(data)
        if compressed:
            data = zlib.decompress(data)

        return data.decode("utf-8")
    except Exception as e:
        return f'[Decoding error: {e}]'
        

cookie = '.eJwlzrkNwkAQAMBeLibY7z43Y-3tI0htHCF6xxLxJPMpex5xPsv2Pq54lP3lZSsdFxOCJWdgQEJdYNJ0yeCs7rcau0hI1qA6OkzkzoMBIbk18SSsuUBNPVS5LydAAxFX1IoqomlITDyVklImmndkG21KlDtynXH8N1S-P7i0LyI.XzztZw.69XSr95anbpcU_9uHkf9-HcQ4JQ'

print(decode(cookie))
