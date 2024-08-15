# ojp-soapui-tests
This is a repo contains different tests for OJP instances in Europe. The main focus is the Swiss servers  (seeh https://opentransportdata.swiss/de/)

# OJP 2.0
We have test cases for OJP 2.0.
In https://github.com/openTdataCH/ojp-soapui-tests/tree/main/ojp2-req-res-examples there is a pyhton program, that:
* downloads the develop branch of 
See also our API-Explorer: https://opentdatach.github.io/api-explorer2


# LinkingAlps
## How to sort
Add for each kind of system a folder and structure which match the OJP Router Structure with its subsystems. E.g. for the LinkingAlps project and its use cases for passive systems make sub folders like: "LinkingAlps/SBB passive server" or "LinkingApls/STA active server".

## Adding test cases
Make meaningful names for the file containing the testcase

## Remarks
The term active system is a server which integrates several passive system, which is referenced in the OJP specification as a distributed OJP router.

# Contact
If you have questions contact opendata@sbb.ch.
