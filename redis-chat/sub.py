from conn import client
import sys

if __name__ == '__main__':
    channel = sys.argv[1]
    pubsub = client.pubsub()
    pubsub.subscribe(channel)

    print ('Listening to {channel}'.format(**locals()))

    while True:
        for item in pubsub.listen():
            print (item['data'])