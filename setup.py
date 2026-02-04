from setuptools import setup, find_packages 

setup(
        name = "baseball_pitch_prediction", 
        version="0.1.0",
        author="Anthony Bernardi", 
        author_email="anthony.david.bernardi@gmail.com",
        description="Deep Learning models for MLB` pitch sequencing and pitch outcome prediction.",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/ad-bernardi/baseball_pitch_prediction",
        packages=find_packages(where="."),
        python_requires=">=3.11",
        install_requires=[
            "torch>=2.0.0",
            "numpy>=1.24.0",
            "pandas>=2.0.0",
            "scikit-learn>=1.3.0",
            "pybaseball>=2.2.0",
            "matplotlib>=3.7.0",
            "seaborn>=0.12.0",
            "tqdm>=4.65.0",
            "pyyaml>=6.0",
            "python-dotenv>=1.0.0",
            ],
        extras_require={
            "dev": [
                "jupyter>=1.0.0",
                "black>=23.10.0",
                "flake8>=6.1.0",
                "pytest>=7.4.0",
                ],
            },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research", 
            "License :: OSI Approved :: BSD License", 
            "Programming Language :: Python :: 3.11",
            ],
        )

