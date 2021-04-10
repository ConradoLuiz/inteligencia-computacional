# Relatório Fuzzy Logic - Controle do Guindaste


###### Grupo: Conrado Luiz, Luiza Guedes, Marcelo Barros, Igor Feital



### 1. Mudança na forma dos conjustos nebulosos de retas para curvas

​		Para realizar a mudança da forma dos conjuntos, basta clicar em cada variável de entrada, entrar em cada termo, conforme a figura abaixo, e mudar o tipo curva de linear para *spline*:

![image-20210323222825160](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210323222825160.png)

![image-20210323222842321](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210323222842321.png)

Após fazer isso para todas os termos, teremos os seguintes conjuntos:

![image-20210323230629920](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210323230629920.png)

![image-20210323230727279](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210323230727279.png)

​		Após feita a mudança em apenas 1 das variáveis, o controlador Fuzzy não conseguiu controlar o guindaste corretamente, deixando o controlador muito impreciso por conta das curvas nas funções. Após feita a mudança das curvas nas duas variáveis, o controlador ficou bastante impreciso, demorando muito mais tempo para conseguir posicionar o guindaste na posição adequada. No final da simulação, ele ainda não consegue deixar o guindaste com 0 de distância da plataforma.

![image-20210323232902561](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210323232902561.png)

### 2. Aumento e diminuição (de maneira uniforme) dos domínios dos conjuntos fuzzy de cada variável

​		Para fazermos o aumento ou diminuição do domínio dos conjuntos, basta abrirmos a janela de cada variável e alterar os conjuntos clicando e arrastando os pontos. Também é possível clicar no *mu* para ajustar os valores mais precisamente.

![image-20210324235859941](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210324235859941.png)

![image-20210324235947410](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210324235947410.png)

​		Após ajustar os domínios, eles ficaram da seguinte maneira:

![image-20210325000231289](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325000231289.png)

​																												Angulo

![image-20210325000424141](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325000424141.png)

​																											Distância

​		Na variável do angulo, o conjunto *neg_big* e *pos_big* foram diminuidos, e os conjuntos *neg_small* e *pos_small* foram aumentados. Na variável Distância, os conjuntos *neg_close* e *far* foram diminuidos, os conjuntos *zero* e *medium* foram aumentados, e o conjunto *close* foi movido para a direita.

![image-20210325001356081](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325001356081.png)

​		As alterações realizadas não aprimoraram o controlador de guindaste. É possível observar que o guindaste não consegue coloca-lo corretamenta em cima da plataforma, ainda ficando com -1.29 de distância dela.

### 3. Mudança no banco de regras(retirar, substituir e acrescentar regras)

​		Para realizar alterações no banco de regras do sistema Fuzzy, é necessário clicar duas vezes no *Rule Block* para abrir a janela de alterar o banco de regras:

![image-20210325001819392](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325001819392.png)

​		Em relação as alterações, a seguinte regra denotada de vermelho foi deletada: ![image-20210325003050601](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325003050601.png)

​		A remoção dessa regra causou o controlador do guindaste não retornar após ele passar um pouco da plataforma. O sistema termina assim, com -3.26 de distância da plataforma:

![image-20210325010755273](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325010755273.png)

​		Após isso, a seguinte regra foi adicionada:![image-20210325010950885](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325010950885.png)

Fazendo com que o controlador do guindaste passe da plataforma e continue dando força, dessa forma destruindo o guindaste:

![image-20210325011156888](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325011156888.png)

​		Em seguida, a seguinte regra foi alterada, de forma que o controlador não passe da plataforma. A saída da força foi alterada de *pos_medium* para *zero*:

![image-20210325020423298](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325020423298.png)

​		Dessa forma fazendo com que o guindaste termine na posição da figura abaixo e não coloque o container na plataforma.

![image-20210325020612536](C:\Users\conrado\AppData\Roaming\Typora\typora-user-images\image-20210325020612536.png)

### 4. Alteração dos métodos de implicação e composição

### 5. Alteração dos métodos de defuzificação

