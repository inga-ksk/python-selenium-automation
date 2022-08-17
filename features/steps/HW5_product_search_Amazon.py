from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
SEARCH_ITEM = (By.CSS_SELECTOR, 'div[cel_widget_id^="MAIN-SEARCH_RESULTS"]')
SEARCH_ITEM_NAME = (By.CSS_SELECTOR, 'div[cel_widget_id^="MAIN-SEARCH_RESULTS"] span.a-size-medium.a-color-base')
SEARCH_ITEM_IMAGE = (By.CSS_SELECTOR, 'div[cel_widget_id^="MAIN-SEARCH_RESULTS"] span[data-component-type="s-product-image"]')

@given('Open Amazon page')
def open_google(context):
    context.app.main_page.open_main()


@given('Open Amazon product page')
def open_amazon_product_page(context):
    context.app.main_page.open_url('gp/product/B074TBCSC8')


@when('Input {search_word} into Amazon search field and click search')
def input_search(context, search_word):
    # search = context.driver.find_element(*SEARCH_INPUT)
    # search.clear()
    # search.send_keys(search_word)
    context.app.header.search_product(search_word)

@when('Click on Amazon search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()

@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()


@when('Select department by value')
def select_department(context):
    context.app.header.select_dept()


@then('Product results for {search_word} are shown on Amazon')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"


@then('Every product has name')
def verify_found_results_feature_name(context):
    product_count = len(context.driver.find_elements(*SEARCH_ITEM))
    product_names_count = len(context.driver.find_elements(*SEARCH_ITEM_NAME))
    assert product_count == product_names_count, f"The search results are showing {product_count} items while {product_names_count} names are available"


@then('Every product has image')
def verify_found_results_feature_image(context):
    product_count = len(context.driver.find_elements(*SEARCH_ITEM))
    product_images_count = len(context.driver.find_elements(*SEARCH_ITEM_IMAGE))
    assert product_count == product_images_count, f"There are {product_count} search items available with {product_images_count} images present"

@then('Verify correct department is selected')
def verify_dept_matches_selected_value(context):
    context.app.header.get_act_dept()

@then('User sees the deals')
def verify_the_deals_appear_when_hover(context):
    context.app.header.new_arrivals_appear_on_hovering()

@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()