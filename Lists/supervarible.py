class A:
    def __init__(self) -> None:
        self.var1=20
        self.name="Srikanth"
class B(A):
    def __init__(self) -> None:
        self.var1=30
        # super().__init__()
        self.name="valli"
        super().__init__()
K=A()
S=B()
print(S.name)
    