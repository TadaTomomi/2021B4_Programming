import numpy as np

def sigmoid(x):
  return 1 /(1 + np.exp(-x))
  
def main():
  x = np.array([-1.0, 0.0, 0.5, 2.0])
  if __name__ == "__main__":
    print(sigmoid(x))

main()