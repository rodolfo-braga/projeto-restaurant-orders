class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders = {}
        for order in self.orders:
            if order[0] == customer:
                if order[1] in orders:
                    orders[order[1]] += 1
                else:
                    orders[order[1]] = 1
        return max(orders, key=orders.get)

    def get_never_ordered_per_customer(self, customer):
        menu = set()
        ordered = set()
        for order in self.orders:
            menu.add(order[1])
            if order[0] == customer:
                ordered.add(order[1])
        return menu - ordered

    def get_days_never_visited_per_customer(self, customer):
        days_open = set()
        days_visited = set()
        for order in self.orders:
            days_open.add(order[2])
            if order[0] == customer:
                days_visited.add(order[2])
        return days_open - days_visited

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
