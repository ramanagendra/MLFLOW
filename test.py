import mlflow
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

def calcualate(x,y):
    return(x+y)

if __name__ == "__main__":
    x,y=100,200
    result=calcualate(x,y)
    print(f"Here is my result {result}")
    
    
