import scrapy
import os
import json

def Run():
    os.system("scrapy runspider scrapper.py -o neat.json")
if __name__ == "__main__":
    Run()
