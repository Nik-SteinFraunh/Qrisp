"""
\********************************************************************************
* Copyright (c) 2023 the Qrisp authors
*
* This program and the accompanying materials are made available under the
* terms of the Eclipse Public License 2.0 which is available at
* http://www.eclipse.org/legal/epl-2.0.
*
* This Source Code may also be made available under the following Secondary
* Licenses when the conditions for such availability set forth in the Eclipse
* Public License, v. 2.0 are satisfied: GNU General Public License, version 2
* with the GNU Classpath Exception which is
* available at https://www.gnu.org/software/classpath/license.html.
*
* SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
********************************************************************************/
"""

from jax.core import AbstractValue, raise_to_shaped_mappings
from qrisp.jax import QuantumPrimitive

class AbstractQuantumCircuit(AbstractValue):
    pass

    def __repr__(self):
        return "QuantumCircuit"

def create_qubits(size, state):
    return create_qubits_p.bind(size, state)
        
raise_to_shaped_mappings[AbstractQuantumCircuit] = lambda aval, _: aval

create_quantum_circuit_p = QuantumPrimitive("create_quantum_circuit")

@create_quantum_circuit_p.def_abstract_eval
def create_quantum_circuit_abstract_eval():
    """Abstract evaluation of the primitive.
    
    This function does not need to be JAX traceable. It will be invoked with
    abstractions of the actual arguments. 
    """
    
    return AbstractQuantumCircuit()

# Register Creation
create_qubits_p = QuantumPrimitive("create_qubits")
create_qubits_p.multiple_results = True

from qrisp.jax import AbstractQubitArray

@create_qubits_p.def_abstract_eval
def create_qubits_abstract_eval(qc, size):
    """Abstract evaluation of the primitive.
    
    This function does not need to be JAX traceable. It will be invoked with
    abstractions of the actual arguments. 
    Args:
      xs, ys, zs: abstractions of the arguments.
    Result:
      a ShapedArray for the result of the primitive.
    """
    
    return AbstractQuantumCircuit(), AbstractQubitArray()

# Call
call_qc_p = QuantumPrimitive("call_qc")
create_qubits_p.multiple_results = True

@call_qc_p.def_abstract_eval
def call_qc_abstract_eval(main_routine_qc, subroutine_qc, *qb_arrays):
    """Abstract evaluation of the primitive.
    
    This function does not need to be JAX traceable. It will be invoked with
    abstractions of the actual arguments. 
    Args:
      xs, ys, zs: abstractions of the arguments.
    Result:
      a ShapedArray for the result of the primitive.
    """
    
    return AbstractQuantumCircuit()