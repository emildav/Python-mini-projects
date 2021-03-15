class Network:

    network = {}

    def add_vertex(self, vertex):
        if vertex not in self.network:
            self.network[vertex] = []
        else:
            print('The vertex already exists')

    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)

        if vrtx1 in self.network and vrtx2 not in self.network[vrtx1]:
            self.network[vrtx1].append(vrtx2)
            self.network[vrtx2].append(vrtx1)
        elif vrtx2 not in self.network[vrtx1]:
            self.network[vrtx1] = [vrtx2]
            self.network[vrtx2] = [vrtx1]

    def display_edges(self):
        for key in self.network:
            values = ''
            for item in self.network[key]:
                values += str(item)  + ' '
            print(f'{key}: {values}')


    def display_vertices(self):
        edge_names = []

        for vrtx1 in self.network:
            edge_names.append(vrtx1.name)

        return edge_names


class WebPage:

    def __init__(self, name, link):
        self.name = name
        self.link = link
    
    def __str__(self):
        return self.name

link_one = WebPage('First Page', 'www.firstpage.com')
link_two = WebPage('Second Page', 'www.secondpage.com')
link_three = WebPage('Third Page', 'www.thirdpage.com')
link_four = WebPage('Fourth Page', 'www.fourthpage.com')

our_network = Network()

our_network.add_vertex(link_one)
our_network.add_vertex(link_two)
our_network.add_vertex(link_three)
our_network.add_vertex(link_four)

our_network.add_edge([link_one, link_two])
our_network.add_edge([link_one, link_three])
our_network.add_edge([link_three, link_four])
our_network.add_edge([link_one, link_two])

our_network.display_edges()
print(our_network.display_vertices())