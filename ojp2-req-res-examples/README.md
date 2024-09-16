# Request / Response validation for the Swiss OJP 2.0 service
Matthias Günter 2024, contact opendata@sbb.ch

The goal of the scripts here is to give some additional checks for the current SKI+ OJP 2.0 implementation.

It contains the following phyton scripts:
* extract_reqs.py - extracts the requests for OJP 2.0 from the ../SwissOJP2.0 soapui file and stores them in the examples folder 
* config.py - containing the configuration for extract_reqs
* actualize_req_res_ojp2.0.py - downloads the current XSD directly from the OJP repository and then starts validating and processing them
* xsd_valid_gui.py - gives you a simple GUI, where you can post an XML and it is validated.

## What is checked in the first three scripts
* The requests are checked against OJP XSD 2.0.
* The requests are transfered to the OJP 2.0 server from Switzerland.
* The responses are validated.

If there is a problem with a request, then a  *.err.req.txt file is stored with the problem
If there is a problem with a response, then a *.err.response.txt file is stored with the problem.

If request and response are present, then they are both valid and the response was provided by the server.

## Important note
Be aware that the OJP 2.0 is under active and rapid development at SKI+ for Switzerland.

## Resources
* OJP 2.0 github: https://github.com/VDVde/OJP
* OJP 2.0 openapi tester: https://opentdatach.github.io/api-explorer2/
* Swiss OJP server information: https://opentransportdata.swiss/de/dataset/ojp2-0
* Swiss OJP demonstrator for 2.0: https://tools.odpch.ch/ojp-demo-v2

## Bugtracker
https://github.com/openTdataCH/ojp-soapui-tests/issues 

## License
This software is provided as AGPL 3.0





