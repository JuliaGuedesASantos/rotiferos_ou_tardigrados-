# <p align="center"> **Rotíferos ou Tardígrados?** 🔬🧠 </p>
## <p align="center"> Utilizando uma Rede Neural Convolucional (CNN) para a classificação de imagens de microscopia óptica </p>


**Autoras:** Júlia Guedes Almeida dos Santos & Lorena Ribeiro Nascimento

**Disciplina:**  ATP-303 - Redes Neurais e Algoritmos Genéticos 

**Orientador:** Dr. Daniel Roberto Cassar

![Status](https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge)
*** 
### Introdução 🔬🖼️
<p align= "justify">
Em resumo, esse repositório busca concentrar as atividades relacionadas a resolução da atividade 4.6 (Rede Neural Convolucional) da disciplina de "Redes Neurais e Algoritmos Genéticos", referente ao terceiro semestre do bacharelado em Ciência e Tecnologia da Ilum - Escola de Ciência. 
</p>

<p align= "justify">
Para esse trabalho, criamos um dataset - dividido em três conjuntos: treino, teste e validação - que contém imagens de Tardígrados e Rotíferos, os quais são dois seres invertebrados amplamente utilizados em análises biológicas e ecológicas. Rotíferos são organismos microscópicos utilizados em análises ecológicas e toxicológicas, por conta da sua sensibilidade físico-química a mudanças do ambiente. Já os tardígrados são seres de tamanho entre 3-5 mm, que possuem capacidade criptobiótica mediante estresses ambientais, permitindo alta resistência. Essa capacidade é foco de estudos na área de fármacos e terapias, além de análise ecológicas devido a resposta a mudanças ambientais.
</p>

<p align= "justify">
Todavia a distinção desses organismos em microscópicos óticos é dificultosa, devido a uma gama de fatores distintos, tais como: presença de liquens e diversos outros organismos semelhantas, posição, transparência e outros aspectos de visualização da imagem. Dessa forma, a identificação desses seres, em larga escala, apresenta-se como um desafio não trivial que pode ser otimizado por meio de técnicas de aprendizado de máquina. 
</p>

<p align= "justify">
Nesse contexto, iremos utilizar uma <em>Convolutional Neural Network</em> (CNN, do português, Rede Neural Convolucional) para buscar classificar essas imagens de microscopia óptica. Esse tipo de arquitetura é amplamente utilizado para a composição de redes em que há a necessidade de contexto entre as features apresentadas, como no caso de imagens. Para a composição da rede, o módulo Pytorch será utilizado e para a avaliação do modelo obtido, será calculada a acurácia e uma matriz de confusão referentes aos resultados optidos por meio do conjunto de teste.
</p>

### Pré-requisitos 📄
<p align= "justify">
Para utilizar os notebooks presentes nesse repositório, é necessário ter conhecimentos prévios de Python e redes neurais - especialmente no que se refere a biblioteca Pytorch -, bem como utilizar um editor de códigos dessa linguagem. Em editores, como o Visual Studio Code (VS Code), é possível clonar o repositório para maior praticidade na obtenção dos arquivos. Nos demais casos, os arquivos podem ser baixados diretamente do repositório.
</p>

Para rodar os arquivos, além da utilização da versão mais atual da linguagem Python (3.13), é preciso realizar a instalação das bibliotecas listadas abaixo nas seguintes versões:
```bash
pip install cv2==4.11.0.86
pip install matplotlib==3.10.1
pip install numpy==1.26.4
pip install skimage==0.25.2
pip install torch==2.5.1
pip install torchvision==0.20.1
pip install zipp==3.21.0
```

### Notebooks e demais arquivos 📓
Para a execução da tarefa proposta, os códigos foram divididos em dois notebooks:
<ul>
  <li> <strong> 4_6_1__Rotífero_ou_Tardígrado__Trabalhando_com_imagens </strong>: Nesse notebook, a partir do dataset <em>Rotiferos-tardigrados.zip</em> realizamos o aumento do dataset referente aos dados de treino por meio de técnicas de rotação e adição de ruído gaussiano. A partir desse processo, foi possível gerar o dataset <em>rotiferos_tardigrados_aumentado.zip</em></li>
  <li> <strong> 4_6_1__Rotífero_ou_Tardígrado__Trabalhando_com_imagens </strong>: Com o dataset criado no notebook anterior, treinamos uma Rede Neural Convolucional (CNN) por meio da biblioteca Pytorch. Além disso, para a avaliação do resultado, calculamos a acurácia e plotamos a matriz de confusão referentes ao conjunto de teste. </li>
</ul>
Além desses notebooks, ambos os datasets mencionados também se encontram postados no repositório.

### Contribuidores 👥

| GitHub | Contribuições |
|:-----|:--------------|
| [Júlia Guedes A. dos Santos](https://github.com/JuliaGuedesASantos) | Formação do dataset, treinamento da rede e criação do repositório |
| [Lorena Ribeiro Nascimento](https://github.com/lorena881) | Formação do dataset, treinamento da rede e comentários nos notebooks |
| [Daniel Roberto Cassar](https://github.com/drcassar) | Orientador |

### Referências 📚
[1] SCIENCE, ODSC-Open Data. Image Augmentation for Convolutional Neural Networks. Disponível em: <https://odsc.medium.com/image-augmentation-for-convolutional-neural-networks-18319e1291c>. Acesso em: 14 abr. 2025.

[2]Transformações geométricas: translação, rotação e reflexão. Toda Matéria. Disponível em: <https://www.todamateria.com.br/transformacoes-geometricas/>. Acesso em: 14 abr. 2025.

[3] YADAV, Amit. What is Gaussian Noise and Why It’s Useful? Disponível em: <https://medium.com/@amit25173/what-is-gaussian-noise-and-why-its-useful-b3c50dd14628>. Acesso em: 14 abr. 2025.

[5] O que são redes neurais convolucionais? | IBM. Disponível em: <https://www.ibm.com/br-pt/think/topics/convolutional-neural-networks>. Acesso em: 18 abr. 2025.

[6] POLONI, Katia. Redes neurais convolucionais. Disponível em: <https://medium.com/itau-data/redes-neurais-convolucionais-2206a089c715>. Acesso em: 18 abr. 2025.

[7] Convolutional Neural Network: Redes neurais convolucionais. IONOS Digital Guide. Disponível em: <https://www.ionos.com/pt-br/digitalguide/sites-de-internet/desenvolvimento-web/convolutional-neural-network/>. Acesso em: 18 abr. 2025.

[8] Training a Classifier — PyTorch Tutorials 2.6.0+cu124 documentation. Disponível em: <https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html>. Acesso em: 18 abr. 2025.

[9] HIEN, Dang Ha The. A guide to receptive field arithmetic for Convolutional Neural Networks. Medium. Disponível em: <https://blog.mlreview.com/a-guide-to-receptive-field-arithmetic-for-convolutional-neural-networks-e0f514068807>. Acesso em: 18 abr. 2025.
