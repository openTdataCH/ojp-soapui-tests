import os
import requests
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from lxml import etree
from zipfile import ZipFile

xmlschemafile="./repository/OJP-develop/OJP.xsd"
# Download entire branch from GitHub
url = 'https://github.com/VDVde/OJP/archive/develop.zip'
response = requests.get(url)
with open('repository.zip', 'wb') as file:
    file.write(response.content)

# Extract the downloaded zip file to a folder
with ZipFile('repository.zip', 'r') as zip_ref:
    zip_ref.extractall('repository')




# Create XML validation function
def validate_xml():
    xml_input = input_text.get("1.0", tk.END)
    try:
        schema_doc = etree.parse(xmlschemafile)
        print("schema parsed.")
        schema = etree.XMLSchema(schema_doc)
        print("schema made ready.")
    except etree.DocumentInvalid as e:
        print("XML could not be parsed:", e)
        exit(1)
    try:
        xml_doc = etree.fromstring(xml_input.encode('utf-8'))
    except (etree.DocumentInvalid, etree.XMLSyntaxError) as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"XML is not valid: {e}")
        result_text.config(state=tk.DISABLED)
    try:

        schema.assertValid(xml_doc)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "XML is valid against the XSD.")
        result_text.config(state=tk.DISABLED)
    except etree.DocumentInvalid as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"XML is not valid against the XSD: {e}")
        result_text.config(state=tk.DISABLED)


# Create GUI
window = tk.Tk()
window.title("XML Validation")
window.geometry("800x600")
title_label = tk.Label(window, text="OJP 2.0 Validation", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

desc_label = tk.Label(window, text="This is a tool for validating OJP 2.0 XML against the XSD schema.", wraplength=350)
desc_label.pack(pady=5)
input_label = tk.Label(window, text="XML Input:")
input_label.pack()

input_text = ScrolledText(window, height=8)
input_text.pack()

validate_button = tk.Button(window, text="Validate", command=validate_xml)
validate_button.pack()

result_label = tk.Label(window, text="Validation Result:")
result_label.pack()

result_text = ScrolledText(window, height=4, state=tk.DISABLED)
result_text.pack()

window.mainloop()
