# circuit_transform.py
# A minimal script to represent a quantum circuit and apply one rewrite rule:
# two consecutive Hadamard gates (H) cancel.

from typing import List


def simplify_gates(gates: List[str]) -> List[str]:
    """
    Simplify a list of quantum gates by cancelling pairs of consecutive H gates.
    This mimics an optimization in quantum circuits where H·H = I (identity),
    so two H gates in a row can be removed.
    
    Args:
        gates: A list of quantum gate names as strings (e.g., ["H", "CNOT", "H"])

    Returns:
        A new list with the simplification applied.
    """
    simplified: List[str] = []  # This will store the simplified list of gates
    for gate in gates:
        # Check if the last gate added was H and the current gate is also H
        if simplified and gate == "H" and simplified[-1] == "H":
            # Cancel the two H gates: remove the previous one and skip this one
            simplified.pop()
        else:
            # Otherwise, add the gate to the simplified list
            simplified.append(gate)
    return simplified


if __name__ == "__main__":
    # Define a sample quantum circuit using a list of gate names
    circuit = ["H", "CNOT", "H", "H"]

    # Print the original circuit
    print("Original circuit:", circuit)

    # Simplify the circuit and print the result
    print("Simplified circuit:", simplify_gates(circuit))