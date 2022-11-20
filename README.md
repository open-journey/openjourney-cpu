# Run OpenJourney on CPU

The script provided in this particular repository is for users who have no GPU or have small amounts of GPU VRAM available. Please note that this process takes a very, very long time to generate images but still is better than nothing 😁

## Dependencies 

1. Install `pytorch`:

```
pip3 install torch torchvision torchaudio
```

2. Install `diffusers` and `transformers`:

```
pip3 install diffusers transformers scipy ftfy
```

## How to generate images

Go to line 9 of the file `main.py` and then change the value of prompt to whatever you like.

_IMPORTANT_: __DO NOT__ change line 10. 

_IMPORTANT_: 