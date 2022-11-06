# Atividade_LP2
Repositório do exercício da disciplina LP2

# Biblioteca Tkinter
A biblioteca Tkinter é uma biblioteca integrada que provê elementos para construção de interfaces gráficas para usuários (Graphical User Interface - GUI). Os elementos gráficos em si não são programados em Python, e a biblioteca é uma camada orientada a objetos posicionada sobre outra linguagem, a Tcl (Tool Command Language) e o sua caixa de ferramentas de interface gráfica, o Tk (conhecidos comumente como Tcl/Tk)
O uso desta biblioteca simplifica a criação de elementos gráficos de interface com o usuário final, como caixas de diálogo, botões, ícones, etc., tornando o programa mais amigável e fácil de utilizar ao usuário final, em oposição ao uso de uma CLI para entrada de dados e exibição de informações.
Apesar de não ser a única biblioteca GUI para Python, é uma das mais populares, tanto pela sua simplicidade, como pelo fato de ser uma biblioteca built-in (integrada) às versões mais recentes. Dessa forma, basta importar a biblioteca no programa em desenvolvimento, não sendo necessária a instalação de módulos externos. Após a importação, cada elemento gráfico (chamados de widgets) pode ser incluído em um módulo ou função. O Tkinter possui vinte elementos pré definidos para serem utilizados.
uso
Os widgets são criados em um estrutura hierárquica, que informa ao programa onde cada elementos deve estar localizado. Assim, um objeto root deve ser criado, que irá fornecer a base para a criação de outros elementos. Estes elementos estão estruturados em Frames, e cada objeto (botão, caixa de diálogo, outros frames) está associado a um objeto pai ou pode conter objetos filho. No exemplo retirado da documentação do tkinter:
from tkinter import *
 
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
 
leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "Hello world")
label.pack()
 
button1 = Button(leftframe, text = "Button1")
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Button2")
button2.pack(padx = 3, pady = 3)
button3 = Button(leftframe, text = "Button3")
button3.pack(padx = 3, pady = 3)
 
root.title("Test")
root.mainloop()

é criado um primeiro Frame ligado à raiz dos elementos (root). Em seguida, dois outros frames filhos deste primeiro são construídos: um à direita (rightframe) e um à esquerda (leftframe). Os elementos são criados como filhos de cada um dos frames: no caso da label (tarja) “Hello World”, diretamente no frame ligado ao root; no caso do botão 1 e 3, no leftframe e no caso do botão 2, no rightframe.

# Aplicação em um exercício prático:

Foi utilizado um programa simples, desenvolvido em aula, que gera a média de cinco números. Foi acrescentada uma interface gráfica que permite uma entrada de dados mais amigável ao usuários. Como um simples exemplo de aplicação, a resposta foi inserida em um novo quadro, sem preocupação de diagramação.
