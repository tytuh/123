import streamlit as st
from scipy.optimize import minimize

def optimize_ellipse():
    a = st.sidebar.slider("a", 0.1, 10.0, 1.0)
    b = st.sidebar.slider("b", 0.1, 10.0, 1.0)
    x0 = st.sidebar.slider("x0", -10.0, 10.0, 0.0)
    y0 = st.sidebar.slider("y0", -10.0, 10.0, 0.0)

    def ellipse(x):
        return (a*x[0] - x0)**2 + (b*x[1] - y0)**2
    
    x0 = [0, 0]
    res = minimize(ellipse, x0)
    st.write("Minimum at ", res.x)
    st.write("Function value at minimum: ", res.fun)

if __name__ == "__main__":
    st.title("Ellipse Optimizer")
    optimize_ellipse()