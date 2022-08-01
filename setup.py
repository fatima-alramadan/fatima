import setuptools

# Loads your README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-Fatima_Alramadan", # Replace with your own username
    version="0.0.1", # Your version number, needs to be incremented with each iteration
    author="Fatima Alramadan", # Your name
    author_email="fatima.ahr1998@gmail.com", # Your email
    description="This pakage provides some of the animals sounds", # A one sentence description of your package
    long_description=long_description, # A longer description from your `README.md`
    long_description_content_type="text/markdown", # The format of you long_description file
    url="https://github.com/fatima-alramadan", # GitHub where to find your code
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Additional required pieces of metadata (Don't Change)
    packages=setuptools.find_packages(), # Find all packages used and get them ready for distribution (Dont Change)
    python_requires=">=3.7", # The required version of python
)