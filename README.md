# My invoices processor

This project is a simple invoices processor. Its goal is to read invoices pdf files (using python pdftotext library) and write information (such as invoice number, date and total due) into csv file. It also creates a log file which contains information about reading invoice and errors that occur.

The script uses a set of exemplary invoices which all share the same format. While this isn's very useful in case of reading invoices created by various companies (each can have its own template) this will work for invoices that are issued by one company (if my company would need automated repports of the invoices that they issue).

The project uses a below dataset containing sample invoices with fictional data.
https://github.com/femstac/Sample-Pdf-invoices

## Running the script

```
./main.py
```
or
```
python3 main.py
```
All invoices files have to be placed in "invoices" directory.
Project was created in Linux-based environment.

## Script features
- searches folder for pdf files with invoices
- reads document content into string
- reads invoices' data (number, date and total amount billed) using **regex**
- creates invoices summary
- creates logs
- uses functional programming paradigm (all functionalities are handled in functions, no side effects)

## Requirements
- pdftotext
- logging
