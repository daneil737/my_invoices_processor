#!/usr/bin/python3

import os
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import pdftotext


def read_document(filename: str) -> list[str]:
	pass


def split_data(data_array: list[str]) -> dict:
	pass


def process_date(date: str):
	pass


def generate_summary():
	pass


def main():


	templates = read_templates("./templates")
	data = extract_data("invoices/invoice_Frank Carlisle_49474.pdf", 
		templates=templates,
		input_reader=pdftotext)
	print(data)



if __name__ == '__main__':
	main()