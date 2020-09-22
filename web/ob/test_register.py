from web.ob.main import Main


class TestRegister:
    def setup(self):
        self.main = Main

    def test_register(self):
        assert "ss" == self.main.goto_login().goto_register()


if __name__ == "__main__":
    pass
