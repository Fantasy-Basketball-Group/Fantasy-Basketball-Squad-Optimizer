# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# copy the content of the local tests directory to the working directory
COPY tests/ .

# copy test data
COPY data/test_data_set.csv data/test_data_set.csv

CMD ["black", "src", "tests" ]
CMD ["pytest", "tests"]
