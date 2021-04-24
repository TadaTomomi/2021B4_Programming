import numpy as np

def relu(x):
  return np.maximum(0, x)

def main():
  x = np.array([-1.0, 0.0, 0.5, 2.0])
  if __name__ == "__main__":
    print(relu(x))

main()