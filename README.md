# quantum-circuit-transform
Concept for quantum circuit simplification.

### Quantum Circuit Graph Transformation

### What I did and why

This implements a tiny slice of a quantum circuit transformation pipeline. It:

- Represents a quantum circuit as a simple Python list of gate names.
- Applies one rewrite rule: two consecutive Hadamard (H) gates cancel each other.

Even though basic, this shows the ability to model circuits as graphs (or sequences), define transformation rules, and execute them programmatically.

### Files

- `circuit_transform.py`: Core script with ~20 lines of Python.
- `README.md`: This description of what was done and why.
"""
