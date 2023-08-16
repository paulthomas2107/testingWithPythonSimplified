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


if __name__ == '__main__':
    unittest.main()
