# devops-eng-training

This project is practical task of the first week of ModuLab's MLOps course.

I connected a router that performs the four fundamental arithmetic operations (addition, subtraction, multiplication, division) to a simple flask app, and proceeded unit test and health check test of each router function through pytest.

## Environment

Use the conda basic virtual environment.

```bash
conda env list
conda activate -n "ENV_NAME"
```

## Usage

```
python app.py
```

## Test

#### Unit Test

```bash
pytest unittest/functions_test.py
```

#### Integration Test

```bash
pytest integration/app_test.py
```

#### Use Browser

```
# url

## functions
localhost:3000/addition&num1=1&num2=2
localhost:3000/subtraction&num1=6&num2=4
localhost:3000/multiplication&num1=5&num2=3
localhost:3000/division&num1=4&num2=2

## integration
localhost:3000/healthz
```


## Author

[Minsu Lee](https://github.com/minsulee2/devops-eng-training)
