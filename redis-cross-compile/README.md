This README is just a fast *quick start* document. You can find more detailed documentation at http://redis.io.
I modify the redis-3.0.7 for  makefile  ，in order to make cross-compile for arm platform, during making, if you don‘t modify makefile ，the deps of jmelloc will be error ,you just modify  the cross-compile tools as your own in the Makefile ，and run "make" command ,you
will obtain the redis-cli and redis-server and so on.
