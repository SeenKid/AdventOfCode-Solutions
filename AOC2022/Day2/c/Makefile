# AOC 2022 template makefile
EXE = day2 
OBJS = day2.o ../lib/libvec.o  
CC = g++
DEBUG = -g
WARN = -Wall -Wextra
CFLAGS = -I. $(DEBUG) $(WARN)
LIBS = 
.PHONY: clean

%.o: %.cpp
	$(CC) $(CFLAGS) -c -o $@ $<

$(EXE) : $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS) $(LIBS)

clean:
	rm -f $(EXE) $(OBJS)
