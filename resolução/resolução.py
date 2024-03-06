import cv2
import numpy as np
import matplotlib.pyplot as plt

caminho_imagem = str(input("Insira o caminho para a imagem: "))
if caminho_imagem[0] == '"' and caminho_imagem[-1] == '"':
    caminho_imagem = caminho_imagem[1:-1]
try:
    with open(caminho_imagem, 'rb') as f:
        byte_content = f.read()
        nparray = np.frombuffer(byte_content, np.uint8)
        imagem = cv2.imdecode(nparray, cv2.IMREAD_COLOR)
except Exception as e:
    print("Falha ao carregar a imagem:", str(e))
    exit()


if imagem is not None:
    print("Largura:", imagem.shape[1])
    print("Altura:", imagem.shape[0])
else:
    print("Falha ao carregar a imagem. Verifique se o caminho está correto.")
