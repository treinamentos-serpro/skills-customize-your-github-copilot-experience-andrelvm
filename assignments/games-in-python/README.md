
# 📘 Assignment: Hangman Game

## 🎯 Objective

Construa um jogo da Forca em Python para praticar manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória.

## 📝 Tasks

### 🛠️ Implementar o jogo da Forca

#### Descrição
Crie um jogo em que o jogador tenta adivinhar uma palavra oculta informando uma letra por vez. O jogo deve atualizar o progresso e terminar quando a palavra for descoberta ou quando o limite de tentativas incorretas for atingido.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Solicitar palpites de letras ao jogador.
- Mostrar o progresso da palavra oculta usando letras reveladas e espaços, como `_ _ _ _`.
- Controlar e exibir a quantidade de tentativas incorretas restantes.
- Evitar que um palpite de letra repetido seja contado novamente.
- Encerrar quando o jogador adivinhar a palavra ou ficar sem tentativas.
- Exibir uma mensagem informando se o jogador venceu ou perdeu.

Exemplo de progresso:

```text
Palavra: _ _ _ _ _
Digite uma letra: a
Palavra: _ a _ _ _
Tentativas restantes: 5
```