from image_utils import load_image,edge_detection
from skimage.filters import median 
from skimage.morphology import ball 
from PIL import image 
lena=load_image('lena.jpg')
clean=median(lena, ball(3))
binary= l_edge > 100
edge_image = Image.fromarry(np.uint8(binary* 225))
edge_image.save('my_edges.png')
