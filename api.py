import requests
import xmltodict

url = 'http://opendata-tr.ratp.fr/wsiv/services/Wsiv'


def get_line_by_id(l_id):
    if l_id is None:
        return None
    elif type(l_id) is int:
        line_id = str(int(l_id))
    else:
        line_id = str(l_id)
    headers = {
        'content-type': 'text/xml',
        'SOAPAction': "urn:getLines"
    }
    body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
       <soapenv:Header/>
       <soapenv:Body>
          <wsiv:getLines>
             <!--Optional:-->
             <wsiv:line>
                <xsd:id>""" + line_id + """</xsd:id>
             </wsiv:line>
          </wsiv:getLines>
       </soapenv:Body>
    </soapenv:Envelope>
    """

    response = requests.post(url, data=body, headers=headers)
    response = xmltodict.parse(response.content)
    response = response.get('soapenv:Envelope').get('soapenv:Body').get('ns2:getLinesResponse').get('ns2:return')
    return {
        "code": response.get('ns1:code', {}).get('#text'),
        "codeStif": response.get("ns1:codeStif", {}).get('#text'),
        "id": response.get("ns1:id", {}).get('#text'),
        "name": response.get("ns1:name", {}).get('#text'),
        "realm": response.get("ns1:realm", {}).get('#text'),
        "reseau": response.get('reseau')
    }
