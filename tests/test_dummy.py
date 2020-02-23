class TestDummy:
    # This was written for two reasons:
    # 1.- Running Pytest from code functionality.
    # 2.- Verifying CircleCI jobs workflow working properly.
    def test_function_dummy(self):
        x = "dummy"
        assert "m" in x
