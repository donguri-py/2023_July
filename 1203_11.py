def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
d = {
    "entree": "beef",
    "drink": "ice coffee"
}

menu(**d)