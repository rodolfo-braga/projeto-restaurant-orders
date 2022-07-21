import csv


def get_orders_by_customer(data, customer):
    return set([row['pedido'] for row in data if row['cliente'] == customer])


def get_days_by_customer(data, customer):
    return set([row['dia'] for row in data if row['cliente'] == customer])


def get_max_order_by_customer(data, customer):
    orders = {}
    for row in data:
        if row['cliente'] == customer:
            if row['pedido'] in orders:
                orders[row['pedido']] += 1
            else:
                orders[row['pedido']] = 1
    return max(orders, key=orders.get)


def count_order(data, customer, order):
    counter = 0
    for row in data:
        if row['cliente'] == customer and row['pedido'] == order:
            counter += 1
    return counter


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão inválida: {path_to_file}')
    try:
        with open(path_to_file, 'r') as f:
            fieldnames = ['cliente', 'pedido', 'dia']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            data = list(reader)

            # Qual o prato mais pedido por 'maria'?
            prato_mais_pedido_maria = get_max_order_by_customer(data, 'maria')

            # Quantas vezes 'arnaldo' pediu 'hamburguer'?
            arnaldo_hamburguer = count_order(data, 'arnaldo', 'hamburguer')

            # Quais pratos 'joao' nunca pediu?
            pratos = set(row['pedido'] for row in data)
            pedidos_joao = get_orders_by_customer(data, 'joao')
            pratos_nunca_pedido_joao = pratos - pedidos_joao

            # Quais dias 'joao' nunca foi à lanchonete?
            dias_aberto = set([row['dia'] for row in data])
            dias_joao = get_days_by_customer(data, 'joao')
            dias_nunca_visitado_joao = dias_aberto - dias_joao

            with open('data/mkt_campaign.txt', 'w') as f:
                f.write(f'{prato_mais_pedido_maria}\n')
                f.write(f'{arnaldo_hamburguer}\n')
                f.write(f'{pratos_nunca_pedido_joao}\n')
                f.write(f'{dias_nunca_visitado_joao}')
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')


if __name__ == '__main__':
    analyze_log('./data/orders_1.csv')
