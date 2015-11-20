import numpy as np

def extract_weights(model):
	weights = []
	for layer in model:
		w = layer.get_weights()
		if w is None:
			continue
		weights.append(w)
	W = np.concatenate(weights)
	return W


def load_weights(model, W):
	for layer in model:
		w = layer.get_weights()
		if w is None:
			continue
		w_shape = w.shape
		w, W = np.split(W, [np.prod(w_shape)])
		layer.set_weights(w.reshape(w_shape))
	return model


def extract_grads(model):
	grads = []
	for layer in model:
		g = layer.get_grads()
		if g is None:
			continue
		grads.append(g)
	dW = np.concatenate(grads)
	return dW


def forward(model, input):
	for layer in model:
		input = layer.forward(input)
	return input


def backward(model, gradient):
	for layer in reversed(model):
		gradient = layer.backward(gradient)


def forget(model):
	for layer in model:
		layer.forget()
