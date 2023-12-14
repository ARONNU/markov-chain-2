import pandas as pd
import numpy as np
from streamlit import st

# Set initial matrix dimensions
m, n = 2, 2

# Define function for matrix multiplication
def matrix_multiply(matrix_a, matrix_b):
  return np.matmul(matrix_a, matrix_b)

# Create empty dataframes for user input
df_a = pd.DataFrame(np.zeros((m, n)), dtype=int)
df_b = pd.DataFrame(np.zeros((n, m)), dtype=int)

# Build the Streamlit app
st.title("Interactive Matrix Multiplication")

# Sidebar for choosing matrix dimensions
with st.sidebar:
  st.header("Matrix Dimensions")
  m = st.slider("Number of rows in matrix A", min_value=1, max_value=10, value=m)
  n = st.slider("Number of columns in matrix A and rows in matrix B", min_value=1, max_value=10, value=n)

# User input for matrices
st.header("Matrix A")
st.dataframe(df_a.astype(int), editable=True)

st.header("Matrix B")
st.dataframe(df_b.astype(int), editable=True)

# Calculate and display result
if st.button("Calculate"):
  matrix_a = df_a.to_numpy()
  matrix_b = df_b.to_numpy()
  result = matrix_multiply(matrix_a, matrix_b)
  st.header("Result Matrix")
  st.dataframe(result)

# Show explanation (optional)
st.markdown("""
**Note:** This app allows you to input matrices through editable tables. 
Click "Calculate" to perform the multiplication and see the result.
""")

