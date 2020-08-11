
import torch
import torchvision
from bento_service import AntOrBeeClassifier
from torch import nn
from torchvision import models


CLASSES = ['ant', 'bee']


def main():
    model = torch.load('ft_ant_bees.pt')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model_ft = models.resnet18(pretrained=True)
    num_ftrs = model_ft.fc.in_features
    model_ft.fc = nn.Linear(num_ftrs, len(CLASSES))

    model_ft.load_state_dict(model['model_state_dict'])
    model_ft = model_ft.to(device)

    bento_svc = AntOrBeeClassifier()
    bento_svc.pack('model', model_ft)
    saved_path = bento_svc.save()
    print('Bento Service saved in ', saved_path)


if __name__ == '__main__':
    main()
