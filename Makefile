install:
	if [ $$USER = "root" ] ; then \
		cp bin/8080.py /usr/bin/; \
		chmod +x /usr/bin/8080.py; \
	else \
		echo "\e[0;31mYOU MUST BE ROOT"; \
		false; \
	fi;
uninstall:
	if [ $$USER = "root" ] ; then \
		rm -rf /usr/bin/8080.py; \
	else \
		echo "\e[0;31mYOU MUST BE ROOT"; \
		false; \
	fi;
test:
	bin/8080.py examples/memcpy
	if [ $$? -eq 0 ] ; then \
		true; \
	else \
		echo "\e[0;31mSomething went wrong..."; \
		false; \
	fi;
clean:
	rm -rf examples/*.rom
