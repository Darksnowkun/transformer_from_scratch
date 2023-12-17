from load_data import load_data, generate_less_sample_data
import torch
from components.FeedForward import FeedForward

test_data = generate_less_sample_data(sample_of_data=10)

FeedForward()

print("test")