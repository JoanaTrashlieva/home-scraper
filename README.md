# Housing website scraper

This is a Python tool designed to automatically scrape multiple websites for housing listings in the Netherlands, specifically for new posts. It aims to simplify the process of finding available homes by aggregating data from various sources.

## Features

- Automated scraping: The tool automatically retrieves the latest housing listings from multiple websites, saving you time and effort.
- Multiple websites: It supports scraping from a variety of websites, allowing you to access a wide range of housing options.
- Customizable filters: You can customize the tool to filter listings based on your preferences, such as location, price range, and property type.
- Notification system: The tool can notify you when new listings that match your criteria are found, ensuring you don't miss out on any opportunities.
- Data visualization: It provides visualizations and statistics to help you analyze the housing market and make informed decisions.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/home-scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd home-scraper
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `config.py` file and customize the settings according to your preferences. You can specify the websites to scrape, filters to apply, and notification options.

2. Run the scraper:

    ```bash
    python scraper.py
    ```

    The tool will start scraping the specified websites and display the results in the console.

3. (Optional) If you want to receive notifications for new listings, make sure to configure the notification settings in `config.py`. You may need to set up additional dependencies or services for this feature to work.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.