import imageio
import glob
from pygifsicle import optimize

things = [x for x in glob.glob(".\\output\\*.jpg")]

things.sort(key = lambda x: int(x.split("\\")[-1].split(".")[0]))

with imageio.get_writer(".\\bubble.gif", mode="I", fps=60) as writer:
  for f in things:
    image = imageio.imread(f)
    writer.append_data(image)
  for i in range(30):
    writer.append_data(imageio.imread(things[-1]))

optimize(".\\bubble.gif")