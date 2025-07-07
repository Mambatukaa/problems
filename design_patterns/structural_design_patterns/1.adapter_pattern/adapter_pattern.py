""""
Summarized concept of the Adapter pattern
The adapter can be summarized as follows:

There’s a service that’s routinely accessed by an application (we’ll call it the Service Implementation).
This service implements some interface (which we’ll call Service Interface).
There’s an endpoint that needs to be accessed by the same part of the application that isn’t compatible with Service Interface.
To solve this problem, there’s an Adapter class, which implements Service Interface but has some internal translation functionality to access this incompatible endpoint.
For example, our application might be dealing with JSON data, but there’s still an endpoint that deals with XML. This endpoint can’t be changed because many other services depend on it. So, if we want to be able to use this endpoint in the JSON-based part of our application, we need an Adapter that will translate between XML and JSON.









"""
from abc import ABC, abstractmethod


# Base socket interface
class ElectricSocket(ABC):
    pass

# European socket interface
class EuropeanElectricSocket(ElectricSocket):
    @abstractmethod
    def connect_two_pins(self):
        pass


# British socket interface
class BritishElectricSocket(ElectricSocket):
    @abstractmethod
    def connect_three_pins(self):
        pass


# Concrete British socket
class ConcreteBritishSocket(BritishElectricSocket):
    def connect_three_pins(self):
        print("Triple-pin plug has been successfully connected.")


# Plug interface
class SocketPlug(ABC):
    @abstractmethod
    def select_socket(self, socket: ElectricSocket):
        pass

    @abstractmethod
    def connect_to_socket(self):
        pass


# Concrete European Plug
class EuropeanSocketPlug(SocketPlug):
    def __init__(self):
        self.european_socket: EuropeanElectricSocket | None = None

    def select_socket(self, socket: ElectricSocket):
        if not isinstance(socket, EuropeanElectricSocket):
            raise ValueError("Can only connect to European socket.")
        self.european_socket = socket

    def connect_to_socket(self):
        if self.european_socket:
            self.european_socket.connect_two_pins()
        else:
            print("No socket selected.")


# Adapter class
class SocketAdapter(EuropeanElectricSocket, SocketPlug):
    def __init__(self):
        self.british_socket: BritishElectricSocket | None = None

    def select_socket(self, socket: ElectricSocket):
        if not isinstance(socket, BritishElectricSocket):
            raise ValueError("Adapter can only connect to British socket.")
        self.british_socket = socket

    def connect_to_socket(self):
        if self.british_socket:
            self.british_socket.connect_three_pins()
        else:
            print("No socket connected.")

    def connect_two_pins(self):
        print("Double-pin plug has been successfully connected to the adapter.")





# Create British socket
british_socket = ConcreteBritishSocket()

# Adapter wraps British socket
adapter = SocketAdapter()
adapter.select_socket(british_socket)

# European plug connects to adapter
european_plug = EuropeanSocketPlug()
european_plug.select_socket(adapter)
european_plug.connect_to_socket()
adapter.connect_to_socket()

