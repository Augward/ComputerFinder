# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:44:49 2025

@author: Augustin Ward
"""


from datetime import datetime
from typing import Optional, Dict
import json


class Computer:
    def __init__(self,
            # Basic Info
            brand: Optional[str] = None,                                       # ex: Hp, Lenovo
            name: Optional[str] = None,                                        # ex: Victus 15, Ominbook X
            style: str = "Laptop",                                             # Only 3 options: Laptop, All-in-One, or Tower
            
            # Reviews & Price
            rating: float = None,                                               # 0.0 - 5.0
            reviews: int = 0,                                                  # review count
            
            price: Optional[int] = None,                                       # integer in dollars
            msrp: Optional[int] = None,                                        # manufacturer's suggested retail price
            sale: int = 0,                                                     # percent off, 0 - 100
            
            # Size & Screen
            weight: Optional[float] = None,                                    # pounds (lb)
            dimensions: [Optional[float], Optional[float], Optional[float]] = 
                            [None, None, None],                                # Length, Width, Thickness iches (in)
            
            screen: Optional[float] = None,                                    # diagonal (in), None for Tower
            resolution: [int, int] = [1920, 1080],                             # Width x Height (px)
            refresh: int = 60,                                                 # Hz
            
            # Features
            keypad: bool = False,                                              # ex: Yes, No
            webcam: bool = False,                                              # ex: Yes, No
            backlit: bool = False,                                             # ex: Yes, No
            
            # Hardware
            cpu: [Optional[str], Optional[int], Optional[int], Optional[int], Optional[chr]] =
                            [None, None, None, None, None],                    # (brand, family, generation, model, suffix)
            gpu: [Optional[str], Optional[str], Optional[int], Optional[int], Optional[str]] =
                            [None, None, None, None, None],                    # (brand, type, generation/series, preformance, suffix)
            
            ram: [Optional[int], Optional[str]] = [None, None],                # (GB, type)
            storage: [Optional[int], Optional[str]] = [None, None],            # (GB, SSD or HDD)
            
            # URL & Timestamp
            url: Optional[str] = None,                                         # URL
            timestamp: Optional[datetime] = None):                             # timestamp
                    
        self.brand = brand
        self.name = name
        self.style = style
        
        self.rating = rating
        self.reviews = reviews
        
        self.price = price
        self.msrp = msrp
        self.sale = sale
        
        self.weight = weight
        self.dimensions = dimensions
        
        self.screen = screen
        self.resolution = resolution
        self.refresh = refresh
        
        self.keypad = keypad
        self.webcam = webcam
        self.backlit = backlit
        
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        
        self.url = url
        self.timestamp = datetime.now()
        self.score = 0

        self.check()
    


    def check(self) -> None:
        # Style check
        if self.style not in {"Laptop", "All-in-One", "Tower"}:
            raise ValueError(f"Invalid style '{self.style}'. Must be Laptop, All-in-One, or Tower.")

        # Reviews checks
        if self.rating is not None and not (0.0 <= self.rating <= 5.0):
            raise ValueError(f"Rating of {self.rating} is outside of range 0 – 5")
        if self.reviews < 0:
            raise ValueError(f"Reviews of {self.reviews} is invalid")

        # Price checks
        if self.price is not None and self.price < 0:
            raise ValueError(f"Price of {self.price} is invalid")
        if self.msrp is not None and self.msrp < 0:
            raise ValueError(f"List price of {self.msrp} is invalid")
        if not (0 <= self.sale <= 100):
            raise ValueError(f"Sale of {self.sale} is outside of range 0 – 100")

        # Size & Screen checks
        if self.weight is not None and self.weight < 0:
            raise ValueError(f"Weight of {self.weight} is invalid")
        if any(d is not None and d < 0 for d in self.dimensions):
            raise ValueError(f"Invalid dimensions: {self.dimensions}")
        if self.screen is not None and self.screen < 0:
            raise ValueError(f"Screen size of {self.screen} is invalid")
        if any(r < 0 for r in self.resolution):
            raise ValueError(f"Invalid resolution: {self.resolution}")
        if self.refresh < 0:
            raise ValueError(f"Refresh rate of {self.refresh} is invalid")

        # CPU & GPU check
        if self.cpu[1] is not None and self.cpu[1] not in {3, 5, 7, 9}:
            raise ValueError(f"CPU family {self.cpu[1]} is not 3, 5, 7, or 9")
        if self.cpu[2] is not None and self.cpu[2] < 0:
            raise ValueError(f"CPU generation of {self.cpu[2]} is invalid")
        if self.cpu[3] is not None and self.cpu[3] < 0:
            raise ValueError(f"CPU model of {self.cpu[3]} is invalid")

        if self.gpu[2] is not None and self.gpu[2] < 0:
            raise ValueError(f"GPU generation of {self.gpu[2]} is invalid")
        if self.gpu[3] is not None and self.gpu[3] < 0:
            raise ValueError(f"GPU performance of {self.gpu[3]} is invalid")

        # RAM & storage checks
        if self.ram[0] is not None and self.ram[0] < 0:
            raise ValueError(f"RAM of {self.ram[0]} GB is invalid")
        if self.storage[0] is not None and self.storage[0] < 0:
            raise ValueError(f"Storage of {self.storage[0]} GB is invalid")
            
        self.score = self.create_score()
            
            
    def create_score(self) -> float:
        ratingScore = (self.rating * 20) if self.rating is not None else 90
        
        priceScore = min((self.msrp - self.price) / 5, 100) if (self.msrp is not None and self.price is not None) else 0
        
        resolutionScore = min(((self.resolution[0] * self.resolution[1]) / (1920 * 1080)) * 50, 100)
        
        refreshScore = min(self.refresh / 2.4, 100)
        
        featureScore = sum([self.keypad, self.webcam, self.backlit]) * 33.4
        
        cpuScore = min((self.cpu[1] - 1) * 12.5, 100) if self.cpu[1] is not None else 0
        
        gpuScore = min(self.gpu[2] + self.gpu[3] - 40, 100) if self.gpu[2] is not None else 20
        
        ramScore = min(self.ram[0] * 1.5625, 100) if self.ram[0] is not None else 6.25
        
        storageScore = min(self.storage[0] / 20, 100) if self.storage[0] is not None else 6
        
        self.score = min(round((ratingScore + priceScore + resolutionScore + refreshScore + featureScore + cpuScore + gpuScore + ramScore + storageScore) / 9, 2), 100)
        return self.score
    
    

    def __str__(self) -> str:
        # Line 1: Basic
        line1 = f"{self.screen or None}\" {self.brand or 'Unknown'} {self.name or ''} {self.style}, {self.rating} Stars & {self.reviews} Reviews"
        
        # Line 2: Price
        line2 = f"${self.price}, with {self.sale}% off and a MSRP of ${self.msrp}"
        
        # Line 3: Physical
        dimensions = f"{self.dimensions[0]} x {self.dimensions[1]} x {self.dimensions[2]} (L x W x T)" if all(self.dimensions) else "Unkown Dimensions"
        line3 = f"Size: {self.weight or 'Unkown'} lb & {dimensions}"
        line4 = f"Resolution: {self.resolution[0]} x {self.resolution[1]} px (W x H) at {self.refresh} Hz"
        
        # Line 4: Features
        features = [f for f, flag in zip(["Keypad","Webcam","Backlit"],[self.keypad,self.webcam,self.backlit]) if flag]
        featureString = ", ".join(features) if features else "None"
        line5 = f"Features include: {featureString}"
        
        # Line 5: CPU
        cpu = self.cpu
        cpuString = (f"CPU: {cpu[0]} {cpu[1]}-{cpu[2]}{cpu[3]}{cpu[4]}" if cpu[0] and cpu[1] is not None else "CPU: N/A")
        
        # Line 6: GPU
        gpu = self.gpu
        gpuString = (f"GPU: {gpu[0]} {gpu[1]} {gpu[2]}{gpu[3]} {gpu[4]}" if gpu[0] and gpu[2] and gpu[3] is not None else "GPU: N/A")
        
        # Line 7: RAM & Storage
        ramString = f"RAM: {self.ram[0]} GB of {self.ram[1]}" if self.ram[0] else "RAM: N/A"
        storageString = f"Storage: {self.storage[0]} GB {self.storage[1]}" if self.storage[0] else "Storage: N/A"
        
        # Line 8: URL
        urlString = f"URL: {self.url or 'N/A'}"
        
        # Line 9: Timestamp
        timestamp = self.timestamp.strftime('%m/%d/%Y at %H:%M')
        timestampString = f"Last Checked on {timestamp}"

        return "\n".join([line1, line2, "", line3, line4, line5, "", cpuString, gpuString, ramString, storageString, "", urlString, timestampString])
        
    
    def to_str(self) -> str:
        cpu, gpu= self.cpu, self.gpu
        
        priceString = f"${self.price}, " if self.price is not None else ""
        basicString = f"{self.screen or None}\" {self.brand or 'Unknown'} {self.name or ''} {self.style}"
        
        cpuString = f", {cpu[0]} {cpu[1]}-{cpu[2]}{cpu[3]}{cpu[4]}" if cpu[0] and cpu[1] is not None else ""
        gpuString = f", {gpu[0]} {gpu[1]} {gpu[2]}{gpu[3]} {gpu[4]}" if gpu[0] and gpu[2] and gpu[3] is not None else ""
        ramString = f", {self.ram[0]} GB of {self.ram[1]}" if self.ram[0] else ""
        storageString = f", {self.storage[0]} GB {self.storage[1]}" if self.storage[0] else ""
        
        return priceString + basicString + cpuString + gpuString + ramString + storageString
        
    
    def to_list(self) -> list:
        return [self.price, [self.brand, self.name, self.style], 
                [self.screen, self.resolution[0], self.resolution[1], self.refresh],
                self.cpu, self.gpu, self.ram, self.storage]


    def to_row(self) -> list:
        return [self.brand, self.name, self.style,
                self.rating, self.reviews,
                self.price, self.msrp, self.sale,
                self.screen, self.resolution, self.refresh,
                self.cpu, self.gpu, self.ram, self.storage,
                self.url, self.timestamp.isoformat(), self.score]


    def to_dict(self) -> dict:
        return {'brand': self.brand, 'name': self.name, 'style': self.style,
                'rating': self.rating, 'reviews': self.reviews,
                'price': self.price, 'msrp': self.msrp, 'sale': self.sale,
                'weight': self.weight, 'dimensions': self.dimensions,
                'screen': self.screen, 'resolution': self.resolution, 'refresh': self.refresh,
                'keypad': self.keypad, 'webcam': self.webcam, 'backlit': self.backlit,
                'cpu': self.cpu, 'gpu': self.gpu, 'ram': self.ram, 'storage': self.storage,
                'url': self.url, 'timestamp': self.timestamp, 'score': self.score}
    
    
    def to_json(self) -> json:
        tempDict = self.to_dict()
        tempDict['timestamp'] = tempDict['timestamp'].isoformat()
        return json.dumps(tempDict, indent = 4)
    
    
    
    def to_computer(data: dict) -> 'Computer':
        tempComputer = Computer()
        for key, val in data.items():
            if hasattr(tempComputer, key):
                setattr(tempComputer, key, val)
        
        tempComputer.check()
        return tempComputer
        
    
    def update(self, data: dict) -> None:
        for key, vavlue in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        self.check()
    
    
    
if __name__ == "__main__":
    pc = Computer()
    
    pc.brand = "HP"
    pc.name = "Victus"
    pc.style = "Laptop"
    pc.rating = 4.5
    pc.reviews = 92
    pc.price = 653.82
    pc.msrp = 653.82
    pc.sale = 0
    pc.refresh = 144
    pc.resolution = [1920, 1080]
    pc.weight = 5.06
    pc.dimensions = [10.04, 14.09, 0.93]
    pc.screen = 15
    pc.keypad = True
    pc.backlit = True
    pc.webcam = True
    pc.cpu = ["Intel", 5, 12, 450, "H"]
    pc.gpu = ["NVIDIA", "GeForce RTX", 30, 50, ""]
    pc.ram = [16, "DDR4"]
    pc.storage = [1000, "SSD"]
    pc.url = "www.example.com"
    
    pc.check()
    print(pc)
    
    pcPrint = pc.__str__()
    pcString = pc.to_str()
    pcList = pc.to_list()
    pcRow = pc.to_row()
    pcDict = pc.to_dict()
    pcJson = pc.to_json()
    
    score = pc.score