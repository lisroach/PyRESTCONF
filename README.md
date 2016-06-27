# PyRESTCONF
##### Author: Lisa Roach
##### Email: lisroach@cisco.com

## Description:

This repository contains a module for making RESTconf calls with python. 

You must add your ip address, port, username, and password for the 
constructor.

### Usage:


For PUT, POST, and PATCH, you must have a configuration of JSON or XML
formatted using a valid YANG model. If your device does not have the YANG
model available, you will not be able to use it. Examples of YANG models can be
found here:

OpenConfig: [https://github.com/openconfig/public]


YangModels: [https://github.com/YangModels/yang]

For GET and DELETE you must know the name of the YANG module and container that
you wish the make changes too. 

```
#JSON

json_rest_object = JSONRestCalls(ip_address, port, username, password)
response_put = json_rest_object.put(data, 'yang_endpoint:container')
response_get = json_rest_object.get('yang_endpoint:container')

#XML

xml_rest_object = XMLRestCalls(ip_address, port, username, password)
response_put = xml_rest_object.put(data, 'yang_endpoint:container')
response_get = xml_rest_object.get('yang_endpoint:container')

```
### Examples:

```
#GET (same for DELETE)

rest_object = JSONRestCalls('127.0.0.1', 80, admin, admin)
response = rest_object.get('yang_module:container')
print response.content # prints the GET object as a string
print response.json() # prints the GET object as a dictionary
print response.status_code # prints the status code of the response
print response.reason # prints the reason for the status code

```

```
#PUT (works same for POST and PATCH)

rest_object = JSONRestCalls('127.0.0.1', 80, admin, admin)
response = rest_object.put(data, 'bgp:bgp')
print response.status_code
print response.reason # prints the reason for the status code

```


