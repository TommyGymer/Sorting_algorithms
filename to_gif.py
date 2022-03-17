import imageio
import glob
from pygifsicle import optimize
from alive_progress import alive_bar

things = [x for x in glob.glob(".\\output\\*.jpg")]

things.sort(key = lambda x: int(x.split("\\")[-1].split(".")[0]))

with alive_bar(len(things) + 30) as bar:
  with imageio.get_writer(".\\bubble.gif", mode="I", fps=60) as writer:
    for f in things:
      image = imageio.imread(f)
      writer.append_data(image)
      bar()
    for i in range(30):
      writer.append_data(imageio.imread(things[-1]))
      bar()

optimize(".\\bubble.gif")