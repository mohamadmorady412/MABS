class NotImplementedInSystem(Exception):
    def __init__(self, component_type: str, name: str):
        message = f"{component_type} '{name}' is not implemented in the system."
        super().__init__(message)
