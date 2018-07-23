from datetime import datetime
import requests
import xmltodict
from flask import Flask, jsonify, request

app = Flask(__name__)

url = 'http://opendata-tr.ratp.fr/wsiv/services/Wsiv'

line_id_transco = {
    'metro': 'M',
    'rer': 'R',
    'sncf': None,
    'noctilienratp': 'BN',
    'busratp': 'B',
    'tram': 'BT'
}


def get_displayable_line(raw_line):
    return {
        "code": raw_line.get('ns1:code', {}).get('#text'),
        "codeStif": raw_line.get("ns1:codeStif", {}).get('#text'),
        "id": raw_line.get("ns1:id", {}).get('#text'),
        "name": raw_line.get("ns1:name", {}).get('#text'),
        "realm": raw_line.get("ns1:realm", {}).get('#text'),
        "reseau": raw_line.get('reseau')
    }


@app.route('/api/lines', defaults={'line_id': None})
@app.route('/api/lines/<string:line_id>')
def get_line_by_id(line_id):
    headers = {
        'content-type': 'text/xml',
        'SOAPAction': "urn:getLines"
    }
    if line_id is None:
        body = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
                <soapenv:Header/>
                <soapenv:Body>
                    <wsiv:getLines>
                    </wsiv:getLines>
                </soapenv:Body>
            </soapenv:Envelope>
        """
    else:
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
    if type(response) is list:
        return jsonify([get_displayable_line(l) for l in response])
    else:
        return jsonify(get_displayable_line(response))


@app.route('/api/nextMissions')
def get_next_missions():
    headers = {
        'content-type': 'text/xml',
        'SOAPAction': "urn:getMissionsNext"
    }
    station_name = request.args.get('stationName')
    line_id = request.args.get('lineId')
    sens = request.args.get('sens')
    body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
        <soapenv:Header/>
        <soapenv:Body>
            <wsiv:getMissionsNext>
                <wsiv:station>
                    <xsd:line>
                        <xsd:id>""" + line_id + """</xsd:id>
                    </xsd:line>
                    <xsd:name>""" + station_name + """</xsd:name>
                </wsiv:station>
                <wsiv:direction>
                    <xsd:sens>""" + sens + """</xsd:sens>
                </wsiv:direction>
            </wsiv:getMissionsNext>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    response = requests.post(url, data=body, headers=headers)
    response = xmltodict.parse(response.content)
    print(response)
    response = response.get('soapenv:Envelope').get('soapenv:Body').get('ns2:getMissionsNextResponse').get('ns2:return')
    return jsonify(response)


def get_remaining_time(mission):
    station_message = mission.get('stationsMessages')
    if type(station_message) is str:
        return station_message
    elif type(station_message) is list:
        return station_message[0]
    else:
        next_mission = datetime.strptime(mission.get('stationsDates')[0], '%Y%m%d%H%M')
        return next_mission.strftime('%H:%M')
        # return int((next_mission - datetime.now()).total_seconds() / 60.0)


@app.route('/api/arduino/nextMissions')
def get_next_missions_ready_for_display():
    headers = {
        'content-type': 'text/xml',
        'SOAPAction': "urn:getMissionsNext"
    }
    station_name = request.args.get('stationName')
    line_id = request.args.get('lineId')
    sens = request.args.get('sens')
    body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
        <soapenv:Header/>
        <soapenv:Body>
            <wsiv:getMissionsNext>
                <wsiv:station>
                    <xsd:line>
                        <xsd:id>""" + line_id + """</xsd:id>
                    </xsd:line>
                    <xsd:name>""" + station_name + """</xsd:name>
                </wsiv:station>
                <wsiv:direction>
                    <xsd:sens>""" + sens + """</xsd:sens>
                </wsiv:direction>
            </wsiv:getMissionsNext>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    response = requests.post(url, data=body, headers=headers)
    response = xmltodict.parse(response.content)
    response = response.get('soapenv:Envelope').get('soapenv:Body').get('ns2:getMissionsNextResponse').get('ns2:return')
    response = response.get('missions', [])
    response = [get_remaining_time(mission) for mission in response]
    return jsonify(sorted(response))


@app.route('/api/directions/<string:line_id>')
def get_directions_by_line_id(line_id):
    headers = {
        'content-type': 'text/xml',
        'SOAPAction': "urn:getDirections"
    }
    body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
        <soapenv:Header/>
        <soapenv:Body>
            <wsiv:getDirections>
                <wsiv:line>
                    <xsd:id>""" + line_id + """</xsd:id>
                </wsiv:line>
            </wsiv:getDirections>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    response = requests.post(url, data=body, headers=headers)
    response = xmltodict.parse(response.content)
    response = response.get('soapenv:Envelope').get('soapenv:Body').get('ns2:getDirectionsResponse').get('ns2:return')
    return jsonify(response)


@app.route('/api/stations', defaults={'station_id': None})
@app.route('/api/stations/<string:station_id>')
def get_station_by_id(station_id):
    headers = {
        'content-type': 'text/xml',
        'SOAPAction': "urn:getStations"
    }
    if station_id is None:
        station_name = request.args.get('stationName')
        if station_name is not None:
            body = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
               <soapenv:Header/>
               <soapenv:Body>
                  <wsiv:getStations>
                     <wsiv:station>
                        <xsd:name>""" + station_name + """</xsd:name>
                     </wsiv:station>
                  </wsiv:getStations>
               </soapenv:Body>
            </soapenv:Envelope>
            """
        else:
            body = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
               <soapenv:Header/>
               <soapenv:Body>
                  <wsiv:getStations>
                 </wsiv:getStations>
               </soapenv:Body>
            </soapenv:Envelope>
            """
        response = requests.post(url, data=body, headers=headers)
        response = xmltodict.parse(response.content)
        response = response.get('soapenv:Envelope').get('soapenv:Body').get('ns2:getStationsResponse').get(
            'ns2:return').get('stations')
        if type(response) is not list:
            response = [response]
        new_response = []
        for station in response:
            station['line']['rawId'] = station.get('line').get('id')
            new_id = line_id_transco.get(station.get('line').get('reseau').get('code'))
            try:
                if station.get('line').get('reseau').get('code') == "tram":
                    if station.get('line').get('reseau').get('code')[0].lower() == 't':
                        new_id += station.get('line').get('code', '').lower()[1:]
                    else:
                        new_id += station.get('line').get('code', '').lower()
                else:
                    new_id += station.get('line').get('code', '').upper()
                station['line']['id'] = new_id
                new_response.append(station)
            except Exception:
                return jsonify({'error': 'station id error'})
        response = new_response
    else:
        body = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsiv="http://wsiv.ratp.fr" xmlns:xsd="http://wsiv.ratp.fr/xsd">
           <soapenv:Header/>
           <soapenv:Body>
              <wsiv:getStations>
                 <wsiv:station>
                    <xsd:id>""" + station_id + """</xsd:id>
                 </wsiv:station>
              </wsiv:getStations>
           </soapenv:Body>
        </soapenv:Envelope>
        """
        response = requests.post(url, data=body, headers=headers)
        response = xmltodict.parse(response.content)
        response = response.get('soapenv:Envelope').get('soapenv:Body').get('ns2:getStationsResponse').get(
            'ns2:return').get('stations')

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
