import time

from project.pages.Main import MainPage
from project.pages.ElementsPage import ElementsPage
from project.pages.AlertsFrameWindowsPage import AlertsFrameWindowsPage
from project.pages.TexBoxPage import TextBoxPage
from project.utils.project_utils import RandomUtils

main = MainPage()
element_page = ElementsPage()
textbox_page = TextBoxPage()
alerts_frame_windows_page = AlertsFrameWindowsPage()

random_email = "test@test.com"
random_text = RandomUtils().get_random_text(8)


def test(set_up):
    main.button_element_click_()
    assert element_page.get_headers_page() == "Elements", 'Страница Elements не открыта'
    textbox_page.select_textbox_from_list()

    textbox_page.enter_full_name(random_text)
    textbox_page.enter_email(random_email)
    textbox_page.enter_current_address(random_text)
    textbox_page.enter_permanent_address(random_text)
    textbox_page.click_submit_button()
    assert textbox_page.is_display_error_email(), "Введеное значение в поле e-mail некорректно"

    full_name_actual_value = textbox_page.get_output_full_name()
    assert textbox_page.is_validate_output_full_name(
        random_text), f'Значение full name не соответствует ожидаемому.Ожидаемое значение: {random_text}, актуальное значение: {full_name_actual_value}'

    email_actual_value = textbox_page.get_output_output_email()
    assert textbox_page.is_validate_output_email(
        random_email), f'Значение e-mail не соответствует ожидаемому.Ожидаемое значение: {random_text}, актуальное значение: {email_actual_value}'

    current_address_actual_value = textbox_page.get_output_current_address()
    assert textbox_page.is_validate_current_address(
        random_text), f'Current address не соответствует ожидаемому.Ожидаемое значение: {random_text}, актуальное значение: {current_address_actual_value}'

    permanent_address_actual_value = textbox_page.get_output_permanent_address()
    assert textbox_page.is_validate_permanent_address(
        random_text), f'Permanent address full name не соответствует ожидаемому.Ожидаемое значение: {random_text}, актуальное значение: {permanent_address_actual_value}'

    element_page.click_button_element()
    alerts_frame_windows_page.alerts_frame_windows_click()
    alerts_frame_windows_page.select_browser_window_from_list()

    current_tab = alerts_frame_windows_page.get_current_tab()
    alerts_frame_windows_page.new_button_click()
    alerts_frame_windows_page.switch_to_last_tab()
    assert alerts_frame_windows_page.is_validate_open_new_tab(), 'Новая вкладка не была открыта'
    alerts_frame_windows_page.switch_to_new_tab(current_tab)
