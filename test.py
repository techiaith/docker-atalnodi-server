import requests

URL = "http://localhost:5555/restore"

def test(raw_text):
    data = {'text': raw_text}
    response = requests.get(URL, params=data)
    return response.text

print (test("mae pwllheli yn dref yn gwynedd gogledd cymru ac mae llandrindod ym mhowys"))
print (test("beth yw'r dyddiad"))

