""""
The Bridge design pattern allows us to separate the business logic from a software component that controls or triggers this business logic. For example, we might have a user interface that has multiple buttons. Each button triggers some logic in the backend. The Bridge design pattern allows us to separate the user interface with the buttons from the component that contains the actual business logic.

The main benefit of using the Bridge design pattern would be that it allows two separate teams to work independently on two application components. One team would be responsible for the user interface, and the other team would be responsible for the implementation of the business logic in the back-end. The teams can work independently as long as they have specified a shared interface definition.

Summarized concept of Bridge
The Bridge design pattern can be summarized as follows:

There are two objects: Interface and Implementation. They’re not to be confused with interfaces and classes. In this context, the object playing the role of Interface is actually a concrete class.
The Implementation object contains the main business logic, while the Interface object is designed to interact with all endpoints of the Implementation object.
The Implementation object depends on an interface (in the normal sense of object-oriented programming), so it can be easily mocked when the Interface object needs to be tested.
"""


from abc import abstractmethod, ABC


class IDataService(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def insert_data(self, item):
        pass


class DataService(IDataService):
    def __init__(self):
        self._data = []

    def get_data(self):
        return self._data

    def insert_data(self, item):
        self._data.append(item)



class BridgeInterface():
    def __init__(self):
        self.implementation: IDataService = None

    def get_data(self):
        if not self.implementation:
            print("no data")
            return 

        for item in self.implementation.get_data():
            print(item)


    def insert_data(self, item):
        self.implementation.insert_data(item)




bridgeInterface = BridgeInterface()


bridgeInterface.implementation = DataService()


bridgeInterface.insert_data(1)
bridgeInterface.insert_data(2)
bridgeInterface.insert_data(3)
bridgeInterface.insert_data(4)
bridgeInterface.get_data()
