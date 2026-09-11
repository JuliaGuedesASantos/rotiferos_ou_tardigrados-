# Bibliotecas para definição de diretório

import zipfile
import os

# Image Augmentation

from skimage import exposure
from skimage.util import random_noise
from skimage import transform
from cv2 import resize

import numpy as np
import shutil

# Image redimension

import torchvision.transforms as transforms
from PIL import Image

import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def augmentation(caminho):

    num_imagem = 0

    for i in os.listdir(caminho):

        img_path = os.path.join(caminho, i)

        # Considera apenas arquivos de imagem
        if not i.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        img = mpimg.imread(img_path)

        num_imagem += 1

        sorteio = random.choice([
            'gauss_noise',
            'horizontal',
            'vertical'
        ])

        if sorteio == 'gauss_noise':

            noise = random_noise(
                img,
                mode="gaussian",
                clip=True
            )

            imagem_final = noise

        elif sorteio == 'horizontal':

            imagem_final = np.fliplr(img)

        else:

            imagem_final = np.flipud(img)

        plt.imsave(
            f"{caminho}{num_imagem}_{sorteio}.png",
            imagem_final,
            cmap="gray"
        )


augmentation(
    caminho='Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/Treino/Tardigrados/'
)

augmentation(
    caminho='Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/Treino/Rotiferos/'
)


# Redimensionamento dos tardígrados

tardigrados = os.listdir(
    'Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/Treino/Tardigrados/'
)

pasta_saida_tardigrados = (
    'Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/'
    'Treino/imagens_redimensionadas/Tardigrados/'
)

os.makedirs(pasta_saida_tardigrados, exist_ok=True)

numero = 1

for arquivo in tardigrados:

    caminho_arquivo = (
        'Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/'
        f'Treino/Tardigrados/{arquivo}'
    )

    # Abre a imagem
    img = Image.open(caminho_arquivo)

    # Converte para RGB se estiver em RGBA ou outros modos
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Redimensiona com PyTorch
    resize_transform = transforms.Resize((32, 32))
    resized_img = resize_transform(img)

    # Salva na nova pasta
    resized_img.save(
        f'{pasta_saida_tardigrados}resized_image{numero}.jpg'
    )

    numero += 1


# Redimensionamento dos rotíferos

rotiferos = os.listdir(
    'Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/Treino/Rotiferos/'
)

pasta_saida_rotiferos = (
    'Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/'
    'Treino/imagens_redimensionadas/Rotiferos/'
)

os.makedirs(pasta_saida_rotiferos, exist_ok=True)

numero = 1

for arquivo in rotiferos:

    caminho_arquivo = (
        'Rotiferos-tardigrados - Extendido/Rotiferos-tardigrados/'
        f'Treino/Rotiferos/{arquivo}'
    )

    # Abre a imagem
    img = Image.open(caminho_arquivo)

    # Converte para RGB se estiver em RGBA ou outros modos
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Redimensiona com PyTorch
    resize_transform = transforms.Resize((32, 32))
    resized_img = resize_transform(img)

    # Salva na nova pasta
    resized_img.save(
        f'{pasta_saida_rotiferos}resized_image{numero}.jpg'
    )

    numero += 1


# Compactação do dataset completo

shutil.make_archive(
    "dataset_extendido",
    "zip",
    "Rotiferos-tardigrados - Extendido"
)