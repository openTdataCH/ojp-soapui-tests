# This folder contains tests for OJP 1.0 and OJP 2.0 for Switzerland
Andreas Glauser, Daniel Rubli, Thomas Odermatt, Christoph Lucas, Matthias Günter
Contact: opendata@sbb.ch

This is a repo contains different tests for OJP instances in Europe. The main focus is the Swiss servers  (see https://opentransportdata.swiss)


# OJP 2.0 SOAPUI
We have tests for SOAPUI: https://github.com/openTdataCH/ojp-soapui-tests/tree/main/Swiss-OJP-2.0
You need to add the necessary information directly to the global properties of your SOAPUI.

# LinkingAlps SOAPUI
## How to sort
Add for each kind of system a folder and structure which match the OJP Router Structure with its subsystems. E.g. for the LinkingAlps project and its use cases for passive systems make sub folders like: "LinkingAlps/SBB passive server" or "LinkingApls/STA active server".

## Adding test cases
Make meaningful names for the file containing the testcase

## Remarks
The term active system is a server which integrates several passive system, which is referenced in the OJP specification as a distributed OJP router.
We have test cases for OJP 2.0.
In https://github.com/openTdataCH/ojp-soapui-tests/tree/main/ojp2-req-res-examples there is a pyhton program, that:
* downloads the develop branch of 
See also our API-Explorer: https://opentdatach.github.io/api-explorer2


# Automated Request/Response tests
In the folder ojp2-req-res-examples we do some some generations of from given requests into responses with validation (and unfortunately validation errors).

[https://github.com/openTdataCH/ojp-soapui-tests/blob/main/ojp2-req-res-examples/README.md](https://github.com/openTdataCH/ojp-soapui-tests/tree/main/ojp2-req-res-examples)

# Contact
If you have questions contact opendata@sbb.ch.

# License
The programs here are made available as AGPL. The tests are made available as CC-BY-SA.
