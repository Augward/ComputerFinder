# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:44:49 2025

@author: Augustin Ward
"""

class Product:
    
    def __init__(self, 
                 brand: str = None, name: str = None, style: str = "Laptop",
                 rating: float = 0, reviews: int = 0, price: int = None, listPrice: int = None, sale: int = 0,
                 size: float = None, resolutionW: int = 1920, resolutionH: int = 1080, refreshRate: int = 60,
                 keypad: bool = 0, webcam: bool = 0, backlit: bool = 0,
                 cpuBrand: str = None, cpu: str = None, gpuBrand: str = "NVIDIA", gpu: str = None,
                 ramType: str = None, ram: int = None, storageType: str = "SSD", storage: int = None,
                 url: str = None):
        
        # Basic product data
        self.brand = brand              # ex: Hp, Lenovo
        self.name = name                # ex: Victus 15, Ominbook X
        self.style = style              # ex: Only 3 options: Laptop, All in One, or Tower
        
        # Price and reviews
        self.rating = rating            # ex: 4.4, 3.4, 2
        self.reviews = reviews          # ex: 100, 2000
        self.price = price              # ex: 700 (.ceil)
        self.listPrice = listPrice      # ex: 800 (.ceil)
        self.sale = sale                # ex: 60 (% .floor)
        
        # Physical data
        self.size = size                # ex: 15.6 for Laptop, 25 tall for Tower
        self.resolutionW = resolutionW  # ex: 1920
        self.resolutionH = resolutionH  # ex: 1080
        self.refreshRate = refreshRate  # ex: 144, 60
        
        self.keypad = keypad            # ex: Yes, No
        self.webcam = webcam            # ex: Yes, No
        self.backlit = backlit          # ex: Yes, No
        
        # Hardware specs
        self.cpuBrand = cpuBrand        # ex: Intel, AMD
        self.cpu = cpu                  # ex: i7 14th gen, RYZEN 5 800
        self.gpuBrand = gpuBrand        # ex: NVIDIA, AMD
        self.gpu = gpu                  # ex: RTX 3060
        
        self.ramType = ramType          # ex: DDR5, DDR4
        self.ram = ram                  # ex: 16, 32, 64
        self.storageType = storageType  # ex: SSD, HDD
        self.storage = storage          # ex: 128, 512, 1000
                
        # URL of product page
        self.url = url                  # ex: www. ...


    # to string method
    
    # to dictionary method
    
    # personal rating system based off specs