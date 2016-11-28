from conn import client
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    channel = sys.argv[2]

    print ('Welcome to {channel}'.format(**locals()))

    while True:
        message = input('Enter one message: ')
        if message.lower() == 'exit':
            break
        message = '{name} says: {message}'.format(**locals())

        client.publish(channel, message)