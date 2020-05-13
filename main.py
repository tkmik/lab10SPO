from gpio import * 
from time import * 
 
def main():  
    pinMode(1, IN)  
    pinMode(2, OUT)  
    pinMode(3, OUT)  
    print("Blinking")  
    while True:   
        Ts = analogRead(1);  
        Tc = ((float(Ts)/1023)*200-100);   
        if Tc < 20:    
            digitalWrite(2, LOW); 
            print("AirCoolerLOW");    
            digitalWrite(3, HIGH);    
            print("HeatingElementHIGH");    
            print("CurrentTemp -> ");    
            print(Tc);    
            delay(1000);   
        elif Tc > 25:    
            digitalWrite(3, LOW);   
            print("HeatingElementLOW");    
            digitalWrite(2, HIGH);    
            print("AirCoolerHIGH");    
            print("CurrentTemp -> ");    
            print(Tc);    
            delay(1000);   
        else:    
            digitalWrite(3, LOW);    
            print("HeatingElementLOW");    
            digitalWrite(2, LOW);    
            print("AirCoolerLOW");    
            print("CurrentTemp -> ");    
            print(Tc);    
            delay(1000); 
 
if __name__ == "__main__":  
    main() 