from restClass import restCalls
import getpass


def get_example():
    """RESTconf example with GET"""
    username = 'username'
    password = 'password'
    ip_address_port = 'ip_address_port'

    rest_request = restCalls(username, password, ip_address_port)
    get_response = rest_request.get('bgp:bgp')
    print get_response


def put_example():
    """RESTconf example with PUT"""
    username = 'username'
    password = 'password'
    ip_address_port = 'ip_address_port'

    rest_request = restCalls(username, password, ip_address_port)
    with open('data.json', 'rb') as data_file:
        contents = data_file.read()
    put_response = rest_request(contents)
    print put_response.status_code


def patch_example():
    """REStconf example with PATCH"""
    username = 'username'
    password = 'password'
    ip_address_port = 'ip_address_port'

    rest_request = restCalls(username, password, ip_address_port)
    with open('data.json', 'rb') as data_file:
        contents = data_file.read()
    patch_response = rest_request(contents)
    print patch_response.status_code


def post_example():
    """REStconf example with POST"""
    username = 'username'
    password = 'password'
    ip_address_port = 'ip_address_port'

    rest_request = restCalls(username, password, ip_address_port)
    with open('data.json', 'rb') as data_file:
        contents = data_file.read()
    post_response = rest_request(contents)
    print post_response.status_code


def settings_config():
    """Configures the required settings to access the device"""
    ip_address = ""


def menu():
    """Prints a menu to the screen asking for user input until exit"""
