class MaClasse:
    pass

a = MaClasse()
print(f"Info sur 'a' : {a}")

# Info sur 'a' : <__main__.MaClasse object at 0x7f76d1f38170>

b=a
print(f"Info sur 'b' : {b}")

# Info sur 'b' : <__main__.MaClasse object at 0x7f76d1f38170>

b=MaClasse()
print(f"Info sur 'b' : {b}")

# Info sur 'b' : <__main__.MaClasse object at 0x7f76d1f380e0>
