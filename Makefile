cgi_server: cgi_server.o task.o
	g++ cgi_server.o task.o -o cgi_server

pool_cgi.o: cgi_server.cpp processpool.h task.h
	g++ -c cgi_server.cpp -o cgi_server.o

task.o: task.h
	g++ -c task.cpp -o task.o

clean:
	rm *.o
	rm cgi_server