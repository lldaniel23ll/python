# progressbar en consola
from tqdm import tqdm

loop =tqdm(total = 5000,position = 0,leave = True)

for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)

loop.close()