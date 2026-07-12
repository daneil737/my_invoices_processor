#!/usr/bin/python3

import pdfplumber

def read_document(filename: str) -> list[str]:
	with pdfplumber.open(filename) as document:
		first_page = document.pages[0]
		text = first_page.extract_text().split("\n")
		return text


def extract_data(data_array: list[str]) -> dict:
	pass


def process_date(date: str):
	pass


def generate_summary():
	pass


def main():
	invoice_text = read_document("invoices/invoice_Frank Carlisle_49474.pdf")


if __name__ == '__main__':
	main()