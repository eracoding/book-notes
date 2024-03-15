from torchvision import models, transforms
from PIL import Image

import torch

# print(dir(models))

alexNet = models.AlexNet()
resnet = models.resnet101(pretrained=True)

# print(resnet)

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])

img = Image.open('./dog.png')

img_t = preprocess(img)

batch_t = torch.unsqueeze(img_t, 0)

resnet.eval()

out = resnet(batch_t)

with open('./imagenet_classes.txt', 'r') as f:
    labels = [line.strip() for line in f.readlines()]

_, index = torch.max(out, 1)

softmax = torch.nn.functional.softmax(out, dim=1)

percentage = softmax[0] * 100
print(index[0])
print(labels[index[0]], percentage[index[0]])

_, indices = torch.sort(out, descending=True)
print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])
