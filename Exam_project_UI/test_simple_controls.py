
from Exam_project_UI.page_simple_controls import PageCheckElements


class TestCheckElements:

    def test_button_is_clickable(self, chrome):
        page = PageCheckElements(driver=chrome)
        page.open()
        page.check_button_is_clickable()
        assert page.check_page_url_after_click_button('button-success')

    def test_filling_fields(self,chrome):
        page = PageCheckElements(driver=chrome)
        page.open()
        page.filling_out_name_field()
        page.filling_out_email_field()
        page.click_email_me_button()
        assert page.check_result_after_filling_fields()
        print('Text result =',page.check_result_after_filling_fields())

    def test_radio_button(self,chrome):
        page = PageCheckElements(driver=chrome)
        page.open()
        page.select_radio_button('male')
        page.is_radio_button_selected('male')

    def test_check_box(self,chrome):
        boxes = ['Bike', 'Car']
        page = PageCheckElements(driver=chrome)
        page.open()
        page.select_check_boxes_from_list(boxes)

    def test_dropdown_menu(self,chrome):
        selected_value = 'Saab'
        page = PageCheckElements(driver=chrome)
        page.open()
        page.expand_dropdown_menu()
        page.select_element_from_dropdown_menu(selected_value)
        assert page.option_check(selected_value)
























