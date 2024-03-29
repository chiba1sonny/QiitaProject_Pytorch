#tensorboard
#from torch.utils.tensorboard import SummaryWriter
from tensorboardX import SummaryWriter
writer = SummaryWriter("logs")
for i in range(100):
    writer.add_scalar("y=2x", 2*i, i)

#transforms
from PIL import Image
from torchvision import transforms
# transforms is a tool box
img_path = "dataset/train/ants_image/0013035.jpg"
img = Image.open(img_path)
print(img)
tensor_trans = transforms.ToTensor()
tensor_image = tensor_trans(img)
print(tensor_image)

#Totensor_tensorboard
trans_tensor = transforms.ToTensor()
img_tensor = trans_tensor(img)
print(img)
writer = SummaryWriter("logs1",img_tensor)
writer.add_image("Totensor", img_tensor)
writer.close()

#open tensorboard by terminal
tensorboard logdir=logs/logs1
