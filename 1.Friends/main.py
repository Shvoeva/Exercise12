from copy import copy

class Friends:
    def __init__(self, *connections):
        сonnections_with_repetition = list(connections[0] if len(connections) == 1 else connections)

        for connection in сonnections_with_repetition:
            connection_copy = copy(connection)
            assert len(connection_copy) == 2
            assert type(connection_copy.pop()) is str
            assert type(connection_copy.pop()) is str

        self.Connections = []
        for connection in сonnections_with_repetition:
            if connection not in self.Connections:
                self.Connections.append(connection)

    def add(self, connection):
        connection_copy = copy(connection)
        assert type(connection_copy) is set
        assert len(connection_copy) == 2
        assert type(connection_copy.pop()) is str
        assert type(connection_copy.pop()) is str

        if connection in self.Connections:
            return False
        else:
            self.Connections.append(connection)
            return True

    def remove(self, connection):
        connection_copy = copy(connection)
        assert type(connection_copy) is set
        assert len(connection_copy) == 2
        assert type(connection_copy.pop()) is str
        assert type(connection_copy.pop()) is str

        if connection in self.Connections:
            self.Connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        designations = copy(self.Connections[0])
        for connection in self.Connections:
            designations |= connection
        return designations

    def connected(self, name):
        assert type(name) is str

        connections_name = [connection for connection in self.Connections if name in connection]
        if not connections_name:
            return {}
        designations = copy(connections_name[0])
        for connection in connections_name:
            designations |= connection
        return designations.difference(name)

if __name__ == '__main__':
    f1 = Friends({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
    f2 = Friends([{"1", "2"}, {"3", "1"}])
    print(f2.add({"1", "3"}))
    print(f2.add({"4", "5"}))
    f3 = Friends([{"1", "2"}, {"3", "1"}])
    print(f3.remove({"1", "3"}))
    print(f3.remove({"4", "5"}))
    f4 = Friends({"a", "b"}, {"b", "c"}, {"c", "d"})
    print(f4.names())
    print(f4.remove({"d", "c"}))
    print(f4.names())
    f5 = Friends({"a", "b"}, {"b", "c"}, {"c", "a"})
    print(f5.connected("a"))
    print(f5.connected("d"))
    print(f5.remove({"c", "a"}))
    print(f5.connected("c"))
