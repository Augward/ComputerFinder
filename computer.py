# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:44:49 2025

@author: Augustin Ward
"""


from datetime import datetime
from typing import Optional
import json



class CPU:
    def __init__(self,
            brand: Optional[str] = None,                                       # Intel
            family: Optional[str] = None,                                      # i5
            generation: Optional[int] = None,                                  # 12th Gen
            model: Optional[int] = None,                                       # 400
            suffix: Optional[str] = None):                                     # K
        
        self.brand = brand
        self.family = family
        self.generation = generation
        self.model = model
        self.suffix = suffix
        
        self.validBrands = ["INTEL", "AMD", "APPLE"]                           # CPU Brands
        self.validFamilies = [3, 5, 7, 9, "3", "5", "7", "9",                  # Intel/AMD Families
                              1, 2, 4, "1", "2", "4"]                          # Mac Families
        
        self.edgeCase = False
        
        self.check()
        
        
    def check(self):
        if self.brand is not None and not isinstance(self.brand, str):
            raise TypeError(f"CPU brand: {self.brand} is invalid")
        elif self.brand is None:
            None
        elif self.brand.upper() not in self.validBrands:
            raise ValueError(f"CPU brand: {self.brand} is invalid")
        elif isinstance(self.brand, str):
            if self.brand.upper() == "AMD":
                self.brand = self.brand.upper()
            else:
                self.brand = self.brand.lower().capitalize()
        else:
            self.edgeCase = True
            
        if self.family is not None and not isinstance(self.family, (str, int)):
            raise TypeError(f"CPU family: {self.family} is invalid")
        elif self.family is None:
            None
        elif self.family not in self.validFamilies:
            raise ValueError(f"CPU family: {self.generation} is invalid")
        elif isinstance(self.family, (str, int)):
            self.family = int(self.family)
        else:
            self.edgeCase = True
        
        if self.generation is not None and not isinstance(self.generation, int):
            raise TypeError(f"CPU generation: {self.generation} is invalid")
        elif self.generation is None:
            None
        elif isinstance(self.generation, int):
            if self.generation < 0:
                raise ValueError(f"CPU generation: {self.generation} is invalid")
        else:
            self.edgeCase = True
            
        if self.model is not None and not isinstance(self.model, int):
            raise TypeError(f"CPU model: {self.model} is invalid")
        elif self.model is None:
            None
        elif isinstance(self.model, int):
            if self.model < 0:
                raise ValueError(f"CPU model: {self.model} is invalid")
        else:
            self.edgeCase = True
            
        if self.suffix is not None and not isinstance(self.suffix, (str, chr)):
            raise TypeError(f"CPU suffix: {self.suffix} is invalid")
        elif self.suffix is None:
            None
        elif isinstance(self.suffix, (str, chr)):
            if self.brand == "Apple":
                self.suffix = self.suffix.lower().capitalize()
            else:
                self.suffix = self.suffix.upper()
        else:
            self.edgeCase = True
                
                
    def __str__(self) -> str:
        tempStr = ""
        
        match self.brand:
            case "Intel":
                tempStr = "Intel "
                if isinstance(self.family, int):
                    tempStr += "i" + str(self.family)
                else:
                    tempStr += str(self.family)
                if self.generation:
                    if self.model:
                        tempStr += "-" + str(self.generation) + str(self.model)
                        if self.suffix:
                            tempStr += self.suffix
                    else:
                        tempStr += " " + str(self.generation) + "th Gen"
            
            case "AMD":
                tempStr = "AMD "
                if isinstance(self.family, int):
                    tempStr += "Ryzen " + str(self.family)
                else:
                    tempStr += str(self.family)
                if self.generation:
                    if self.model:
                        tempStr += " " + str(self.generation) + str(self.model)
                        if self.suffix:
                            tempStr += self.suffix
                    else:
                        tempStr += " " + str(self.generation) + "th Gen"
                        
                
            case "Apple":
                tempStr = "Apple "
                if isinstance(self.family, int):
                    tempStr += "M" + str(self.family)
                else:
                    tempStr += str(self.family)
                if self.suffix:
                    tempStr += " " + self.suffix
                
            case _:
                tempStr = "Unkown CPU Brand"
        
        return tempStr
    
    
    # def to_dict(self) -> dict:
    #     return {
    #         'brand': self.brand,
    #         'family': self.family,
    #         'generation': self.generation,
    #         'model': self.model,
    #         'suffix': self.suffix
    #     }
    
    
    
class GPU:
    def __init__(self,
            brand: Optional[str] = None,
            series: Optional[str] = None,
            generation: Optional[int] = None,
            performance: Optional[int] = None,
            suffix: Optional[str] = None):

        self.brand = brand
        self.series = series
        self.generation = generation
        self.performance = performance
        self.suffix = suffix


        self.validBrands = ["NVIDIA", "RADEON", "INTEL", "APPLE"]
        
        self.edgeCase = False

        self.check()
        
        
    def check(self):
        if self.brand is not None and not isinstance(self.brand, str):
            raise TypeError(f"GPU brand: {self.brand} is invalid")
        elif self.brand is None:
            None
        elif self.brand.upper() not in self.validBrands:
            raise ValueError(f"GPU brand: {self.brand} is invalid")
        elif isinstance(self.brand, str):
            if self.brand.upper() == "NVIDIA":
                self.brand = self.brand.upper()
            else:
                self.brand = self.brand.lower().capitalize()
        else:
            self.edgeCase = True
        
        if self.series is not None and not isinstance(self.series, str):
            raise TypeError(f"GPU series: {self.series} is invalid")
        elif self.series is None:
            None
        elif self.series.upper() == "INTEGRATED":
            self.series = self.series.lower().capitalize()
        elif isinstance(self.series, str):
            self.series = self.series.upper()
        else:
            self.edgeCase = True
            
        if self.generation is not None and not isinstance(self.generation, int):
            raise TypeError(f"GPU generation: {self.generation} is invalid")
        elif self.generation is None:
            None
        elif isinstance(self.generation, int):
            if self.generation < 0:
                raise ValueError(f"GPU generation: {self.generation} is invalid")
        else:
            self.edgeCase = True
            
        if self.performance is not None and not isinstance(self.performance, int):
            raise TypeError(f"GPU performance: {self.performance} is invalid")
        elif self.performance is None:
            None
        elif isinstance(self.performance, int):
            if self.performance < 0:
                raise ValueError(f"GPU performance: {self.performance} is invalid")
        else:
            self.edgeCase = True
            
        if self.suffix is not None and not isinstance(self.suffix, (str, chr)):
            raise TypeError(f"GPU suffix: {self.suffix} is invalid")
        elif self.suffix is None:
            None
        elif isinstance(self.suffix, (str, chr)):
            if self.brand in ["Intel", "Apple"]:
                self.suffix = self.suffix.lower().capitalize()
            else:
                if len(self.suffix) <= 2: 
                    self.suffix = self.suffix.upper()
                else:
                    self.suffix = self.suffix.lower().capitalize()
        else:
            self.edgeCase = True    
                        
            
    def __str__(self) -> str:
        tempStr = ""
        
        match self.brand:
            case "NVIDIA":
                tempStr = "NVIDIA " + self.series
                if self.generation:
                    tempStr += " " + str(self.generation) + str(self.performance)
                    if self.suffix:
                        tempStr += " " + self.suffix
            
            case "Radeon":
                tempStr = "Radeon " + self.series
                if self.generation:
                    tempStr += " " + str(self.generation) + str(self.performance)
                    if self.suffix:
                        tempStr += " " + self.suffix
                        
            case "Intel":
                tempStr = "Intel "
                if self.series:
                    tempStr += self.series
                else:
                    tempStr += "Integrated"
            
            case "Apple":
                tempStr = "Apple "
                if self.series:
                    tempStr += self.series
                else:
                    tempStr += "Integrated"
                                    
            case _:
                tempStr = "Unkown GPU Brand"
                
        return tempStr
    
    
    # def to_dict(self) -> dict:
    #     return {
    #         'brand': self.brand,
    #         'series': self.series,
    #         'generation': self.generation,
    #         'performance': self.performance,
    #         'suffix': self.suffix
    #     }
    
    

class Computer:
    def __init__(self,
            # Basic Info
            brand: Optional[str] = None,                                       # ex: Hp, Lenovo
            name: Optional[str] = None,                                        # ex: Victus 15, Ominbook X
            style: str = "Laptop",                                             # Only 4 options: Laptop, All-in-One, Mini, or Tower
            
            # Reviews & Price
            rating: float = None,                                              # 0.0 - 5.0
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
            cpu: CPU = CPU(),
            gpu: GPU = GPU(),
            
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
        if self.style not in {"Laptop", "All-in-One", "Mini", "Tower"}:
            raise ValueError(f"Invalid style '{self.style}'. Must be Laptop, All-in-One, Mini, or Tower.")

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
        self.cpu.check()
        self.gpu.check()

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
        
        cpuScore = min((self.cpu.family - 1) * 12.5, 100) if self.cpu.family is not None else 0
        
        gpuScore = min(self.gpu.generation + self.gpu.performance - 40, 100) if self.gpu.generation is not None else 20
        
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
        cpuString = (f"CPU: {cpu}" if cpu.brand and cpu.family is not None else "CPU: N/A")
        
        # Line 6: GPU
        gpu = self.gpu
        gpuString = (f"GPU: {gpu}" if gpu.brand and gpu.generation and gpu.performance is not None else "GPU: N/A")
        
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
        return {
            'brand': self.brand, 'name': self.name, 'style': self.style,
            'rating': self.rating, 'reviews': self.reviews,
            'price': self.price, 'msrp': self.msrp, 'sale': self.sale,
            'weight': self.weight, 'dimensions': self.dimensions,
            'screen': self.screen, 'resolution': self.resolution, 'refresh': self.refresh,
            'keypad': self.keypad, 'webcam': self.webcam, 'backlit': self.backlit,
            'cpu': self.cpu, 'gpu': self.gpu, 'ram': self.ram, 'storage': self.storage,
            'url': self.url, 'timestamp': self.timestamp, 'score': self.score
        }
    
    
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
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        self.check()
    
    
    
if __name__ == "__main__":
    cpu1 = CPU("intel", 3, 14, 400)
    print(cpu1)
    cpu2 = CPU("amd", 7, 8, 300, "x")
    print(cpu2)
    cpu3 = CPU("apple", 4, None, None, "Pro")
    print(cpu3)
    
    gpu1 = GPU("Nvidia", "GTX", 30, 50, "SUper")
    print(gpu1)
    gpu2 = GPU("Radeon", "Rx", 90, 60, "XT")
    print(gpu2)
    gpu3 = GPU("Intel", "Integrated")
    print(gpu3)
    gpu4 = GPU("Apple")
    print(gpu4)
    
    # pc = Computer()
    
    # pc.brand = "HP"
    # pc.name = "Victus"
    # pc.style = "Laptop"
    # pc.rating = 4.5
    # pc.reviews = 92
    # pc.price = 653.82
    # pc.msrp = 653.82
    # pc.sale = 0
    # pc.refresh = 144
    # pc.resolution = [1920, 1080]
    # pc.weight = 5.06
    # pc.dimensions = [10.04, 14.09, 0.93]
    # pc.screen = 15
    # pc.keypad = True
    # pc.backlit = True
    # pc.webcam = True
    # cpu = CPU("Intel", 5, 12, 450, "H")
    # pc.cpu = cpu
    # gpu = GPU("NVIDIA", "GeForce RTX", 30, 50, "")
    # pc.gpu = gpu
    # pc.ram = [16, "DDR4"]
    # pc.storage = [1000, "SSD"]
    # pc.url = "www.example.com"
    
    # pc.check()
    # print(pc)
    
    # pcPrint = pc.__str__()
    # pcString = pc.to_str()
    # pcList = pc.to_list()
    # pcRow = pc.to_row()
    # pcDict = pc.to_dict()
    # pcJson = pc.to_json()
    
    # score = pc.score