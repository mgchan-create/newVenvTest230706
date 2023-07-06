import logging

logs = logging.getLogger()
logs.setLevel(logging.INFO)

fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(fmt)
# logs.addHandler(streamhandler)
# logs.info("......")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a, sep='\n', end='\n')
print(*a, sep='\n', end='')
