CC=g++
CFLAGS=-W -Wall -std=c++17 -pedantic

main: main.o cell.o maze.o settings.o
	$(CC) -o main main.o cell.o maze.o settings.o $(CFLAGS)

main.o: main.cpp cell.hpp maze.hpp settings.h
	$(CC) -o main.o -I. -c main.cpp $(CFLAGS)

maze.o: maze.cpp maze.hpp cell.hpp
	$(CC) -o maze.o -I. -c maze.cpp $(CFLAGS)

cell.o: cell.cpp cell.hpp settings.h
	$(CC) -o cell.o -I. -c cell.cpp $(CFLAGS)

settings.o: settings.cpp settings.h
	$(CC) -o settings.o -I. -c settings.cpp $(CFLAGS)


clean:
	rm -rf *.o *~ main
