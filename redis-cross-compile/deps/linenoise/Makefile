
ifndef CROSS_COMPILE
CROSS_COMPILE :=arm-linux-gnueabihf-
endif

STD=
WARN= -Wall
OPT= -Os

R_CFLAGS= $(STD) $(WARN) $(OPT) $(DEBUG) $(CFLAGS)
R_LDFLAGS= $(LDFLAGS)
DEBUG= -g

export CROSS_COMPILE

R_CC=$(CROSS_COMPILE)gcc $(R_CFLAGS)
R_LD=$(CROSS_COMPILE)gcc $(R_LDFLAGS)

linenoise.o: linenoise.h linenoise.c

linenoise_example: linenoise.o example.o
	$(R_LD) -o $@ $^

.c.o:
	$(R_CC) -c $<

clean:
	rm -f linenoise_example *.o
