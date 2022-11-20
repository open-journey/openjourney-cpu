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

Go to line 9 of the file `main.py` and then change the value of prompt to whatever you like. Then simply run this:

```bash
python3 main.py
``` 

The final image will be saved as `image.png` in the current working directory. In order to change the name, you can modify line 15 of the `main.py` file. Or better, you can randomize it using libraries like `uuid`. 

_IMPORTANT_: __DO NOT__ change line 10. 

_IMPORTANT_: This will change soon and there will be some `argparse` or `sys.argv` stuff in the code. This is a fast _proof of concept_ I wrote for a friend.

## TODO List

- [ ] Adding argument and flag support to the code. 
- [ ] Working on the naming of the output files.