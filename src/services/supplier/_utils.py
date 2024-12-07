from selenium.webdriver import ChromeOptions


def add_downloading_driver_options(
        options: ChromeOptions,
        download_path: str
):
    options.add_experimental_option('prefs', {
        'download.default_directory': download_path,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })


def add_default_options_args(options: ChromeOptions):
    options.add_argument("--headless")
