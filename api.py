from bottle import get, route,run,request
from examples.lib.ec2 import get_volumes
from examples.lib.ec2 import get_instances
from examples.lib.ec2 import get_vpcs
from examples.lib.ec2 import put_tagInstance

@get('/instances')
def instances():
    instances=get_instances()
    return instances

@get('/volumes')
def volumes():
    volumes=get_volumes()
    return volumes

@get('/vpcs')
def vpcs():
    vpcs=get_vpcs()
    return vpcs


@route('/name', method='POST')
def name():
    username = request.json('Username') + "\n"
    return  username

@route('/tag', method='POST')
def tag():
    username = request.json('Username') + "\n"
    put_tagInstance(username)

    return  username


run(host='localhost', port=8080, debug=True,reloader=True)

