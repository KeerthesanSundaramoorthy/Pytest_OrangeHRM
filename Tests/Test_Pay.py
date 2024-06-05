import pytest
from Pages.PayGradePage import PayGradePage
from Utility import Excel_Reader

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("paygrade",Excel_Reader.get_data("E:\\Pytest_OrangeHRM\\Excel_Files\\Pay_Grade.xlsx","Sheet1"))
class TestPay:
    #@pytest.mark.valid
    def test_add_paygrade(self,paygrade):
        pay = PayGradePage(self.driver)
        pay.valid_login()
        pay.pay_functions()
        pay.add()
        pay.paygrade(paygrade[0])
        pay.click_save()
        pay.assert_pay()