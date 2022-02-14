import imageio
import glob
from pygifsicle import optimize

things = [x for x in glob.glob(".\\*.jpg")]

things.sort(key = lambda x: int(x.split("\\")[-1].split(".")[0]))

with imageio.get_writer("./bubble.gif", mode="I") as writer:
  for f in things:
    image = imageio.imread(f)
    writer.append_data(image)

optimize("./bubble.gif")