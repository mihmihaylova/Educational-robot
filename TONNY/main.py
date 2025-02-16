from machine import Pin, PWM 
from time import sleep
import ubinascii
# functions for binary-to-text and text-to-binary conversions
from umqtt.simple import MQTTClient
import random
import lineRobo


MQTT_BROKER = "broker.hivemq.com"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
print(CLIENT_ID)
SUBSCRIBE_TOPIC = b"robot/mimi"

        
def sub_cb(topic, msg):
    data = msg.decode()
    if data == "next_mark":
        lineRobo.green()  
        lineRobo.next_mark()
    elif data == "wrongAnswer":
         lineRobo.red()
         lineRobo.buzzer()
    else:
        stop()
        lineRobo.lightTurnOff()
        
 
    
def reset():
    print("Resetting...")
    sleep(5)
    machine.reset()
    

def main():
    print(f"Begin connection with MQTT Broker :: {MQTT_BROKER}")
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    mqttClient.set_callback(sub_cb)
    mqttClient.connect()
    mqttClient.subscribe(SUBSCRIBE_TOPIC)
    print(f"Connected to MQTT  Broker :: {MQTT_BROKER}, and waiting for callback function to be called!")
    while True:
            # Non-blocking wait for message
            mqttClient.wait_msg()


if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()
















