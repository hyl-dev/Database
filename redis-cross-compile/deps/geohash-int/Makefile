ifndef CROSS_COMPILE
CROSS_COMPILE :=arm-linux-gnueabihf-
endif

STD=
WARN= -Wall
OPT= -O2

export CROSS_COMPILE

R_CFLAGS= $(STD) $(WARN) $(OPT) $(DEBUG) $(CFLAGS)
R_LDFLAGS= $(LDFLAGS)
DEBUG= -g

R_CC=$(CROSS_COMPILE)gcc $(R_CFLAGS)
R_LD=$(CROSS_COMPILE)gcc $(R_LDFLAGS)

all: geohash.o geohash_helper.o

.PHONY: all

geohash.o: geohash.h geohash.c
geohash_helper.o: geohash.h geohash_helper.h geohash_helper.c

.c.o:
	$(R_CC) -c $<

clean:
	rm -f *.o
