
import functools


if __name__ == "__main__":
    class Hero:
        DEFAULT_NAME = "Superman"
        def __init__(self):
            self.name = Hero.DEFAULT_NAME
 
        def rename(self, new_name):
            self.name = new_name

        reset_name = functools.partialmethod(rename, DEFAULT_NAME)
 
        def __repr__(self):
            return f"Hero({self.name!r})"

    hero = Hero()
    assert hero.name == "Superman"
    hero.rename("Batman")
    print(hero)
    assert hero.name == "Batman"
    hero.reset_name()
    print(hero)
    assert hero.name == "Superman"
    print(hero)

    