import myapp
import unittest
import os


class TestMyApp(unittest.TestCase):
    def test_appExists(self):
        app = myapp.Pythagorean()
        self.assertIsNotNone(app)

    def test_guiExists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        self.assertIsNotNone(gui)

    def test_widgetExists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children
        self.assertIsNotNone(widgets)
        self.assertEqual(len(widgets), 5)
        for i in widgets:
            self.assertIsNotNone(i)

    def test_assetsExist(self):
        cwd = os.getcwd()
        img1 = os.path.join(cwd, 'assets', "diagram.png")
        img2 = os.path.join(cwd, 'assets', "logo.png")
        self.assertEqual(os.path.isfile(img1), True)
        self.assertEqual(os.path.isfile(img2), True)

    def test_dictExists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        output = gui.pythagorean()
        self.assertIsInstance(output, dict)
        for key, val in output.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(val, str)

    def test_inputAB(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children
        [print(idx, val) for idx, val in enumerate(widgets[1].children)]
        inputA = widgets[1].children[4]
        inputB = widgets[1].children[2]
        inputA.text = '3'
        inputB.text = '4'
        output = gui.pythagorean()
        self.assertEqual(output, {"c": "5.0"})


if __name__ == '__main__':
    unittest.main()
