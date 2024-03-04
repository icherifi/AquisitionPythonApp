from pylsl import StreamInlet, resolve_stream


def main():
    # first resolve a marker stream on the lab network
    print("looking for a out stream...")
    streams = resolve_stream('name', 'OutStream')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        print("got %s at time %s" % (sample, timestamp))


if __name__ == '__main__':
    main()