all: primarythread secondarythread

primarythread: primarythread.cpp
	gcc primarythread.cpp -o primarythread `pkg-config --cflags --libs gtk+-2.0` -g

secondarythread: secondarythread.cpp
	gcc secondarythread.cpp -o secondarythread `pkg-config --cflags --libs gtk+-2.0` -g
