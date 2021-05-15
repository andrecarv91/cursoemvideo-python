from math import radians, cos, sin, tan
angulo = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {angulo:.1f} tem o SENO de {sin(radians(angulo)):.2f} \n'
      f'O ângulo de {angulo:.1f} tem o COSSENO de {cos(radians(angulo)):.2f} \n'
      f'O ângulo de {angulo:.1f} tem a TANGENTE de {tan(radians(angulo)):.2f}')
