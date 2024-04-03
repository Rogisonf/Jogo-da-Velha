# Jogo da Velha Clássico em Python

![Texto alternativo](https://i.imgur.com/spSdF6j.png)

Bem-vindo ao reino nostálgico do clássico Jogo da Velha! Mergulhe neste simples, porém encantador jogo baseado em terminal, que revive as memórias de infância que todos nós guardamos com carinho. Aperfeiçoe sua estratégia e teste sua inteligência contra uma IA rudimentar que desafia tanto novatos quanto adeptos.

## Recursos

- **Jogabilidade Intuitiva**: Entre direto no jogo com prompts de terminal fáceis de seguir.
- **IA Inteligente**: Engaje com uma IA que faz movimentos aleatórios, simulando uma partida casual entre amigos.
- **Detecção de Vitória**: Lógica integrada para determinar o vencedor ou um empate, garantindo um resultado claro para cada partida.
- **Exploração de Movimentos**: Implementações exemplares de Busca em Largura (BFS) e Busca em Profundidade (DFS) para explorar os movimentos do jogo (um ponto de partida para uma IA mais complexa).

## Apresentação sobre o projeto
**[Clique aqui para visualizar a apresentação do projeto](https://www.canva.com/design/DAGBUaRaw5Y/SFM2qmeXUCTeG-ZAlLNB6w/edit?utm_content=DAGBUaRaw5Y&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)**

## Como Funciona

`TicTacToe` é uma classe Python que encapsula a essência do jogo:
- Mantém o estado do tabuleiro.
- Acompanha o vencedor atual.
- Permite que os jogadores façam movimentos e verifica a condição de vitória.

A jogabilidade é um loop de turnos onde o jogador humano insere um movimento e a IA responde com o seu, ambos ilustrados em um tabuleiro simples baseado em texto.

## Começando

- **[Clique aqui para acessar o repositorio](https://github.com/Rogisonf/Jogo-da-Velha)**

Aproveite um rápido jogo de Jogo da Velha durante sua pausa ou enquanto saboreia seu café da noite.

- **Jogue Contra a Máquina**: Execute o arquivo `jogo-da-velha.py` no seu ambiente Python para uma partida interativa contra o algoritimo.
- **Máquina vs Máquina**: Execute o arquivo `jogo-da-velha.ipynb` no seu ambiente de notebook (como Jupyter) para assistir a uma simulação de jogo onde duas IAs competem entre si.

## Contribuições

Interessado em explorar a profundidade estratégica do Jogo da Velha? Convidamos contribuições que aprimorem a complexidade e inteligência do nosso jogo! A utilização de grafos é crucial para entender e expandir as possibilidades dentro do jogo, permitindo a implementação de algoritmos avançados de busca e otimização de estratégias, como a aplicação de Minimax para uma IA desafiadora ou até mesmo a exploração de algoritmos de busca em largura (BFS) e busca em profundidade (DFS) para prever jogadas. Se você tem ideias ou habilidades em teoria dos grafos, algoritmos de busca, ou simplesmente deseja melhorar a experiência do usuário na interface do terminal, sua contribuição será muito bem-vinda. Vamos juntos tornar este projeto de Jogo da Velha uma referência em aplicação prática de conceitos computacionais avançados!

---

## Mergulhe no Código

Abaixo estão os componentes principais do projeto:

- **A Classe do Jogo**: Nossa classe `TicTacToe` é a espinha dorsal, lidando com o tabuleiro e verificando o fim do jogo.
- **Mecânica dos Movimentos**: Funções como `available_moves` e `make_move` são as engrenagens que movem a mecânica do jogo.
- **Exploração do Espaço de Estados**: Dê uma olhada na função `get_next_states` que oferece um vislumbre das futuras possibilidades do jogo.
- **Movimentos da IA**: Testemunhe a simplicidade da IA com `random_move`, e imagine como você pode expandi-la.
- **Loop de Jogo**: A função `play_game` é onde a mágica acontece, alternando turnos entre o jogador e a IA.

Para entender cada peça, confira o código bem comentado que guia você pela lógica e pelo fluxo.

---

## Teste do algoritimo
![Imgur](https://imgur.com/zlzwWN7.jpg)
![Imgur](https://imgur.com/j25BVYo.jpg)
![Imgur](https://imgur.com/6i3YTQn.jpg)


---

## Creditos

- Rogisonf
- Rlucas

---
