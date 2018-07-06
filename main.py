import requests
import json
import logging
import db
import MySQLdb
from config import MAPS_API_KEY
from push_notification import push

logging.basicConfig(filename='/root/asu-traffic-report/logs/debug.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

logger=logging.getLogger(__name__)


def req(name,params):

    response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=params)

    try:

        response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=params)
        json_data = json.loads(response.text.encode('ascii', 'ignore').decode('ascii'))

        time_json = json_data['rows'][0]['elements'][0]

        logger.debug(time_json)
        #push(name,json.dumps(time_json))
        db.insert_data(name,json.dumps(time_json))

    except requests.exceptions.RequestException as err:
        logger.error(err)
        push("Requests Error",str(err))
    except ValueError:
        logger.error("Decoding JSON has failed")
        push("Error","Decoding JSON has failed")
    except MySQLdb.Error as err:
        logger.error(err)
        push("Mysql Error",str(err))

def asu_luque():

    params =[
        ('origins', '-25.289021, -57.590337'),
        ('destinations', '-25.267776, -57.489307'),
        ('departure_time','now'),
        ('key',MAPS_API_KEY)
    ]

    req('asu-luque',params)

    params[0] = ('origins', '-25.267776, -57.489307')
    params[1] = ('destinations', '-25.289021, -57.590337')

    req('luque-asu',params)


def asu_fdmora():

    params =[
        ('origins', '-25.289021, -57.590337'),
        ('destinations', '-25.326145, -57.548403'),
        ('units','imperial'),
        ('departure_time','now'),
        ('key',MAPS_API_KEY)
    ]

    req('asu-fdmora',params)

    params[0] = ('origins', '-25.326145, -57.548403')
    params[1] = ('destinations', '-25.289021, -57.590337')

    req('fdmora-asu',params)

def asu_lambare():

    params =[
        ('origins', '-25.289021, -57.590337'),
        ('destinations', '-25.342582, -57.614490'),
        ('units','imperial'),
        ('departure_time','now'),
        ('key',MAPS_API_KEY)
    ]

    req('asu-lambare',params)

    params[0] = ('origins', '-25.342582, -57.614490')
    params[1] = ('destinations', '-25.289021, -57.590337')

    req('lambare-asu',params)

def centro_villamorra():

    params =[
        ('origins', '-25.281669, -57.634689'),
        ('destinations', '-25.285546, -57.576954'),
        ('units','imperial'),
        ('departure_time','now'),
        ('key',MAPS_API_KEY)
    ]

    req('centro-villamorra',params)

    params[0] = ('origins', '-25.285546, -57.576954')
    params[1] = ('destinations', '-25.281669, -57.634689')

    req('villamorra-centro',params)



asu_luque()
asu_fdmora()
asu_lambare()
centro_villamorra()
