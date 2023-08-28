import tkinter as tk
from tkinter import ttk
from tkinter import Label, Entry
import urllib.request
from html.parser import HTMLParser
import ssl

# a SSL context is created that doesn't verify certificates
ssl_context = ssl._create_unverified_context()

# this class parses and extracts data from HTML content 
class MyHTMLParser(HTMLParser):

# the constructor initalizes the class object, and within it
# the HTMLParser constructor is called to be initalized as well
# an instance of a list called "data" is also created 
    def __init__(self):
        super().__init__()
        self.data = []

# this method handles the text in the HTML content when parsing 
# occurs; the updated data (sans surrounding whitespace) is added to 
# the data list 
    def handle_data(self, data):
        self.data.append(data.strip())

# tnis method scrapes the url to display the content on it, based on which option
# the user chooses
def scrape_and_display():

# the url line is retrieved from the entry field using get()
    url = url_entry.get()  

# the url is opened and the HTLML content is fetched for
# context is involved with the SSL context to handle not 
# verifying cerificates
    response = urllib.request.urlopen(url, context=ssl_context)

# the HTML content from the response is read for raw data
    html_content = response.read()

# an instance of the MyHTMLParser class is made using the variable parser 
# to extract data from the HTML content, and said content is decoded using
# UTF-8 encoding 
# the parsing process starts here 
    parser = MyHTMLParser()
    parser.feed(html_content.decode('utf-8'))

# the user's dropdown is retrieved again with the use of get()
    selected = selected_option.get()

# if <strong> is selected, each paragrpah wrapped in <strong> tags is displayed 
    if selected == '<strong>':
        scraped_content = '\n'.join([f"<strong>{paragraph}</strong>" for paragraph in parser.data])

# if <p class="aclass bclass> is selected, each paragrpah wrapped in 
# <p class="aclass bclass> tags is displayed  
    elif selected == '<p class="aclass bclass">':
        scraped_content = '\n'.join([f"<p class='aclass bclass'>{paragraph}</p>" for paragraph in parser.data])

# if <p id="someid"> is selected, each paragrpah wrapped in <p id="someid"> 
# tags is displayed
    elif selected == '<p id="someid">':
        scraped_content = '\n'.join([f"<p id='someid'>{paragraph}</p>" for paragraph in parser.data])
    
# if full content is selected, all the scraped HTML content is displayed  
    else:
        scraped_content = '\n'.join([f"'{paragraph}'" for paragraph in parser.data])

# the exisiting text_widget is cleared and the formatted extracted HTML content is 
# inserted into the text widget
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, scraped_content)

# a tkinter window is created with its title
root = tk.Tk()
root.title('Web Scraping with Tkinter')

# the user prompted with the url entry box that's labeled: "Enter URL"
url_label = Label(root, text='Enter URL:')
url_label.pack()
url_entry = ttk.Entry(root)
url_entry.pack()

# the dropdown menu is created 
options = ['<strong>', '<p class="aclass bclass">', '<p id="someid">', 'Full Content']
selected_option = tk.StringVar(value=options[0])
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)
dropdown.pack()

# a text widget to display all the scraped content is created 
text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack()

# a buttom to start the scraping process and print its findings is created
scrape_button = tk.Button(root, text='Scrape', command=scrape_and_display)
scrape_button.pack()

# the tkinter even loop is started 
root.mainloop()
