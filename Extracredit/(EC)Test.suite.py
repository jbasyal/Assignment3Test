import unittest
Login_site=__import__("(EC)login")
Edit_Customer = __import__("(EC)EditCustomer")
Customer_Summary = __import__("(EC)CustomerSummary")
Delete_Customer = __import__("(EC)DeleteCustomer")
Add_Product = __import__("(EC)AddProduct")
Edit_Product = __import__("(EC)EditProduct")
Delete_Product = __import__("(EC)DeleteProduct")
Add_Service = __import__("(EC)AddService")
Edit_Service = __import__("(EC)EditService")
Delete_Service = __import__("(EC)DeleteService")




loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Login_site))
suite.addTests(loader.loadTestsFromModule(Edit_Customer))
suite.addTests(loader.loadTestsFromModule(Customer_Summary))
suite.addTests(loader.loadTestsFromModule(Delete_Customer))
suite.addTests(loader.loadTestsFromModule(Add_Product))
suite.addTests(loader.loadTestsFromModule(Edit_Product))
suite.addTests(loader.loadTestsFromModule(Delete_Product))
suite.addTests(loader.loadTestsFromModule(Add_Service))
suite.addTests(loader.loadTestsFromModule(Edit_Service))
suite.addTests(loader.loadTestsFromModule(Delete_Service))



runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)