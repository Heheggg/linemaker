all: run

run: main.py
	python main.py

clean:
	rm -f *.png  *.ppm *.pyc \
