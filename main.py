#!/usr/bin/env python
"""Sample assignment for students to fly a drone?"""

import logging
import logging.config
import time

import yaml
from tellopy import Tello


app_start_time = None


def config_logger():
    """Setup logging configuration"""
    path = 'logging.yaml'
    with open(path, 'rt') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    return logging.getLogger(__name__)


# Create module logger from config file
logger = config_logger()


def handler(sender, event, data, **args):
    """Handles event callbacks from Tello"""
    drone = sender
    if event is Tello.EVENT_FLIGHT_DATA:
        logger.debug(data)
    elif event is Tello.EVENT_CONNECTED:
        logger.info('Connected to Tello')
    elif event is Tello.EVENT_DISCONNECTED:
        logger.info('Disconnected from Tello')
        Tello.FLIGHT_EVENT


def main():
    # create an instance of the drone
    drone = Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
        drone.subscribe(drone.EVENT_CONNECTED, handler)
        drone.subscribe(drone.EVENT_DISCONNECTED, handler)

        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        time.sleep(3)
        drone.flip_forward()
        time.sleep(3)
        drone.flip_back()
        time.sleep(3)
        drone.down(50)
        time.sleep(3)
        drone.land()
        time.sleep(5)
    except Exception as ex:
        logger.exception(ex)
    finally:
        drone.quit()
        

if __name__ == '__main__':
    logger.info('Running')
    main()
    logger.info('Stopped')
