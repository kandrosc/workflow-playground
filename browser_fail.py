from selenium import webdriver
import os
import sys

class ClassNotFoundError(Exception): pass


FILEPATH = os.path.dirname(os.path.abspath(__file__))+"/"

if __name__ == "__main__":
    