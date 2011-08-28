all: primarythread secondarythread secondarythread_init

primarythread: primarythread.cpp
	gcc primarythread.cpp -o primarythread `pkg-config --cflags --libs gtk+-2.0` -g

secondarythread: secondarythread.cpp
	gcc secondarythread.cpp -o secondarythread `pkg-config --cflags --libs gtk+-2.0` -g

secondarythread_init: secondarythread_init.cpp
	gcc secondarythread_init.cpp -o secondarythread_init `pkg-config --cflags --libs gtk+-2.0` -g
