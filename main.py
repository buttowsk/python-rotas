import matplotlib.pyplot as plt
import numpy as np

pontos = [{"id": 1, "x": -1.198, "y": -5.164},
          {"id": 2, "x": 5.573, "y": 7.114},
          {"id": 3, "x": -6.614, "y": 0.072},
          {"id": 4, "x": -7.374, "y": -1.107},
          {"id": 5, "x": -9.251, "y": 8.321},
          {"id": 6, "x": 6.498, "y": -6.036},
          {"id": 7, "x": 0.861, "y": 6.903},
          {"id": 8, "x": 3.904, "y": -5.261},
          {"id": 9, "x": 7.976, "y": -9.000},
          {"id": 10, "x": -2.61, "y": 0.039},
          {"id": 11, "x": 4.487, "y": 7.142},
          {"id": 12, "x": 8.938, "y": -4.388},
          {"id": 13, "x": -4.17, "y": -9.09},
          {"id": 14, "x": 7.835, "y": -9.269},
          {"id": 15, "x": 2.792, "y": -7.944},
          {"id": 16, "x": 5.212, "y": 9.271},
          {"id": 17, "x": 6.687, "y": 6.731},
          {"id": 18, "x": -2.19, "y": -9.21},
          {"id": 19, "x": -1.06, "y": 8.752},
          {"id": 20, "x": 6.883, "y": 0.882}]

central_point = {"id": 0, "x": 0, "y": 0}
pontos.append(central_point)


def generate_route(points):
    # Ponto central
    central_point = {"id": 0, "x": 0, "y": 0}

    # Adiciona o ponto central como o ponto atual
    current_point = central_point

    # Cria uma lista para armazenar a rota
    route = [current_point]

    # Remove o ponto central da lista de pontos
    points.remove(central_point)

    # Enquanto ainda houver pontos na lista de entrada, continua adicionando o ponto mais próximo à rota
    while len(points) > 0:
        # Calcula as distâncias entre o ponto atual e todos os pontos restantes
        distances = [np.linalg.norm([current_point['x'] - p['x'], current_point['y'] - p['y']]) for p in points]

        # Encontra o índice do ponto mais próximo e o adiciona à rota
        nearest_idx = np.argmin(distances)
        nearest_point = points.pop(nearest_idx)
        route.append(nearest_point)

        # Define o ponto mais próximo como o novo ponto atual
        current_point = nearest_point

    # Adiciona o ponto central novamente para completar o ciclo
    route.append(central_point)

    return route


def plot_route(route):
    # Separa as coordenadas x e y de todos os pontos na rota
    x = [p['x'] for p in route]
    y = [p['y'] for p in route]

    # Plota os pontos usando a função scatter, com tamanho 100 e cor azul
    plt.scatter(x, y, s=80, color='blue')

    # Plota as linhas que conectam os pontos, com cor verde
    labels = ['Inicio']
    for i in range(len(route) - 1):
        p1 = route[i]
        p2 = route[i + 1]
        if i == 0:
            # Ponto inicial é vermelho
            plt.scatter(p1['x'], p1['y'], s=300, color='salmon', marker='D', label='Inicio')
            color = 'red'
        elif i == len(route) - 2:
            color = 'green'  # Última linha é verde
            labels.append('Fim')
        else:
            color = 'black'  # Linhas intermediárias são pretas
            labels.append('')
        plt.plot([p1['x'], p2['x']], [p1['y'], p2['y']], color=color, label=labels[i])

    # Mostra o gráfico
    plt.legend()
    plt.show()


rota = generate_route(pontos)
plot_route(rota)
