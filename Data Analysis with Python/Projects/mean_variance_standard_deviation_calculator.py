import numpy as np

def calculate(clist):
    """
    The input of the function should be a list containing 9 digits.
    The function should convert the list into a 3 x 3 Numpy array,
    and then return a dictionary containing the mean, variance,
    standard deviation, max, min, and sum along both axes and 
    for the flattened matrix.

    The returned dictionary should follow this format:

     {
     'mean': [axis1, axis2, flattened],
     'variance': [axis1, axis2, flattened],
     'standard deviation': [axis1, axis2, flattened],
     'max': [axis1, axis2, flattened],
     'min': [axis1, axis2, flattened],
     'sum': [axis1, axis2, flattened]
     }
  """
    # Check that list has nine digits
    if len(clist) != 9:
        raise ValueError("List must contain nine numbers.")
        
    # Convert list to array
    a = np.array(clist).reshape(3,3)
    
    # Create empty calculations dictionary
    calculations = {}
    
    # Add each category to calculations dictionary
    calculations['mean']=[a.mean(axis=0).tolist(),a.mean(axis=1).tolist(),a.mean().tolist()]
    calculations['variance']=[a.var(axis=0).tolist(),a.var(axis=1).tolist(),a.var().tolist()]
    calculations['standard deviation']=[a.std(axis=0).tolist(),a.std(axis=1).tolist(),a.std().tolist()]
    calculations['max']=[a.max(axis=0).tolist(),a.max(axis=1).tolist(),a.max().tolist()]
    calculations['min']=[a.min(axis=0).tolist(),a.min(axis=1).tolist(),a.min().tolist()]
    calculations['sum']=[a.sum(axis=0).tolist(),a.sum(axis=1).tolist(),a.sum().tolist()]
    
    # Return calculations dictionary
    return calculations


### TESTING
# print(calculate([0,1,2,3,4,5,6,7,8]))
    
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

#axis0 = col
#axis1 = row
