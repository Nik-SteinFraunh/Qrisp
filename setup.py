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

import setuptools

REQUIREMENTS = ["connexion>=2.12.0",
                "qiskit",
                "thrift>=0.15.0",
                "matplotlib>=3.5.1",
                "waitress>=2.1.1",
                "scipy>=1.10.0",
                "numba",
                "networkx",
                "tdqm",
                "dill",
                "flask"]


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrisp",
    author="Raphael Seidel",
    author_email="raphael.seidel@fokus.fraunhofer.de",
    description="Qrisp - A high level language for gate-based quantum computing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires = REQUIREMENTS,
    setup_requires = REQUIREMENTS,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
