# Python program to demonstrate basic array characteristics
import numpy as np


# Creating array object
numpy_array_1 = np.array([[1, 2, 3],
                         [4, 2, 5]])

print(f'First Numpy Array:\n{numpy_array_1}')

# Printing the type of array object
print(f'Type of the Numpy Array:{type(numpy_array_1)}')

# Printing Array Dimensions (axes)
print(f'Dimension of the array:{numpy_array_1.ndim}')

# Printing Array Shape
print(f'Shape of the array:{numpy_array_1.shape}')

# Printing Array Size (total number of elements in the array)
print(f'Size of the array:{numpy_array_1.size}')

# Printing type of elements in array
print(f'Array stores elements of type:{numpy_array_1.dtype}')


class NumPyArrayManager:
    def __init__(self, *args):
        self.numpy_array_1_ins = np.array([args[0],
                                  args[1]])
        print(f'First Numpy Array:\n{self.numpy_array_1_ins}')

    def check_array_type( self ):
        print(f'Type of the First Numpy Array:\n{type(self.numpy_array_1_ins)}')

    def check_array_dimension( self ):
        print(f'Dimension of the First Numpy Array:\n{self.numpy_array_1_ins.ndim}')

    def check_array_shape( self ):
        print(f'Dimension of the First Numpy Array:\n{self.numpy_array_1_ins.shape}')

    def check_array_size( self ):
        print(f'Dimension of the First Numpy Array:\n{self.numpy_array_1_ins.size}')

def main():
    list_1:list = [1, 2, 3]
    list_2:list = [4, 2, 5]
    numpy_array_manager = NumPyArrayManager(list_1, list_2)


if __name__ == "__main__":
    main()