# Top level makefile, the real shit is at src/Makefile

default: all

#.DEFAULT:
#	cd src && $(MAKE) $@ 
all:
	cd deps/linenoise && make
	cd deps/geohash-int && make
	cd deps/lua/src && make all
	cd deps/hiredis && make static && make
	cd deps/jemalloc && make
	cd src && $(MAKE) $@
clean:
	cd deps/linenoise && make $@
	cd deps/geohash-int && make $@
	cd deps/lua/src && make $@
	cd deps/hiredis && make $@
	cd deps/jemalloc && make $@
	cd src && $(MAKE) $@
install:
	cd src && $(MAKE) $@

.PHONY: install clean all
