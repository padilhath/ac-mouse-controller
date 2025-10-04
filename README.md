## 📖 Descrição

Este script tem como objetivo tornar a experiência de jogar **Assetto Corsa** utilizando **teclado e mouse** mais fluida e natural.
Ele faz uso das bibliotecas **FreePIE** e **vJoy** para emular um volante e pedais virtuais, convertendo os movimentos do mouse e teclas do teclado em eixos analógicos.

---

## ⚙️ Requisitos

Antes de executar o script, é necessário instalar:

1. **[FreePIE](https://andersmalmgren.github.io/FreePIE/)** – Ferramenta usada para interpretar entradas e enviar comandos para o vJoy.
2. **[vJoy](https://sourceforge.net/projects/vjoystick/)** – Driver de joystick virtual que recebe os eixos simulados.

---

## 🎮 Controles

| Função            | Entrada                       | Eixo / Botão vJoy |
| ----------------- | ----------------------------- | ----------------- |
| Direção           | Movimento horizontal do mouse | Eixo **X**        |
| Acelerador 100%   | **W**                         | Eixo **Y**        |
| Acelerador 66%    | **E**                         | Eixo **Y**        |
| Acelerador 33%    | **Q**                         | Eixo **Y**        |
| Freio 100%        | **S**                         | Eixo **Z**        |
| Freio 66%         | **D**                         | Eixo **Z**        |
| Freio 33%         | **A**                         | Eixo **Z**        |
| Embreagem         | **C**                         | Eixo **RX**       |
| Freio de mão      | **Espaço (Space)**            | Eixo **RY**       |
| Botão 1 (exemplo) | Clique esquerdo do mouse      | Botão **0**       |
| Botão 2 (exemplo) | Clique direito do mouse       | Botão **1**       |
| Bloquear cursor   | **Y**                         | — (toggle)        |

---

## 🛠️ Configurações Principais

No início do script, é possível ajustar os seguintes parâmetros:

```python
mouse_sensitivity = 10
throttle_increase_time = 100
throttle_decrease_time = 100
braking_increase_time = 100
braking_decrease_time = 100
hand_braking_increase_time = 50
hand_braking_decrease_time = 50
clutch_increase_time = 50
clutch_decrease_time = 50
```

* **mouse_sensitivity** — Ajusta o quanto o movimento do mouse afeta a direção.
* **increase/decrease_time** — Controla a suavidade de cada pedal. Valores maiores = resposta mais lenta e progressiva.

---

## 🚀 Como Usar

1. Abra o **FreePIE**.
2. Abra o script (File/Open) no FreePIE.
4. Rode o script (Script/Run Script) no FreePIE.
5. Abra o **Assetto Corsa** e configure os controles para usar o **vJoy Device** como volante e pedais.
