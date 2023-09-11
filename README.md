# mnist-flask

## json

```
curl --location 'http://localhost:7777/predict-all' \
--header 'Content-Type: application/json' \
--data '{
    "img": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAACR0lEQVR4nO2Wv2vyYBDH73FQKNnEQYhb6VhCBMkgdHTQUft/CF3cpA5ODnVzEgrBqUu6OYg/QMGlbo42lCoZqoVOwl2/76RQ3kaTvqVQeA9uuXzvPs/z3B1EERHoBy3yk7D/wKOWTqep3W6TiFC73SbTNAPl4StuGAbW6zWYee8vLy9BcsPDMpkMnp6eICJgZmw2G3ieB2aGZVmIRqPfAzw5OUE2m8Xj4yOYeQ+cTqcoFov7WKVS8a0RqoetVov6/T7puv4hbpomaZpGg8GAiIjOz899awQGptNpyufzpJQipRQNh0O6uroipRStVit6eHigZrNJkUiElFIHa4UekPv7e2iahnw+j0qlgkQisdeKCN7e3mCa5td6eHZ2Btu2ISLwPA+z2QzFYtFXv+urbdvhgbFYDI7jgJnx+vqKXC6HeDwOXdePAkejUXigZVn7Z7y4uAg0yf8EHI/HEBH0er3AqwMAIuIL9J3SQqFAhmEQAHIcx0/2l72/vxMAms1mvppPT1IqlcDMWC6XSCaTR28Wi8VQr9chIuh2u9A0LdyT7oCLxSIQrFargZnhui5yudwh/WHgzc3NQZhhGLBtG8yMu7u7IH3+/MPl5SVEBK7r+iaXy2Ws12uICG5vb4MO1uEbbrdbNJtNGIaBVCqFUqkEx3Hgui5EBIvFAp1OB5ZlfQ9w58/Pz5jP5x9io9EI19fXgVfmIFDXdUwmk33x3UIzMzzPO9rb0EAiQjKZRLVa/QBsNBo4PT39KgxqR/0p+11/bb8C+AckZQshd9lmNQAAAABJRU5ErkJggg=="
}'
```

## form-data

```
curl --location 'http://localhost:7777/predict-all' \
--form 'img=@"img/mnist_0.png"'
```

## form-urlencoded

```
curl --location 'http://localhost:7777/predict-all' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'img=iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAACR0lEQVR4nO2Wv2vyYBDH73FQKNnEQYhb6VhCBMkgdHTQUft/CF3cpA5ODnVzEgrBqUu6OYg/QMGlbo42lCoZqoVOwl2/76RQ3kaTvqVQeA9uuXzvPs/z3B1EERHoBy3yk7D/wKOWTqep3W6TiFC73SbTNAPl4StuGAbW6zWYee8vLy9BcsPDMpkMnp6eICJgZmw2G3ieB2aGZVmIRqPfAzw5OUE2m8Xj4yOYeQ+cTqcoFov7WKVS8a0RqoetVov6/T7puv4hbpomaZpGg8GAiIjOz899awQGptNpyufzpJQipRQNh0O6uroipRStVit6eHigZrNJkUiElFIHa4UekPv7e2iahnw+j0qlgkQisdeKCN7e3mCa5td6eHZ2Btu2ISLwPA+z2QzFYtFXv+urbdvhgbFYDI7jgJnx+vqKXC6HeDwOXdePAkejUXigZVn7Z7y4uAg0yf8EHI/HEBH0er3AqwMAIuIL9J3SQqFAhmEQAHIcx0/2l72/vxMAms1mvppPT1IqlcDMWC6XSCaTR28Wi8VQr9chIuh2u9A0LdyT7oCLxSIQrFargZnhui5yudwh/WHgzc3NQZhhGLBtG8yMu7u7IH3+/MPl5SVEBK7r+iaXy2Ws12uICG5vb4MO1uEbbrdbNJtNGIaBVCqFUqkEx3Hgui5EBIvFAp1OB5ZlfQ9w58/Pz5jP5x9io9EI19fXgVfmIFDXdUwmk33x3UIzMzzPO9rb0EAiQjKZRLVa/QBsNBo4PT39KgxqR/0p+11/bb8C+AckZQshd9lmNQAAAABJRU5ErkJggg=='
```

## binary

```
curl --location 'http://localhost:7777/predict-all' \
--header 'Content-Type: application/octet-stream' \
--data '@img/mnist_8.png'
```