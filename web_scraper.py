import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def scrape_ecommerce(url, product_selector, name_selector, price_selector, rating_selector):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request was unsuccessful

        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Define lists to hold extracted data
        product_names = []
        prices = []
        ratings = []

        # Extract data from the page
        for product in soup.select(product_selector):
            name_element = product.select_one(name_selector)
            price_element = product.select_one(price_selector)
            rating_element = product.select_one(rating_selector)

            # Extract and clean data
            name = name_element.get_text(strip=True) if name_element else 'N/A'
            price = price_element.get_text(strip=True) if price_element else 'N/A'
            rating = rating_element.get_text(strip=True) if rating_element else 'N/A'

            product_names.append(name)
            prices.append(price)
            ratings.append(rating)

        # Create a DataFrame from the extracted data
        data = {
            'Product Name': product_names,
            'Price': prices,
            'Rating': ratings
        }
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        df.to_csv('products.csv', index=False)

        return "Data has been successfully extracted and saved to 'products.csv'."

    except requests.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"


def on_scrape_button_click():
    url = url_entry.get()
    product_selector = product_selector_entry.get()
    name_selector = name_selector_entry.get()
    price_selector = price_selector_entry.get()
    rating_selector = rating_selector_entry.get()

    if not url or not product_selector or not name_selector or not price_selector or not rating_selector:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    result = scrape_ecommerce(url, product_selector, name_selector, price_selector, rating_selector)
    messagebox.showinfo("Result", result)


def on_reset_button_click():
    url_entry.delete(0, tk.END)
    product_selector_entry.delete(0, tk.END)
    name_selector_entry.delete(0, tk.END)
    price_selector_entry.delete(0, tk.END)
    rating_selector_entry.delete(0, tk.END)


# Set up the GUI window
window = tk.Tk()
window.title("E-commerce Scraper")

# Create and place labels and entry fields
tk.Label(window, text="URL:").grid(row=0, column=0, padx=10, pady=5)
url_entry = tk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Product Selector:").grid(row=1, column=0, padx=10, pady=5)
product_selector_entry = tk.Entry(window, width=50)
product_selector_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Name Selector:").grid(row=2, column=0, padx=10, pady=5)
name_selector_entry = tk.Entry(window, width=50)
name_selector_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Price Selector:").grid(row=3, column=0, padx=10, pady=5)
price_selector_entry = tk.Entry(window, width=50)
price_selector_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="Rating Selector:").grid(row=4, column=0, padx=10, pady=5)
rating_selector_entry = tk.Entry(window, width=50)
rating_selector_entry.grid(row=4, column=1, padx=10, pady=5)

# Create and place the buttons
scrape_button = tk.Button(window, text="Scrape Data", command=on_scrape_button_click)
scrape_button.grid(row=5, column=0, columnspan=2, pady=10)

reset_button = tk.Button(window, text="Reset", command=on_reset_button_click)
reset_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI event loop
window.mainloop()
