# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:44:49 2025

@author: Augustin Ward
"""


from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Tuple


@dataclass
class Computer:
    # Basic Info
    brand: Optional[str] = None                                 # ex: Hp, Lenovo
    name: Optional[str] = None                                  # ex: Victus 15, Ominbook X
    style: str = "Laptop"                                       # Only 3 options: Laptop, All-in-One, or Tower
    
    # Reviews & Price
    rating: float = 0.0                                         # 0.0 - 5.0
    reviews: int = 0                                            # review count
    
    price: Optional[int] = None                                 # integer in dollars
    msrp: Optional[int] = None                                  # manufacturer's suggested retail price
    sale: int = 0                                               # percent off, 0 - 100
    
    # Size & Screen
    weight: Optional[float] = None                              # pounds (lb)
    dimensions: Tuple[Optional[float], Optional[float], Optional[float]] = (None, None, None)
                                                                # Length, Width, Thickness iches (in)
    
    screen: Optional[float] = None                              # diagonal (in), None for Tower
    resolution: Tuple[int, int] = (1920, 1080)                  # Width x Height (px)
    refresh: int = 60                                           # Hz
    
    # Features
    keypad: bool = False                                        # ex: Yes, No
    webcam: bool = False                                        # ex: Yes, No
    backlit: bool = False                                       # ex: Yes, No
    
    # Hardware
    cpu: Tuple[Optional[str], Optional[int], Optional[int], Optional[int], Optional[chr]] = (None, None, None, None, None)
                                                                # (brand, family, generation, model, suffix)
    gpu: Tuple[Optional[str], Optional[str], Optional[int], Optional[int], Optional[str]] = (None, None, None, None, None)    
                                                                # (brand, type, generation/series, preformance, suffix)
    
    ram: Tuple[Optional[int], Optional[str]] = (None, None)     # (GB, type)
    storage: Tuple[Optional[int], Optional[str]] = (None, None) # (GB, SSD or HDD)
    
    # URL & Timestamp
    url: Optional[str] = None                                   # URL
    timestamp: datetime = datetime.now()                        # timestamp
    
    score: Optional[float] = None
    


    def __post_init__(self):
        # Style check
        if self.style not in {"Laptop", "All-in-One", "Tower"}:
            raise ValueError(f"Invalid style '{self.style}'. Must be Laptop, All-in-One, or Tower.")

        # Reviews checks
        if not (0.0 <= self.rating <= 5.0):
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
            

    def __str__(self):
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
        
    
    def to_str(self):
        cpu, gpu= self.cpu, self.gpu
        
        priceString = f"${self.price}, " if self.price is not None else ""
        basicString = f"{self.screen or None}\" {self.brand or 'Unknown'} {self.name or ''} {self.style}"
        
        cpuString = f", {cpu[0]} {cpu[1]}-{cpu[2]}{cpu[3]}{cpu[4]}" if cpu[0] and cpu[1] is not None else ""
        gpuString = f", {gpu[0]} {gpu[1]} {gpu[2]}{gpu[3]} {gpu[4]}" if gpu[0] and gpu[2] and gpu[3] is not None else ""
        ramString = f", {self.ram[0]} GB of {self.ram[1]}" if self.ram[0] else ""
        storageString = f", {self.storage[0]} GB {self.storage[1]}" if self.storage[0] else ""
        
        return priceString + basicString + cpuString + gpuString + ramString + storageString
        
    
    def to_list(self):
        return [self.price, (self.brand, self.name, self.style), (self.screen, self.resolution[0], self.resolution[1], self.refresh), self.cpu, self.gpu, self.ram, self.storage]


    def create_score(self):
        ratingScore = self.rating * 20
        
        priceScore = min((self.msrp - self.price) / 5, 100)
        
        resolutionScore = min(((self.resolution[0] * self.resolution[1]) / (1920 * 1080)) * 50, 100)
        
        refreshScore = min(self.refresh / 2.4, 100)
        
        featureScore = sum([self.keypad, self.webcam, self.backlit]) * 33.4
        
        cpuScore = (self.cpu[1] - 1) * 12.5
        
        gpuScore = min(self.gpu[2] + self.gpu[3] - 40, 100)
        
        ramScore = min(self.ram[0] * 1.5625, 100)
        
        storageScore = min(self.storage[0] / 20, 100)
        
        self.score = min(round((ratingScore + priceScore + resolutionScore + refreshScore + featureScore + cpuScore + gpuScore + ramScore + storageScore) / 9, 2), 100)
        return self.score
        
    
    
if __name__ == "__main__":
    pc = Computer()
    # assign after init
    pc.brand = "HP"
    pc.name = "Victus"
    pc.style = "Laptop"
    pc.rating = 4.5
    pc.reviews = 92
    pc.price = 653.82
    pc.msrp = 653.82
    pc.sale = 0
    pc.refresh = 144
    pc.resolution = (1920, 1080)
    pc.weight = 5.06
    pc.dimensions = (10.04, 14.09, 0.93)
    pc.screen = 15
    pc.keypad = True
    pc.backlit = True
    pc.webcam = True
    pc.cpu = ("Intel", 5, 12, 450, "H")
    pc.gpu = ("NVIDIA", "GeForce RTX", 30, 50, "")
    pc.ram = (16, "DDR4")
    pc.storage = (1000, "SSD")
    pc.url = "www.example.com"
    print(pc)
    
    pcString = pc.to_str()
    pcList = pc.to_list()
    pc.create_score()
    
    score = pc.score